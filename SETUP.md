# al-folio hello world — Xiang "Shaun" Li

Scaffolded from [al-folio](https://github.com/alshedivat/al-folio), pre-filled with
content pulled from your current site (xiangli-shaun.github.io).

---

## 1. Run it locally on your Mac

You already have `rbenv`. al-folio needs **Ruby >= 3.1**.

```bash
# one-time: toolchain
brew install rbenv ruby-build imagemagick      # imagemagick is needed by jekyll-imagemagick
rbenv install 3.3.6                            # skip if already installed: rbenv versions

# project setup
cd ~/Desktop/al-folio-site
rbenv local 3.3.6                              # writes .ruby-version
gem install bundler
bundle install                                 # ~3-5 min the first time

# serve
bundle exec jekyll serve --livereload
```

Then open **http://localhost:4000**. Edits to `_pages/`, `_news/`, `_bibliography/`
rebuild automatically. Changes to `_config.yml` require restarting the server.

### If `bundle install` fails
Almost always a native-extension build. In order:
1. `xcode-select --install`
2. `brew install imagemagick pkg-config`
3. Still stuck? Use Docker instead: `docker compose up` (Dockerfile is included).

---

## 2. What's already filled in

| File | Contents |
|---|---|
| `_config.yml` | Your name, `url: https://xiangli-shaun.github.io`, empty `baseurl` (correct for a user page) |
| `_pages/about.md` | Homepage bio: MGH/HMS, Kempner, research areas, PhD/postdoc, editorial service |
| `_data/socials.yml` | Scholar, GitHub, LinkedIn, ORCID, DBLP, Semantic Scholar, Mastodon, MGH profile, email |
| `_bibliography/papers.bib` | 12 of your papers; 5 flagged `selected={true}` so they appear on the homepage |
| `_news/` | 6 recent updates from 2025 |

Nav is on for **about / news / publications**. Blog, CV, and repositories pages are
present but hidden (`nav: false`) — flip them on when you want them.

---

## 3. TODO before this goes live

- [ ] **Replace `_bibliography/papers.bib`.** Author lists in it are placeholders.
      Google Scholar → your profile → select all → Export → BibTeX → paste over the file.
      Keep the `selected={true}` lines on whichever papers you want on the homepage.
- [ ] **`assets/img/prof_pic.jpg`** is still the al-folio demo photo. Drop yours in at
      that exact path (square crop, ~800x800).
- [ ] **`assets/pdf/CV_xiang.pdf`** is referenced in `_data/socials.yml` but the folder
      is empty — copy your CV PDF in under that name (the sandbox couldn't reach
      github.io to fetch it).
- [ ] Skim `_config.yml` for analytics / giscus comments / newsletter blocks you may
      want to switch on.

---

## 4. Deploy to GitHub Pages

Your existing site lives at `xiangli-shaun/xiangli-shaun.github.io`. **Branch the old
one first** so you can roll back.

```bash
cd ~/Desktop/al-folio-site
git remote add origin git@github.com:xiangli-shaun/xiangli-shaun.github.io.git
git push -u origin main --force        # only once you're happy with localhost:4000
```

Then in the repo: **Settings → Pages → Source = "Deploy from a branch" → `gh-pages` / root**.

`.github/workflows/deploy.yml` builds the Jekyll site on every push to `main` and
publishes the result to `gh-pages`. So `main` holds your source, `gh-pages` holds the
generated HTML — don't edit `gh-pages` by hand.

A safer first pass: push to a repo named `al-folio-test`, set `baseurl: /al-folio-test`
in `_config.yml`, confirm it renders at `xiangli-shaun.github.io/al-folio-test`, then
move it over and reset `baseurl` to `""`.

### Pulling upstream al-folio updates later
```bash
git remote add upstream https://github.com/alshedivat/al-folio.git
git fetch upstream && git merge upstream/main
```

---

## 5. What was trimmed from upstream

Demo pages (projects, teaching, books, profiles), demo blog posts and news, ~110 MB of
sample images/video/audio, and all upstream CI workflows except `deploy.yml`. The
disabled workflows are parked in `.github/_workflows_disabled/` if you want any back.
