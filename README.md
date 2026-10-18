# Nikita Dubitskiy — academic website

English: https://nikdubitskiy.github.io/

Русский: https://nikdubitskiy.github.io/ru/

Static bilingual website for GitHub Pages. No package installation, external fonts, analytics or paid hosting required.

## Edit content

1. Edit `TEXT` (page content) or `PAPERS` (publication list) in `scripts/build.py`.
2. Run `python3 scripts/build.py`.
3. Commit the generator and generated pages to `main`.

HTML is generated in advance: navigation, content and scientific links work without JavaScript. JavaScript adds publication filtering, theme switching and the email draft form. CV buttons download static PDF files.

## Publish

Repository Settings → Pages: **Deploy from a branch**, branch **main**, folder **/ (root)**. If already configured, pushing triggers the existing Pages build. `.nojekyll` serves the generated files directly.

## Search visibility

Includes page titles and descriptions, canonical URLs, English/Russian alternate links, Person structured data with a stable identity and scientific profile links, social metadata, sitemap and robots.txt.

After launch, verify ownership in Google Search Console and submit `https://nikdubitskiy.github.io/sitemap.xml`. Update the website URL in ORCID, Scholar, ResearchGate and CoLab. Link or redirect the old website where supported. These account changes require access to the respective services.

For a custom domain, change `BASE` in `scripts/build.py`, rebuild, and configure GitHub Pages and DNS. Domain registration is separate from free Pages hosting.

See `CONTENT_SOURCES.md` for sources and figure attribution. A website and structured data cannot guarantee a Google knowledge panel.

## Yandex

Ownership verification is published both as `yandex_129322c641eb4aed.html` and a `yandex-verification` meta tag, using the code supplied by the owner. Complete verification by clicking **Проверить** in the owner's Yandex Webmaster account, then add `https://nikdubitskiy.github.io/sitemap.xml` under **Индексирование → Файлы Sitemap**.

The sitemap includes language alternates and the portrait image. Crawlable HTML, individual Russian titles and descriptions, canonical URLs, connected JSON-LD identity and breadcrumbs support discovery. The original portrait is served from this domain and connected to the Person identity.

`site-config.json` holds public search verification codes and a public IndexNow key. It contains no passwords. To notify Yandex of updated URLs AFTER deployment, run `python3 scripts/notify_indexnow.py`. A 200 means receipt; a 202 means the key awaits verification. Neither guarantees inclusion or a position in search results.

References: https://yandex.ru/support/webmaster/ru/controlling-robot/sitemap and https://yandex.ru/support/webmaster/ru/indexnow/reference .

## Editorial content and themes

- `scripts/content.py`: sourced biography, conference records, Russian explanatory paper titles and page components. `scripts/build.py` keeps bibliographic records and generates HTML/SEO files.
- `assets/site.css`: responsive reading layout, translucent navigation and light/dark colour tokens. `assets/theme.js` applies the saved theme before first paint; the default follows system preferences. No account or tracking is used.
- The email form opens a `mailto:` draft with encoded subject and body. It does not send mail or store submissions. The visitor needs a configured email app, or can copy the address.
- The research atlas opens original images in an accessible dialog; links still open the original files without JavaScript.
- Rebuild with `python3 scripts/build.py`. The sitemap now includes 12 bilingual pages, including `/conferences/` and `/ru/conferences/`.

## CV downloads

The CV buttons link directly to static PDFs; no print-dialog JavaScript is required. After changing the biography, run `python scripts/build.py` and `python scripts/export_cv.py`. PDF export requires Python Playwright and Chromium at `/usr/bin/chromium`. Generated RU/EN files live in `assets/nikita-dubitskiy-cv-ru.pdf` and `assets/nikita-dubitskiy-cv-en.pdf`.

`scripts/science.py` contains original conceptual structure, electronic-state and device diagrams with visible source links. They are not crystallographic refinements or numerical band calculations.

## Google indexing and entity identity

`scripts/structured_data.py` connects the bilingual ProfilePage records, WebSite, Person, portrait, institute, laboratory and scholarly articles through stable identifiers. The same person is a coauthor of the listed publications; other listed authors are preserved. Abbreviated author lists remain partial. No follower counts, invented dates or knowledge-panel status are asserted. The 404 response contains no profile markup or language alternate links.

See [SEARCH_VISIBILITY.md](SEARCH_VISIBILITY.md) for the audit, Google Search Console setup, account updates and measurement plan. Google verification is included only when the owner supplies `google_site_verification` in `site-config.json`. IndexNow does not submit URLs to Google.

## Plain-text sitemap fallback

`sitemap.txt` lists the same 12 canonical URLs as `sitemap.xml` and is generated from the same routes. It is linked in robots.txt alongside the XML sitemap. This is a Google-supported alternative for a fresh Search Console submission while investigating the owner's reported XML fetch failure. It does not establish the cause of that failure or guarantee indexing. Submit the full address https://nikdubitskiy.github.io/sitemap.txt in Search Console.
