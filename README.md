# xiangli-shaun.github.io

Source for **[xiangli-shaun.github.io](https://xiangli-shaun.github.io)** — the academic
homepage of Xiang "Shaun" Li, Assistant Professor of Radiology at Massachusetts General
Hospital and Harvard Medical School.

Built with [Jekyll](https://jekyllrb.com/) and the
[al-folio](https://github.com/alshedivat/al-folio) theme. Deployed to GitHub Pages.

---

## Running it locally

Requires **Ruby ≥ 3.1** (this site is built on 4.0.4 via `rbenv`) and ImageMagick.

```bash
brew install rbenv ruby-build imagemagick   # one time
cd ~/Desktop/al-folio-site
gem install bundler
bundle install                               # ~3-5 min the first time
bundle exec jekyll serve --livereload
```

Open <http://localhost:4000>.

Edits to `_pages/`, `_posts/`, `_news/` and `_bibliography/` reload automatically.
**Changes to `_config.yml` do not** — stop the server (Ctrl-C) and restart it.

---

## Where the content lives

| Path | Holds | Current |
|---|---|---|
| `_pages/about.md` | Homepage bio, profile block | — |
| `_bibliography/papers.bib` | All publications | 282 entries, 9 `selected` |
| `_news/` | Homepage news items, one file each | 6 |
| `_posts/` | Blog posts, `YYYY-MM-DD-slug.md` | 4 |
| `_data/cv.yml` | CV page content (RenderCV format) | 9 sections |
| `_data/socials.yml` | Profile links and icons | — |
| `_data/venues.yml` | Venue tags and colours for `abbr` keys | 24 venues |
| `_data/original_posts.yml` | Registry of the Chinese originals | 9 posts |
| `assets/img/`, `assets/pdf/` | Site images, CV PDF | — |
| `pdf/`, `img/` | **Legacy files from the previous site** | 70 PDFs |

Live pages: `/` · `/news/` · `/publications/` · `/blog/` · `/cv/` · `/repositories/`

### Two things not to break

**`pdf/` and `img/`** carry over from the previous version of this site. Their URLs
(`xiangli-shaun.github.io/pdf/CV_xiang.pdf` and similar) are cited externally, so they
are preserved verbatim. `keep_files` in `_config.yml` protects them from being
re-copied on every build — don't remove those two entries.

**`.nojekyll`** must reach the built output, which is why it is listed in `include:`.
Without it GitHub tries to re-build the already-built site and fails.

---

## Adding a paper

Export BibTeX from Google Scholar, paste into `_bibliography/papers.bib`, and add the
optional al-folio fields:

```bibtex
@inproceedings{key2026,
  title     = {...},
  author    = {Li, Xiang and ...},
  booktitle = {...},
  year      = {2026},
  abbr        = {NeurIPS},   % venue tag; see _data/venues.yml
  selected    = {true},      % also show on the homepage
  abstract    = {...},       % adds an "Abs" toggle
  arxiv       = {2601.12345},
  pdf         = {paper.pdf}, % bare filename -> assets/pdf/
  bibtex_show = {true}
}
```

Your name is bolded via the `scholar:` block in `_config.yml`, which matches
`Li` against `Xiang`, `X.`, `X` and `Shaun`.

`WORKFLOW.md` has the fuller guide — news items, thumbnails, hidden pages, troubleshooting.

---

## Deploying

Push to `master`. The `Deploy site` workflow builds the site and publishes the result
to the `gh-pages` branch, which GitHub Pages serves.

```bash
git push origin master
```

Then watch the **Actions** tab. A red X means the live site did not update.

- **`origin` uses SSH.** An HTTPS push is rejected, because updating
  `.github/workflows/deploy.yml` needs a token with the `workflow` scope, which
  `gh auth login` does not grant by default.
- **Never edit `gh-pages` by hand** — it is regenerated on every deploy.
- If the workflow does not trigger, run it manually: Actions → Deploy site → Run workflow.

`MIGRATION.md` records how the site was cut over from the previous version, including
the rollback tag `pre-al-folio`.

---

## Repository notes

- `SETUP.md`, `MIGRATION.md`, `WORKFLOW.md` are working notes, excluded from the build.
- `.github/_workflows_disabled/` holds upstream al-folio CI that is not used here.
- `bin/` holds upstream utility scripts; `update_scholar_citations.py` may be useful.

## License

Site content © Xiang Li. The al-folio theme is available under the
[MIT License](LICENSE).
