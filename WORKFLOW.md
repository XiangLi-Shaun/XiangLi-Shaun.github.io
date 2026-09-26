# Day-to-day: running this site yourself

## The mental model

Three things are **your content**. Everything else is machinery you can ignore.

```
_bibliography/papers.bib   <- publications
_news/*.md                 <- the "news" items on the homepage
_pages/about.md            <- homepage bio
_data/socials.yml          <- your profile links
assets/img/, assets/pdf/   <- photos, PDFs, posters, slides
```

You never write HTML. You edit a `.bib` or a `.md`, Jekyll regenerates the site.

## The loop

Leave this running in a terminal while you work:

```bash
cd ~/Desktop/al-folio-site
bundle exec jekyll serve --livereload
```

Then: edit a file → save → the browser tab at `localhost:4000` refreshes itself.
When it looks right:

```bash
git add -A
git commit -m "Add NeurIPS 2026 paper"
git push
```

GitHub Actions rebuilds the live site, usually in 2–5 minutes. Watch it under the
repo's **Actions** tab; a red X there means the live site didn't update.

> **The one gotcha:** edits to `_config.yml` are *not* picked up by `--livereload`.
> Stop the server (Ctrl-C) and restart it. Everything else is live.

---

## Adding one paper

### Step 1 — get the BibTeX

Google Scholar → your profile → click the paper → the `"` (quote) icon → **BibTeX**.
Or grab it from arXiv ("Export BibTeX citation") or the publisher's page.

### Step 2 — paste it into `_bibliography/papers.bib`

Anywhere in the file. Order doesn't matter — jekyll-scholar sorts by year, newest
first. Make sure the citation key (the bit right after `{`) is unique.

### Step 3 — add the al-folio extras

Raw BibTeX renders fine, but these optional fields are what make the entry useful:

```bibtex
@inproceedings{yourkey2026,
  title     = {Your Paper Title Here},
  author    = {Li, Xiang and Coauthor, Ada},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2026},

  abbr        = {NeurIPS},          % the colored tag on the left
  selected    = {true},             % ALSO show this on the homepage
  abstract    = {One paragraph...}, % adds an "Abs" toggle button
  arxiv       = {2601.12345},       % identifier ONLY, not the full URL
  pdf         = {mypaper.pdf},      % bare filename -> looks in assets/pdf/
  code        = {https://github.com/you/repo},
  website     = {https://project-page.example},
  bibtex_show = {true},             % adds a "Bib" button showing the BibTeX
  preview     = {mypaper.png},      % thumbnail, from assets/img/publication_preview/
  doi         = {10.1000/xyz123},
  altmetric   = {true},             % Altmetric badge (needs doi)
  dimensions  = {true},             % Dimensions citation badge (needs doi)
  award       = {Best Paper Award}  % highlighted banner on the entry
}
```

Only `title`, `author`, `year` and a venue are required. Add the rest as you have them.

### Step 4 — check and push

Save the file, look at `localhost:4000/publications/`, then commit and push.

---

## Recipes

**Put a paper on the homepage** — add `selected = {true}` to it. The homepage shows
`selected` papers only; `_pages/about.md` controls whether that block appears.

**Your name in bold** — `_config.yml` → the `scholar:` block has `last_name: [Li]` and
`first_name: [Xiang, X., Shaun]`. Any author matching those combinations gets bolded.
Add more spellings to the list if a journal renders you differently.

**Host a PDF** — drop the file in `assets/pdf/`, then reference the bare filename:
`pdf = {mypaper.pdf}`. Same pattern for `slides`, `poster`, `supp`.

**Add a thumbnail** — put the image in `assets/img/publication_preview/`, reference the
bare filename via `preview = {...}`. Roughly 3:2, a few hundred KB.

**Add a news item** — create `_news/2026-03-14-something.md`:
```markdown
---
layout: post
date: 2026-03-14 09:00:00-0400
inline: true
related_posts: false
---

Our paper on X was accepted at **CVPR 2026**.
```
The filename date and the `date:` field should agree. `inline: true` = one-liner on the
homepage. Copy an existing file in `_news/` rather than typing this from scratch.

**Make the venue tag a link** — `_data/venues.yml` maps an `abbr` to a URL and a color.

**Turn on a hidden page** — `_pages/cv.md`, `blog.md`, `repositories.md` all have
`nav: false` in their front matter. Change to `nav: true`.

**Edit the bio** — `_pages/about.md`, below the `---`. Plain Markdown.

---

## When something breaks

| Symptom | Cause |
|---|---|
| Change doesn't appear locally | It was a `_config.yml` edit — restart the server |
| A paper vanished from the list | Malformed BibTeX; check for an unbalanced `{` |
| "Liquid Exception" on build | Usually a stray `{{` or `{%` in Markdown text |
| Local looks fine, live site doesn't update | Check the repo's **Actions** tab for a failed run |
| Everything is broken | `git diff` to see what changed, or `git checkout -- <file>` to revert it |

Because it's all in git, nothing you do is unrecoverable. `git log` and `git revert`
are your undo button.
