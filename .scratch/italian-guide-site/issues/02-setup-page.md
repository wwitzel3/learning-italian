# 02: Setup page

**What to build:** A learner can follow the Setup page from a fresh machine to a working Anki and Yomitan install for Italian, where one click in Yomitan turns a looked-up word into an Anki card with its sentence, definition, audio and picture.

**Blocked by:** 01 (Home page and build test)

**Status:** ready-for-agent

- [x] The Setup page sits in the spec's nav position, after Home and Guide.
- [x] The Anki section covers installing Anki, turning on FSRS, and a recommended daily new-card limit with the reason for it.
- [x] The Yomitan section covers installing Yomitan, installing current Wiktionary-derived Italian dictionaries, and connecting to Anki through AnkiConnect.
- [x] The page recommends an existing note type and lists its fields: word, sentence, definition, audio and picture.
- [x] Before writing, the agent checks the current Yomitan docs for Italian language support and dictionary names, and does not rely on memory.
- [x] Screenshots, if any, are new images, and the page reads fine without them.
- [x] The build test lists Setup in the nav order and lists its expected sections.
- [x] The full test suite passes.
