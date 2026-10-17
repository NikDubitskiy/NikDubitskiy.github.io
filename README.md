# Nikita Dubitskiy — academic website

English: https://nikdubitskiy.github.io/

Русский: https://nikdubitskiy.github.io/ru/

Static bilingual website for GitHub Pages. No package installation, external fonts, analytics or paid hosting required.

## Edit content

1. Edit `TEXT` (page content) or `PAPERS` (publication list) in `scripts/build.py`.
2. Run `python3 scripts/build.py`.
3. Commit the generator and generated pages to `main`.

HTML is generated in advance: navigation, content and scientific links work without JavaScript. JavaScript adds publication filtering and the CV print button. Save CV as PDF through the browser print dialog.

## Publish

Repository Settings → Pages: **Deploy from a branch**, branch **main**, folder **/ (root)**. If already configured, pushing triggers the existing Pages build. `.nojekyll` serves the generated files directly.

## Search visibility

Includes page titles and descriptions, canonical URLs, English/Russian alternate links, Person structured data with a stable identity and scientific profile links, social metadata, sitemap and robots.txt.

After launch, verify ownership in Google Search Console and submit `https://nikdubitskiy.github.io/sitemap.xml`. Update the website URL in ORCID, Scholar, ResearchGate and CoLab. Link or redirect the old website where supported. These account changes require access to the respective services.

For a custom domain, change `BASE` in `scripts/build.py`, rebuild, and configure GitHub Pages and DNS. Domain registration is separate from free Pages hosting.

See `CONTENT_SOURCES.md` for sources and figure attribution. A website and structured data cannot guarantee a Google knowledge panel.

## Yandex

Ownership verification is published both as `yandex_129322c641eb4aed.html` and a `yandex-verification` meta tag, using the code supplied by the owner. Complete verification by clicking **Проверить** in the owner's Yandex Webmaster account, then add `https://nikdubitskiy.github.io/sitemap.xml` under **Индексирование → Файлы Sitemap**.

The sitemap includes language alternates and the portrait image. Crawlable HTML, individual Russian titles and descriptions, canonical URLs, visible Person microdata, JSON-LD identity and breadcrumbs support discovery. The original portrait is served from this domain and connected to the Person identity.

`site-config.json` holds public search verification codes and a public IndexNow key. It contains no passwords. To notify Yandex of updated URLs AFTER deployment, run `python3 scripts/notify_indexnow.py`. A 200 means receipt; a 202 means the key awaits verification. Neither guarantees inclusion or a position in search results.

References: https://yandex.ru/support/webmaster/ru/controlling-robot/sitemap and https://yandex.ru/support/webmaster/ru/indexnow/reference .
