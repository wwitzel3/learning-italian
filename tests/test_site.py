import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

import pytest
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent

PAGES = [
    ("Home", "index.html"),
]

JAPANESE_TERMS = [
    "kana",
    "hiragana",
    "katakana",
    "kanji",
    "furigana",
    "textractor",
    "visual novel",
    "jmdict",
    "pitch accent",
]

SECTIONS = {
    "index.html": ["What this site is", "Who it's for", "How to use it", "Credits"],
}


@pytest.fixture(scope="session")
def build(tmp_path_factory):
    site_dir = tmp_path_factory.mktemp("site")
    result = subprocess.run(
        ["mkdocs", "build", "--strict", "--site-dir", str(site_dir)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return result, site_dir


@pytest.fixture(scope="session")
def site(build):
    result, site_dir = build
    assert result.returncode == 0, result.stderr
    return site_dir


def soup(site_dir, page):
    return BeautifulSoup((site_dir / page).read_text(), "html.parser")


def test_strict_build_succeeds(build):
    result, _ = build
    assert result.returncode == 0, result.stderr


def test_nav_tabs_follow_the_page_order(site):
    tabs = soup(site, "index.html").select("a.md-tabs__link")
    assert [tab.get_text(strip=True) for tab in tabs] == [title for title, _ in PAGES]


@pytest.mark.parametrize("page", SECTIONS)
def test_page_has_its_expected_sections(site, page):
    headings = soup(site, page).select("article h2")
    assert [h.get_text(strip=True) for h in headings] == SECTIONS[page]


def test_home_credits_donkuri(site):
    links = soup(site, "index.html").select("article a[href]")
    assert "https://donkuri.github.io/learn-japanese/" in [a["href"] for a in links]


@pytest.mark.parametrize("page", [page for _, page in PAGES if page != "index.html"])
def test_page_has_no_japanese_specific_terms(site, page):
    text = soup(site, page).select_one("article").get_text(" ").lower()
    found = [t for t in JAPANESE_TERMS if re.search(rf"\b{t}\b", text)]
    assert found == []


@pytest.mark.parametrize("page", [page for _, page in PAGES])
def test_internal_links_and_images_resolve(site, page):
    page_path = site / page
    for tag, attr in (("a", "href"), ("img", "src")):
        for element in soup(site, page).select(f"article {tag}[{attr}]"):
            url = urlsplit(element[attr])
            if url.scheme or url.netloc:
                continue
            target = (page_path.parent / unquote(url.path)).resolve() if url.path else page_path
            if target.is_dir():
                target = target / "index.html"
            assert target.is_file(), f"{element[attr]} on {page}"
            if url.fragment:
                assert soup(site, target.relative_to(site)).find(id=url.fragment), (
                    f"#{url.fragment} on {page}"
                )


def test_search_index_covers_every_page(site):
    index = json.loads((site / "search" / "search_index.json").read_text())
    indexed = {doc["location"].split("#")[0] for doc in index["docs"]}
    expected = {"" if page == "index.html" else page.removesuffix("index.html") for _, page in PAGES}
    assert expected <= indexed


def test_repo_docs_folder_is_not_published(site):
    for source in (ROOT / "docs").rglob("*.md"):
        built = site / source.relative_to(ROOT / "docs").with_suffix("")
        assert not built.exists(), f"{source} was published"
