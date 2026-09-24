# learning-italian

An English-language guide to learning Italian through immersion, built with MkDocs Material. The pages live in `site-src/`.

## Preview locally

```sh
uv venv .venv
uv pip install -p .venv -r requirements.txt
.venv/bin/mkdocs serve
```

Then open http://127.0.0.1:8000. Run the tests with `.venv/bin/pytest tests`.

## Publish to GitHub Pages

The workflow in `.github/workflows/pages.yml` runs the tests, builds the site with `--strict`, and deploys it on every push to `main`. Pull requests run the tests and the build without deploying.

To turn it on, once per repository:

1. Push this repository to GitHub.
2. In the repository, open Settings, then Pages, and set Source to "GitHub Actions".
3. Push to `main`, or run the "Publish site" workflow from the Actions tab.

The site appears at `https://<user>.github.io/<repo>/`. The workflow passes that address to MkDocs as `SITE_URL`, so links and the 404 page work under the repository path. A custom domain set in the Pages settings is picked up the same way.
