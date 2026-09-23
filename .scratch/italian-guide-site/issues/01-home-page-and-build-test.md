# 01: Home page and build test

**What to build:** A reader can open the site and see the Home page. It says what the site is, who it's for, and links to donkuri's "Immersion-Based Japanese Learning" site as the model it follows. The site has the Japanese site's look: tabs across the top, previous and next links in the footer, a light and dark palette that follows the system setting, search, and click-to-zoom images. A pytest module builds the site and checks what a reader would see, so every later page ticket only adds a page and its expectations.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [x] MkDocs with the Material theme builds from `site-src/`, and a requirements file pins the Python dependencies.
- [x] The theme enables `navigation.tabs`, `navigation.footer`, `toc.follow` and `header.autohide`, and offers light and dark schemes that follow the system preference.
- [x] Search indexes English and Italian. The glightbox plugin is on.
- [x] The Home page explains the site in fresh prose and links to donkuri.github.io/learn-japanese.
- [x] One pytest module runs `mkdocs build --strict` once per session into a temporary directory and asserts on the built HTML.
- [x] The test checks that the strict build succeeds.
- [x] The test checks nav order against one expected list of pages, which later tickets extend.
- [x] The test checks each page's expected top-level sections by heading text, from one table that later tickets extend.
- [x] The test checks that every internal link and image reference resolves to a built file and every in-page anchor exists.
- [x] The test checks that no page except Home contains kana, hiragana, katakana, kanji, furigana, Textractor, visual novel, JMdict or pitch accent.
- [x] The test checks that Home links to donkuri's site, that the search index exists and covers every page, and that nothing from the repo's `docs/` folder appears in the output.
- [x] The full test suite passes.
