# Mining

Mining means turning a word you don't know into an Anki card while you read or watch Italian. You meet the word, look it up with Yomitan, and click once to save it. The card keeps the sentence you found it in, so you review the word in the context where it first confused you.

This page covers four kinds of material: web pages, video, ebooks and comics. Each one needs a slightly different set of tools, but the core is the same. Yomitan must be able to read the text, and Anki must be open to receive the card.

Don't mine every unknown word. Pick words you have seen more than once, or words that stop you from following what's happening. Ten cards you care about are easier to review than forty you added out of habit.

## Setting up Anki and Yomitan for mining

Everything on this page builds on the [Setup](setup.md) page. If you haven't finished it, do that first. Mining relies on these pieces from Setup:

- Anki is open while you mine, with the AnkiConnect add-on installed. See [Connecting Yomitan to Anki](setup.md#connecting-yomitan-to-anki).
- **Enable Anki integration** is on in Yomitan's settings.
- **Configure Anki flashcards…** points at your Italian deck and the Lapis note type, with the markers from [Map Yomitan's markers to the fields](setup.md#map-yomitans-markers-to-the-fields).
- The `Sentence` field uses `{cloze-prefix}<b>{cloze-body}</b>{cloze-suffix}`. That marker is what carries the context onto your card on every medium below.

Two more Yomitan settings help once you mine every day. Both sit in the **Anki** section of Yomitan's settings.

- Leave **Check for card duplicates** on. When you look up a word you already have a card for, Yomitan marks the add button, so you don't make the same card twice.
- If you mine a lot from one source, add a word to **Card tags**, such as the name of the series or book. You can then search for those cards in Anki's browser later.

Yomitan also has a keyboard shortcut for adding a card. While a popup is showing, **Alt + E** adds the first word in it to Anki. You can see and change all of Yomitan's shortcuts under **Configure standard keyboard shortcuts…** in the **Shortcuts** section of its settings.

The rest of this page assumes you hold **Shift** to scan a word, as the Setup page describes. If you changed the **Scan modifier key**, use your own key instead.

## Web setup

Start on the web. Yomitan works on almost any page with no extra tools.

### Tools

- A browser with Yomitan installed and set up as on the [Setup](setup.md) page.
- Anki, open, with AnkiConnect.

### Mining from an article

1. Open an Italian article. A news site such as [Il Post](https://www.ilpost.it/) writes in clear, modern Italian. The [Resources](resources.md) page lists more sources.
2. Read until you hit a word you don't know. Hold **Shift** and move the mouse over it.
3. Read the entry in the popup. If the word is a verb form such as "tornerebbe", Yomitan shows the base verb "tornare" and names the form.
4. Click the add button next to the word at the top of the entry, or press **Alt + E**.
5. Keep reading. Check the card in Anki at the end of your session, not after each one, so that you don't break your reading.

Yomitan takes the sentence from the text around the word. It stops at a full stop, question mark or exclamation mark. If the article splits a sentence across two lines or boxes, the card may only get half of it. When that happens, open the card in Anki and fix the `Sentence` field by hand.

### Mining from Wikipedia

The Italian Wikipedia at [it.wikipedia.org](https://it.wikipedia.org/) covers every subject you care about, and its articles stay in a neutral register that suits learners.

1. Pick a topic you already know well in English, such as your job or a hobby. Knowing the facts lets you guess more of the Italian.
2. Scan and add words the same way as on an article.
3. Follow the links inside the article. Related pages reuse the same words, so you meet your new words again straight away.

Wikipedia sentences can be long. If one runs to three lines, cut it in Anki down to the clause that holds the word.

### Adding a picture

The `Picture` field stays empty when you mine from the web, as the Setup page explains. For concrete nouns such as food or animals, copy a photo from the page and paste it into the `Picture` field in Anki's editor.

## Video setup

Video lets you mine a word together with the voice that said it. With the right tools, one card gets the subtitle line as the sentence, a recording of that line, and a still from the scene.

The tool that makes this work is asbplayer, a free browser extension. It shows a subtitle file over a video in your browser as text that Yomitan can scan. It also records the audio of a subtitle line and captures a screenshot, and sends both to Anki through AnkiConnect.

### Tools

- Chrome or Edge, with Yomitan. asbplayer also runs in Firefox, but its documentation says some features are limited there, so use a Chromium-based browser for mining.
- asbplayer, from the [Chrome Web Store](https://chromewebstore.google.com/detail/asbplayer-language-learni/hkledmpjpaehamkiehglnbelcpdflcab) or [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/asbplayer-language-learning/). Its documentation is at [docs.asbplayer.dev](https://docs.asbplayer.dev/).
- Anki, open, with AnkiConnect.
- Italian subtitles for what you watch.

### Where to get Italian subtitles

asbplayer can pick up subtitles on its own from some streaming sites. Its compatibility list includes Netflix, YouTube, Disney Plus and Amazon Prime Video, though it notes timing problems on Prime. On these sites you don't need a subtitle file.

- **Netflix.** Italian productions such as *Summertime*, *Baby* and *La legge di Lidia Poët* have Italian audio and Italian subtitles. Many foreign shows also have Italian dubs with Italian subtitles, but dubbed subtitles often differ from what the actors say.
- **YouTube.** Many Italian channels upload their own subtitles. Automatic captions exist for most Italian videos, but they often lack punctuation and mishear words, so they make poor sentences for cards.
- **RaiPlay.** Italy's public broadcaster, at [raiplay.it](https://www.raiplay.it/), streams films, series and documentaries for free. Programmes marked "sottotitolati" have Italian subtitles, which you turn on with the speech bubble icon in the player. You need a free account, and most of the catalogue only plays from inside Italy. RaiPlay is not on asbplayer's list of supported sites, so asbplayer won't load its subtitles for you.
- **Subtitle files.** For films and series you have on disk, search [OpenSubtitles](https://www.opensubtitles.com/) for an Italian `.srt` file. Check that the file matches your version of the video, because a subtitle made for a different cut drifts out of sync.

### Set up asbplayer for Lapis

asbplayer can fill some Lapis fields, and Yomitan fills the rest. Set asbplayer to fill only the fields Yomitan can't.

1. Open asbplayer's settings and find the Anki section.
2. Leave the **AnkiConnect URL** at `http://127.0.0.1:8765`, the same address Yomitan uses.
3. Set **Deck** to your Italian deck and **Note Type** to **Lapis**.
4. Set the **Audio** field to `SentenceAudio`.
5. Set the **Image** field to `Picture`.
6. Leave the **Sentence**, **Word** and **Definition** fields empty. Yomitan already fills `Sentence`, `Expression` and `MainDefinition`, and it bolds the word in the sentence. If asbplayer wrote the sentence as well, it would replace Yomitan's version.

### Load subtitles on a streaming site

1. Start the video on the streaming site.
2. On a supported site such as Netflix or YouTube, asbplayer detects the site's subtitle tracks. Turn on its **Auto-load detected subtitles** setting and it loads them for you, then shows them over the video.
3. To use a subtitle file instead, click the puzzle piece icon in your browser's toolbar, choose asbplayer, then **Open Side Panel**. Click **Load Subtitles** and pick your `.srt` file.
4. Turn off the site's own subtitles, so you only see asbplayer's.

If the lines appear too early or too late, asbplayer has keyboard shortcuts to shift the subtitle offset in 100 millisecond steps. They are listed in its settings.

### Load subtitles for a local video

1. Go to [app.asbplayer.dev](https://app.asbplayer.dev/).
2. Drag your video file and its subtitle file onto the page together.
3. The video plays in the page, with the subtitle list beside it.

The steps below work the same way here.

### Mine a line

1. When you hear a word you don't know, pause the video.
2. Hold **Shift** over the word in the subtitle. Yomitan's popup appears.
3. Click Yomitan's add button. Yomitan creates the card with the word, the bolded sentence, the definition and the word audio.
4. Straight away, press **Ctrl + Shift + U**. This is asbplayer's "update last card" shortcut. It records the audio of the current subtitle line, takes a screenshot, and adds both to the card you just made.
5. Resume the video.

Keep the Anki card browser closed while you do this. asbplayer's documentation warns that the update may not show up if the browser window is open.

If you want to check the clip before it goes on the card, press **Ctrl + Shift + X** instead of **Ctrl + Shift + U**. asbplayer opens its Anki dialog. There you can drag the time range to include a line before or after, pick a different frame for the screenshot, and then click the button to update the last card.

### Tips for video

- Mine from series rather than films at first. The same characters reuse the same words every episode.
- Adjust **Audio padding start** and **Audio padding end** in asbplayer's settings if the clips cut off the first or last syllable.
- Play the sentence audio on the back of each card. It trains your ear on real speed and intonation.

## Ebook setup

Novels repeat their vocabulary over hundreds of pages, so the words you mine in chapter one come back in chapter ten. To mine from them, you need a reader that shows the book's text as real text in the browser, so Yomitan can scan it.

### Tools

- Koodo Reader, a free, open-source ebook reader with a web version at [web.koodoreader.com](https://web.koodoreader.com/). It reads EPUB, MOBI, AZW3, PDF and plain text, among other formats.
- Yomitan and Anki, as above.
- Italian ebooks in EPUB format without DRM.

Koodo shows each page of the book inside the browser as ordinary text. Yomitan scans text inside embedded frames, so the popup works in Koodo the same way it does on a web page. A book you buy from a store with DRM won't open in Koodo, so start with free books.

### Where to get Italian ebooks

- [Liber Liber](https://liberliber.it/) is an Italian non-profit digital library that has run since 1994. Its Progetto Manuzio holds thousands of Italian classics. Each book's page has a **Scarica gratis** section with EPUB, PDF and ODT files.
- [Project Gutenberg](https://www.gutenberg.org/browse/languages/it) has over a thousand books in Italian, free and in EPUB. Collodi's *Le avventure di Pinocchio* is a good first novel, because it was written for children and its chapters are short.

Classics from Liber Liber and Gutenberg are in the public domain, so their Italian is often a century old or more. Expect some spellings and verb forms that sound formal today. The [Recommendations](recommendations.md) page suggests modern books once you're ready to buy.

### Read and mine

1. Open [web.koodoreader.com](https://web.koodoreader.com/).
2. Click **Import** and choose your EPUB file. Koodo asks where to keep your data. You can let it store books in the browser, or pick a folder on your computer so that clearing your browser data doesn't delete your library.
3. Click the book's cover. Koodo opens the book in a new tab.
4. Read. When you hit an unknown word, hold **Shift** over it and add the card from Yomitan's popup as usual.

The `Picture` and `SentenceAudio` fields stay empty on book cards. That's fine. If you want sound, Yomitan's word audio still fills `ExpressionAudio`.

Italian novels often mark dialogue with guillemets or dashes, and a line of speech may run into the narration. Trim the sentence in Anki if it doesn't make sense on its own.

## Comics setup

Italy has a large comics tradition, including *Topolino*, *Dylan Dog*, *Tex* and the work of Zerocalcare. Most comics are images, though, so Yomitan can't read their speech balloons directly. The fix is to turn the text in a panel into real text with optical character recognition (OCR), then look it up in Yomitan's search page.

### Tools

- Yomitan's search page, built into Yomitan. Open it with the magnifying glass in Yomitan's toolbar menu, or press **Alt + Insert**.
- An OCR tool that reads Italian:
    - On a Mac, Live Text is part of macOS. Apple lists Italian among its supported languages.
    - On Windows, Text Extractor is part of Microsoft's free [PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/text-extractor). It uses the Windows OCR language packs, so you need the Italian pack installed. Microsoft's page explains how to check for it and add it.
- Anki, open, with AnkiConnect.
- Your comic, as a digital file or scanned pages you can view on screen.

### Set up the search page to watch the clipboard

1. Open Yomitan's settings and go to the **Clipboard** section.
2. Turn on **Enable search page clipboard text monitoring**. Your browser asks for permission to read the clipboard. Allow it.
3. Open Yomitan's search page and turn on the **Clipboard monitor** switch at the top.

From now on, any text you copy appears in the search page on its own, as text you can scan.

### Mine a balloon

1. Open the comic in any viewer and find a balloon with a word you don't know.
2. Copy the balloon's text with your OCR tool:
    - On a Mac, open the page in Preview or Photos, then drag across the text in the balloon to select it, and press **Command + C**.
    - On Windows, press **Win + Shift + T** to start Text Extractor, then drag a box around the balloon. The text goes to your clipboard.
3. Switch to Yomitan's search page. The balloon's text is there.
4. Check the text against the image. OCR sometimes misreads comic lettering, which is often all capitals and hand drawn. Fix any wrong letters in the search box.
5. Hold **Shift** over the unknown word in the text and add the card from the popup. Yomitan takes the sentence from the balloon text.

Yomitan ignores capital letters when it matches a word, so all-capitals lettering is no problem. Accents are different. If the OCR turns "è" into "e" or "perché" into "perche", add the accent back before you look the word up.

To add the panel as the card's picture, take a screenshot of it, then paste it into the `Picture` field in Anki.

### Digital comics with real text

Some webcomics put their dialogue on the page as text instead of drawing it into the image. If you can select a word in a balloon with the mouse, Yomitan can scan it directly, as on any web page. Try this first with anything you read in a browser.
