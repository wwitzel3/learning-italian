# Spec: Immersion-based Italian learning site

Status: ready-for-agent

## Problem Statement

I want to learn Italian through immersion, the way donkuri's "Immersion-Based Japanese Learning" site (donkuri.github.io/learn-japanese) teaches Japanese. That site gives a learner one opinionated path: a roadmap from day one, an exact Anki and Yomitan setup, an FAQ on the doubts that come up during immersion, per-medium mining workflows, and a curated list of resources. I haven't found an equivalent for Italian. The Italian resources I've found are mostly textbook courses or scattered Reddit threads, and none of them tells an English speaker "do this, then this, with these tools."

The Japanese site can't be reused as it stands. Much of it is specific to Japanese: kana drills, kanji, pitch accent, visual-novel text hooking, Japanese dictionaries. Its repository also states no licence, so I can't copy its prose.

## Solution

A static documentation site, written in English, with the same shape as the Japanese one and content rebuilt for Italian:

- **Home**: what the site is, who it's for, and credit to donkuri's site as the model.
- **Guide**: a numbered roadmap from zero to reading native content, ending in a checklist.
- **Setup**: step-by-step Anki and Yomitan configuration for Italian.
- **Immersion**: an FAQ on routine, motivation, output, textbooks, grammar, accents and dialects, and dubbed media.
- **Mining**: how to turn unknown words into Anki cards from web pages, video, ebooks and comics.
- **Resources**: dictionaries, grammar references, listening sources and other guides.
- **Recommendations**: Italian media to start with, grouped by medium and difficulty.
- **Miscellaneous**: the theory behind input-based learning, and the Italian certifications.

It keeps the Japanese site's look: tab navigation, light and dark modes, search, and click-to-zoom images.

## User Stories

1. As a beginner, I want the home page to tell me what the site is and whether it's for me, so that I don't waste time on the wrong method.
2. As a beginner, I want one ordered roadmap, so that I always know the next step.
3. As a beginner, I want to learn Italian pronunciation and spelling first, so that I can read words aloud correctly from the start.
4. As a beginner, I want the rules for c/g before e and i, gl, gn, sc and double consonants spelled out, so that I stop mispronouncing common words.
5. As a beginner, I want to know how written stress works (the grave accent on final vowels) and that stress elsewhere is unmarked, so that I know when to check a dictionary.
6. As a beginner, I want a starting vocabulary deck recommendation, so that most words in my first immersion aren't new to me.
7. As a beginner, I want to know which grammar to cover before immersing (articles, articulated prepositions, present-tense conjugation, the passato prossimo), so that I can parse simple sentences.
8. As a beginner, I want to be told plainly how much grammar study is enough, so that I don't stay in textbooks for a year.
9. As a learner, I want to install and configure Anki with the exact settings the guide recommends, so that my reviews don't pile up.
10. As a learner, I want the guide to cover FSRS and a recommended daily new-card limit, so that I don't burn out.
11. As a learner, I want to install Yomitan with Italian dictionaries, so that I can look up words by hovering over them in my browser.
12. As a learner, I want Yomitan and Anki connected, so that one click turns a looked-up word into a card.
13. As a learner, I want a recommended card note type and its fields (word, sentence, definition, audio, picture), so that my cards carry context.
14. As a learner, I want to mine words from web articles and Wikipedia, so that anything I read in a browser becomes study material.
15. As a learner, I want to mine words from video with Italian subtitles, so that I can learn from films, series and YouTube.
16. As a learner, I want to know where to get Italian subtitles and how to load them into a browser video player, so that subtitle-based mining works on the content I watch.
17. As a learner, I want to mine words from Italian ebooks, so that I can move to novels.
18. As a learner, I want a workflow for Italian comics (fumetti), so that I can mine from them too.
19. As a learner, I want each mining workflow to list its tools and setup steps, so that I can follow it without outside help.
20. As a learner, I want advice on building a daily immersion routine, so that I keep going on busy days.
21. As a learner, I want to hear that immersion gets easier over time, so that I don't quit during the hard first months.
22. As a learner, I want an answer on when to start speaking and writing, so that I can stop worrying about output too early or too late.
23. As a learner, I want a fair take on textbooks, so that I know when a textbook helps and when it slows me down.
24. As a learner, I want guidance on choosing immersion material I enjoy, so that I stay motivated.
25. As a learner, I want an explanation of standard Italian versus regional accents and dialects, so that I'm not thrown when a film character speaks Neapolitan or Sicilian.
26. As a learner, I want to know whether Italian-dubbed foreign films and series are good immersion, so that I can use media I already know, since Italy dubs almost all foreign films and TV.
27. As a learner, I want advice on subtitles: Italian, English, or none, so that I get the most from what I watch.
28. As a learner, I want the difference between active and passive listening explained, so that I know how much a podcast playing while I do chores counts toward my listening.
29. As a learner, I want a view on tutors and classes, so that I know whether and when to pay for them.
30. As a learner, I want reassurance and tactics for slow reading, so that I keep reading instead of switching back to English.
31. As a learner, I want to know whether mining words straight from a dictionary is worth it, so that I use my time well.
32. As a learner, I want advice on avoiding method wars online, so that I don't lose weeks to arguing.
33. As a learner, I want a list of Italian dictionaries (monolingual and bilingual), so that I can look up what Yomitan misses.
34. As a learner, I want grammar references I can consult when a sentence won't parse, so that I'm not stuck.
35. As a learner, I want listening sources: public broadcasters, podcasts and YouTube channels, so that I have free input at every level.
36. As a learner, I want links to other good Italian-learning guides, so that I can compare approaches.
37. As a learner, I want media recommendations grouped by medium and rough difficulty, so that I can pick a first series or book.
38. As a learner, I want a short "just give me three things to start" list, so that I'm not stuck choosing.
39. As a curious learner, I want the theory behind comprehensible input explained, so that I trust the method.
40. As a learner planning study or work in Italy, I want the Italian certifications (CILS, CELI, PLIDA, CERT.IT) compared, so that I can pick one.
41. As a learner, I want a checklist at the end of the guide, so that I can track which stages I've done.
42. As a reader, I want to search the whole site, so that I can find a topic without clicking through tabs.
43. As a reader, I want light and dark modes that follow my system setting, so that the site is comfortable at night.
44. As a reader, I want to click a screenshot to enlarge it, so that I can read small settings panels.
45. As a reader, I want tab navigation across the top and previous/next links at the bottom of each page, so that I can read the site in order.
46. As a reader on a phone, I want the site to work on a narrow screen, so that I can read the guide on my commute.
47. As the site owner, I want the site to build without warnings, so that broken links and missing pages are caught before I publish.
48. As the site owner, I want an automated check that no Japanese-specific instructions survived the adaptation, so that learners never get told to install a Japanese tool.
49. As the site owner, I want the home page to credit donkuri's site, so that readers know where the approach comes from.

