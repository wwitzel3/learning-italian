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
    ("Guide", "guide/index.html"),
    ("Setup", "setup/index.html"),
    ("Immersion", "immersion/index.html"),
    ("Mining", "mining/index.html"),
    ("Resources", "resources/index.html"),
    ("Recommendations", "recommendations/index.html"),
    ("Miscellaneous", "miscellaneous/index.html"),
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
    "lapis",
]

SECTIONS = {
    "index.html": ["What this site is", "Who it's for", "How to use it", "Credits"],
    "guide/index.html": [
        "Learn pronunciation and spelling",
        "Set up Anki and Yomitan",
        "Learn basic grammar and vocabulary",
        "Consume native content",
        "Talk and write to Italian speakers",
        "What's next",
        "Checklist",
    ],
    "mining/index.html": [
        "Setting up Anki and Yomitan for mining",
        "Web setup",
        "Video setup",
        "Ebook setup",
        "Comics setup",
    ],
    "setup/index.html": [
        "Anki setup",
        "Yomitan setup",
        "Connecting Yomitan to Anki",
        "Card note type",
    ],
    "immersion/index.html": [
        "How do I build a daily routine?",
        "Does immersion get easier?",
        "When should I start speaking and writing?",
        "Are textbooks bad?",
        "How do I stay motivated?",
        "How do I choose what to watch and read?",
        "What about regional accents and dialects?",
        "Is Italian-dubbed media good immersion?",
        "Should I use subtitles?",
        "What's the difference between active and passive listening?",
        "Should I get a tutor or take classes?",
        "I read too slowly. What do I do?",
        "Is mining words from a dictionary worth it?",
        "How do I avoid arguments about method?",
    ],
    "resources/index.html": [
        "Italian learning guides",
        "Flashcards and dictionaries",
        "Pronunciation",
        "Grammar",
        "Listening",
        "General resources",
    ],
    "recommendations/index.html": [
        "Start here",
        "Series",
        "Films",
        "Books",
        "Fumetti",
        "Podcasts",
        "YouTube",
    ],
    "miscellaneous/index.html": ["Why input works", "Certifications"],
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
    assert all((site / page).is_file() for _, page in PAGES)
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


def built_page_for(source):
    relative = source.relative_to(ROOT / "docs")
    if relative.stem in ("index", "README"):
        return relative.parent / "index.html"
    return relative.with_suffix("") / "index.html"


def test_repo_docs_folder_is_not_published(site):
    sources = list((ROOT / "docs").rglob("*.md"))
    assert sources
    for source in sources:
        assert not (site / built_page_for(source)).exists(), f"{source} was published"


def test_guide_checklist_renders_as_checkboxes(site):
    checklist = soup(site, "guide/index.html").find("h2", string="Checklist").find_next("ul")
    items = checklist.find_all("li", recursive=False)
    assert items
    assert all(item.find("input", type="checkbox") for item in items)


def test_resources_names_nativepractice_the_top_phrase_resource(site):
    article = soup(site, "resources/index.html").select_one("article")
    links = [a["href"] for a in article.select("a[href]")]
    assert "https://nativepractice.com/" in links
    assert "top resource for practising and learning Italian phrases" in article.get_text(" ")
