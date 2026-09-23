# Setup

This page gets two free programs working together. Anki is a flashcard app that decides when you should review each card. Yomitan is a browser extension that shows a dictionary entry when you hover over a word. Once you connect them, one click in Yomitan saves the word you looked up as an Anki card. The card holds the word, the sentence you found it in, an English definition, a recording of the word and, if you want one, a picture.

Plan on about an hour. Do the four sections in order, because each one relies on the one before it.

## Anki setup

### Install Anki

1. Go to [apps.ankiweb.net](https://apps.ankiweb.net/) and download the desktop version for your system. Anki runs on Windows, macOS and Linux, and the desktop version is free.
2. Run the installer and open Anki.
3. Anki opens on the Decks screen with one deck called "Default". You can rename it or create a new deck with the **Create Deck** button at the bottom of the screen. Call it something like "Italiano".

Anki also has phone apps. AnkiDroid for Android is free, and AnkiMobile for iPhone is a paid app that funds Anki's development. Both can sync with the desktop app through a free AnkiWeb account, so you can do reviews on your phone. You still need the desktop app, because Yomitan only talks to the desktop version.

### Turn on FSRS

FSRS is a scheduling method that Anki can use to decide when you see each card again. The Anki manual says it helps you remember more in the same amount of study time than Anki's older method. Turn it on before you add any cards.

1. On the Decks screen, click the gear icon to the right of your deck and choose **Options**.
2. Scroll to the **FSRS** section at the bottom of the page and switch **FSRS** on. This setting applies to your whole collection, not only to this deck.
3. Leave **Desired retention** at its default of 90%. This means Anki schedules each review for the point where you have about a 90% chance of still remembering the card. Higher values give you more reviews per day, and lower values give you more forgotten cards.
4. Click **Save** at the top right of the window.

Once you have a month or two of reviews, open the same page again and click **Optimize** under **FSRS parameters**. Anki then tunes the schedule to your own review history. The manual says once a month is often enough.

The Anki manual gives one more rule for FSRS. Keep every learning step and relearning step shorter than one day, so that you can finish them on the day you see the card. You'll find these under **Learning steps** and **Relearning steps** in the same Options page.

### Set a daily new-card limit

Open your deck's Options page again and find the **Daily Limits** section. It has two numbers:

- **New cards/day** is how many cards you have never seen before Anki shows you each day.
- **Maximum reviews/day** is a cap on reviews of cards you have already seen.

Set **New cards/day** to **10** for your first month. Set **Maximum reviews/day** to a large number, such as 9999, so Anki never hides reviews that are due.

The reason for starting low is that each new card creates reviews for weeks afterwards. The Anki manual says that if you learn 20 new cards a day, you can expect about 200 reviews a day once things settle down, so every new card a day adds about ten reviews a day. At 10 new cards you'll settle at about 100 reviews a day. That leaves time for the reading and listening that the [Immersion](immersion.md) page describes, and immersion is where most of your progress comes from.

After a month, time your reviews for a few days. If they fit into your day and you want to go faster, raise the limit to 15 or 20. If reviews start to feel like a chore you put off, lower it. Skipping days costs more than a smaller limit does, because missed reviews pile up.

## Yomitan setup

### Install the extension

Yomitan works in Chrome, Firefox and Edge. Install it from your browser's store:

- [Chrome Web Store](https://chrome.google.com/webstore/detail/yomitan/likgccmbimhjbgkjambclfkhldnlhbnn)
- [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/yomitan/)
- [Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/yomitan/idelnfbbmikgfiejhgmddlbkfgiifnnn)

After you install it, Yomitan opens a page called "Welcome to Yomitan!".

1. Under **Recommended Permissions**, turn on **Enable recommended permissions**. Without them, Yomitan can't read text on most websites.
2. Under **Import Dictionaries**, set **Language** to **Italian**. This tells Yomitan which language you are reading. With Italian selected, Yomitan ignores capital letters and accents when it matches a word. It also strips common elided words before an apostrophe, so hovering over "dell'Italia" finds "Italia" and hovering over "c'erano" finds "erano".
3. Leave **Enable audio playback for terms** on. Yomitan will fetch recordings of Italian words from online sources, including the Wiktionary and Lingua Libre recordings on Wikimedia Commons.

You can reopen these settings at any time. Click the Yomitan icon in your browser's toolbar, then click **Settings**.

### Install Italian dictionaries

Yomitan comes with no dictionaries. You add them yourself as .zip files. The best free Italian dictionaries for Yomitan come from the [wty project](https://yomidevs.github.io/wiktionary-to-yomitan/download/) run by the Yomitan developers. It converts Wiktionary, the free dictionary from the Wikimedia Foundation, into Yomitan's format and publishes new versions often.

Install these three to start:

| Dictionary | What it gives you | Size |
| --- | --- | --- |
| `wty-it-en` | Full entries in English from the English Wiktionary, with several meanings per word, example sentences and word origins. | about 16 MB |
| `wty-it-en-gloss` | Short English translations taken from the Italian Wiktionary's translation lists. | about 1 MB |
| `wty-it-en-ipa` | The pronunciation of each word in the International Phonetic Alphabet. | about 1 MB |

The main dictionary also lists conjugated and inflected forms, and Yomitan uses that list to find the base word. When you hover over "parlano", Yomitan shows the entry for "parlare" and labels the form as third-person plural present indicative.

The quickest way to install the main dictionary is from inside Yomitan:

1. Open Yomitan's settings. With **Language** set to Italian, click **Get recommended dictionaries…**.
2. Click **Download** next to `wty-it-en`. Wait for the import to finish.

To install the other two, paste their download links into Yomitan:

1. In settings, click **Configure installed and enabled dictionaries…**, then click **Import**.
2. Paste these two links into the box under **Import dictionaries from URLs**, one per line:

        https://huggingface.co/datasets/daxida/wty-release/resolve/main/latest/dict/it/en/wty-it-en-gloss.zip
        https://huggingface.co/datasets/daxida/wty-release/resolve/main/latest/dict/it/en/wty-it-en-ipa.zip

3. Click **Import from URLs** and wait for both to finish.

If the links ever stop working, go to the [wty download page](https://yomidevs.github.io/wiktionary-to-yomitan/download/), choose Italian as the source language and English as the target, and download the files there. You can then drag the .zip files onto Yomitan's **Import** window.

Wiktionary grows every week. To get the newest entries, open **Configure installed and enabled dictionaries…** and click **Check for Updates** every month or two.

Later, once you can follow simple Italian, add `wty-it-it`. It has definitions written in Italian, taken from the Italian Wiktionary. You can install it the same way from the wty download page, with Italian as both source and target. The [Resources](resources.md) page lists other Italian dictionaries to use when Yomitan's entries fall short.

### Try it out

Open any Italian web page, such as an article on [it.wikipedia.org](https://it.wikipedia.org/). Hold **Shift** and move your mouse over a word. A popup shows the dictionary entries. Click the speaker icon to hear the word. If you would rather not hold a key, you can change the **Scan modifier key** on the welcome page or in settings.

## Connecting Yomitan to Anki

Yomitan can't write to Anki by itself. An Anki add-on called AnkiConnect lets other programs on your computer add cards to Anki while Anki is open.

### Install AnkiConnect

1. In Anki, open the **Tools** menu and choose **Add-ons**.
2. Click **Get Add-ons…**.
3. Enter the code `2055492159` and click **OK**.
4. Close Anki and open it again. The add-on only starts after a restart.

To check that it works, leave Anki open and visit `http://127.0.0.1:8765` in your browser. The page should show a short message that includes the word "AnkiConnect".

### Turn on Anki integration in Yomitan

1. Open Yomitan's settings and scroll to the **Anki** section.
2. Turn on **Enable Anki integration**. Anki must be open when you do this.
3. Leave **AnkiConnect server address** at `http://127.0.0.1:8765`, the address AnkiConnect uses unless you change it.
4. By default, Yomitan tags every card it creates with "yomitan". If you don't want that tag, clear the **Card tags** box in the same section.

The card format comes next, and it needs the note type from the next section. Install that first, then come back to **Configure Anki flashcards…**.

## Card note type

A note type tells Anki which fields a card has and how to lay them out on screen. Don't build your own. Use Lapis, a free note type made for cards from Yomitan. The author of the guide this site is modelled on co-wrote it, and it needs no custom Yomitan templates.

### Install Lapis

1. Go to the [Lapis releases page](https://github.com/donkuri/lapis/releases) and download `Lapis.apkg` from the newest release.
2. In Anki, open the **File** menu and choose **Import**, then pick the file you downloaded. You can also double-click the file.
3. Anki adds a sample deck and the "Lapis" note type. You can delete the sample deck after you've looked at the example card. The note type stays.

### The fields you'll use

Lapis has more fields than an Italian learner needs, because it also covers features for other languages. Five of them hold what you want on every card:

| What it holds | Lapis field |
| --- | --- |
| Word | `Expression` |
| Sentence | `Sentence` |
| Definition | `MainDefinition` |
| Audio | `ExpressionAudio` |
| Picture | `Picture` |

Lapis also has a `SentenceAudio` field for a recording of the whole sentence, which the [video workflow](mining.md#video-setup) can fill in, and a `Glossary` field that holds the entries from all your dictionaries at once. Leave every other field empty. An empty field doesn't break the card.

### Map Yomitan's markers to the fields

Yomitan fills each field from a marker, a word in curly brackets that it swaps for real content when it creates the card.

1. In Yomitan's settings, go to the **Anki** section and click **Configure Anki flashcards…**.
2. Set **Deck** to your Italian deck.
3. Set **Model** to **Lapis**. Yomitan loads the Lapis fields into the **Field** column.
4. Type these markers into the **Value** column. You can also click the down arrow at the right of a value box and pick a marker from the list.

| Field | Value | What Yomitan puts there |
| --- | --- | --- |
| `Expression` | `{expression}` | The dictionary form of the word, such as "parlare" for "parlano". |
| `ExpressionAudio` | `{audio}` | A recording of the word. |
| `SelectionText` | `{popup-selection-text}` | Any text you highlighted inside the popup before adding the card. |
| `MainDefinition` | `{single-glossary-wty-it-en-gloss}` | The short English translation from one dictionary. |
| `Sentence` | `{cloze-prefix}<b>{cloze-body}</b>{cloze-suffix}` | The sentence around the word, with the word in bold as it appeared on the page. |
| `Picture` | leave empty | See below. |
| `Glossary` | `{glossary}` | The entries from every dictionary you have turned on. |

Leave all other values empty. If Yomitan has filled in a value you didn't ask for, delete it.

For `MainDefinition`, a short translation is easier to review than a long entry. If you'd rather have the full English entry, use `{single-glossary-wty-it-en}` instead. The exact marker names depend on the dictionary names, so pick them from the down-arrow list to be sure you have them right.

Keep `Expression` as the first field in the list. Yomitan and Anki check the first field to spot duplicates, and the word itself is the right thing to check.

The `Picture` field stays empty in this setup, because a web page seldom has one image that fits the word. When you mine from video, you'll add a still from the scene. On a web page you can paste an image into the field in Anki by hand. If you want Yomitan to add one, it has two markers for this: `{screenshot}` captures the visible part of the page, and `{clipboard-image}` takes whatever image you last copied.

### Add your first card

1. Make sure Anki is open.
2. Hold **Shift** over an Italian word on a web page.
3. In the popup, click the add button beside the word at the top of the entry. Its tooltip starts with "Add".

Switch to Anki and open your deck. The new card shows the word on the front. When you flip it, you see the sentence, the definition and the audio. If a field is empty or wrong, go back to **Configure Anki flashcards…** and check its value.

If you want the sentence on the front of the card as a hint, type an "x" into the card's `IsWordAndSentenceCard` field in Anki. Lapis has a few other card styles, each switched on the same way. Its [README](https://github.com/donkuri/lapis) describes them. Use only one at a time.

Your setup is done. Head to the [Immersion](immersion.md) page to plan how you'll use it, or to [Recommendations](recommendations.md) for something to read or watch first.