## Implementation Decisions

- **Toolchain.** MkDocs with the Material theme, the same stack as the Japanese site. A requirements file pins the Python dependencies.
- **Source folder.** Site pages live in `site-src/`, and the MkDocs config points its docs directory there. The repo's `docs/` folder holds agent instructions in `docs/agents/`, which must never appear on the site.
- **Pages.** Eight Markdown pages, one per section in the Solution list, in that nav order. Each page's section headings follow the matching page on the Japanese site, except where an Italian section replaces a Japanese-only one:
  - Guide: "Learn kana" becomes "Learn pronunciation and spelling". Drop the two kanji sections. Pronunciation, Anki and Yomitan, basic grammar and vocabulary, native content, talking and writing to natives, what's next, and the checklist stay.
  - Immersion: "pitch accent" becomes "accents and dialects". The anime-subtitles question becomes a subtitles question plus a dubbed-media question.
  - Mining: the visual novel, anime, novel and manga setups become web, video, ebook and comics setups. Drop the Textractor-style text hooking section.
  - Resources: "Kana and Kanji" becomes "Pronunciation". The other groups stay.
  - Recommendations: the visual novel list becomes a short starter list across media.
  - Miscellaneous: input theory stays. Certifications covers the Italian exams.
- **Theme.** Material features `navigation.tabs`, `navigation.footer`, `toc.follow` and `header.autohide`. The palette offers light and dark schemes and follows the system preference, as the Japanese site does.
- **Search.** The built-in search plugin, with the language set to English and Italian so Italian words are stemmed and searchable ("parlare" matches "parlano").
- **Images.** The glightbox plugin for click-to-zoom. No images come from the Japanese site. Screenshots are new, and a page reads fine without them.
- **Language.** The site is in English, for English speakers. There is no translated version.
- **Content.** Write all prose fresh. Take structure and approach from the Japanese site, never its text. Check tool names, settings and links against each tool's current version.
- **Credit.** The home page links to donkuri's site as the model this one follows.
- **Build.** `mkdocs build --strict` must pass. Any warning (broken internal link, missing nav target, bad anchor) fails it.

## Testing Decisions

- **One seam: the built site.** A single pytest module builds the site once per session with `mkdocs build --strict` into a temporary directory and asserts on the generated HTML. Nothing tests the Markdown source, the MkDocs config, or pages one at a time.
- **What a good test here checks:** what a reader would see or hit. For example "the Mining page has a Video setup section" or "this link goes somewhere that exists."
- **Assertions:**
  - The strict build succeeds.
  - Every page in the nav exists in the output, and the nav order matches the Solution list.
  - Every page has its expected top-level sections, by heading text.
  - Every internal link and image reference resolves to a built file, and every in-page anchor exists.
  - Every page except Home is free of Japanese-specific terms: kana, hiragana, katakana, kanji, furigana, Textractor, visual novel, JMdict, pitch accent. Home is exempt so it can name and credit the Japanese site.
  - The home page links to donkuri's site.
  - No page built from the repo's `docs/` folder appears in the output.
  - The search index exists and contains every page.
- **Prior art:** none. The repo is empty, so this module sets the pattern.

## Out of Scope

- Any translated version of the site, including counterparts to the Japanese site's French pages.
- Deploying to GitHub Pages or anywhere else. The repo has no remote yet.
- Copying any text or image from the Japanese site.
- A shipped Anki note type, deck or add-on. The Setup page has the learner build a note type from Anki's Basic, because the maintained mining note types target Japanese.
- Browser tests of the theme toggle, search box or image zoom. Material and glightbox own that behaviour.
- Checking that external links are live.
- An Italian media recommendation spreadsheet like the Japanese site's. The Recommendations page is a hand-written list.

## Further Notes

- The Japanese site's Markdown source isn't public. Both of its branches hold only the built site (MkDocs 1.5.3, Material 9.5.1), so I took the page structure from the built HTML.
- Yomitan's Italian support and the Wiktionary-derived Italian dictionaries it uses change often. Check current install steps and dictionary names while writing the Setup page, rather than trusting memory.
- The Japanese site's checklist sits at the end of the Guide page, not on a page of its own. Keep it there.
