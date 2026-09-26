# Swapping xiangli-shaun.github.io over to al-folio

Your repo `xiangli-shaun/xiangli-shaun.github.io` currently serves plain HTML from the
root of `master`. al-folio works differently: `master` holds Jekyll **source**, a GitHub
Action builds it, and the generated HTML lands on a **`gh-pages`** branch that Pages
serves. So this is not a file swap — the serving model changes too.

Total time: ~20 minutes, most of it waiting on a build.

---

## Already done for you

- [x] `pdf/` (70 PDFs, 237 MB) copied in — every `xiangli-shaun.github.io/pdf/*.pdf`
      URL keeps resolving after cutover
- [x] `img/` (41 files) copied in for the same reason
- [x] `CV_xiang.pdf` also placed at `assets/pdf/` so the CV icon works
- [x] `keep_files: [pdf, img]` set, so Jekyll doesn't recopy 278 MB on every rebuild
- [x] `origin` set to `https://github.com/xiangli-shaun/xiangli-shaun.github.io.git`
- [x] Local branch is `master`, matching the remote

---

## Phase 0 — Back up the live site (2 min)

**Do not skip this.** It makes the whole migration one command to undo.

```bash
cd /tmp
git clone --depth 1 https://github.com/xiangli-shaun/xiangli-shaun.github.io.git backup-old
cd backup-old
git tag pre-al-folio
git push origin pre-al-folio
```

Confirm at `https://github.com/xiangli-shaun/xiangli-shaun.github.io/tags` that
`pre-al-folio` is listed. Your entire old site is now permanently recoverable.

Also grab a local copy you can't lose:
```bash
cd /tmp && zip -qr ~/Desktop/old-site-backup.zip backup-old && echo done
```

## Phase 0b — Grant the Action write permission (1 min)

The deploy Action creates the `gh-pages` branch, which it can't do with default
permissions. Set this **before** pushing or the first run fails.

1. Repo → **Settings** → **Actions** → **General**
2. Scroll to **Workflow permissions**
3. Select **Read and write permissions** → **Save**

---

## Phase 1 — Verify locally (5 min)

`_config.yml` changed, so the running server won't have picked it up. Restart it.

```bash
cd ~/Desktop/al-folio-site
# Ctrl-C the running server first
bundle exec jekyll serve --livereload
```

Check each of these at `localhost:4000`:

- [ ] Homepage loads, says **Xiang Li**, shows the bio
- [ ] News section shows the 2025 items
- [ ] `/publications/` lists 12 papers, **your name is bold** in each author line
- [ ] `localhost:4000/pdf/CV_xiang.pdf` opens the PDF  ← the critical one
- [ ] `localhost:4000/pdf/2939672.2939730.pdf` also opens (spot-check a second file)

If the `/pdf/` checks fail, **stop** — that means the legacy files aren't being copied
into the build and pushing would break every existing PDF link.

## Phase 2 — Push (2 min + build time)

```bash
cd ~/Desktop/al-folio-site
git push --force origin master
```

`--force` is required and safe here: the old history is preserved under the
`pre-al-folio` tag from Phase 0.

**If the push asks for a password:** GitHub removed password auth. Either use the `gh`
CLI (`brew install gh && gh auth login`, then push again), or switch to SSH:
```bash
git remote set-url origin git@github.com:xiangli-shaun/xiangli-shaun.github.io.git
```

## Phase 3 — Watch the Action (3-6 min)

Go to the repo's **Actions** tab. A run called **"Deploy site"** should be in progress.

- Green check → continue to Phase 4
- Red X → click in, read the failing step, fix locally, push again. **Do not continue
  to Phase 4 until it's green** — switching Pages to a branch that doesn't exist takes
  the site down.

Expect this run to be slower than normal (5+ min) because of the 278 MB of PDFs.

## Phase 4 — Confirm gh-pages exists (1 min)

Repo → branch dropdown → confirm **`gh-pages`** is now listed. Click it; you should see
generated HTML (`index.html`, `publications/`, `pdf/`, `assets/`), not your source files.

## Phase 5 — Point Pages at gh-pages (1 min)

1. Repo → **Settings** → **Pages**
2. **Source**: Deploy from a branch
3. **Branch**: `gh-pages`  ·  **Folder**: `/ (root)`
4. **Save**

## Phase 6 — Verify live (5 min)

Give it 2-3 minutes to propagate, then hard-refresh (Cmd-Shift-R):

- [ ] `https://xiangli-shaun.github.io` → the new site
- [ ] `https://xiangli-shaun.github.io/publications/` → your papers
- [ ] `https://xiangli-shaun.github.io/pdf/CV_xiang.pdf` → **your CV still works**
- [ ] One more legacy PDF of your choosing

That third one is the one that matters. If it 404s, roll back and diagnose.

---

## Rollback

If anything goes wrong, restore the old site in under a minute:

1. **Settings → Pages → Source → Branch: `master` / root → Save**
2. ```bash
   cd /tmp/backup-old
   git push --force origin pre-al-folio:master
   ```

You're back to exactly what was live before. Nothing is lost.

---

## Safer alternative: rehearse first

If you'd rather not point the real URL at this until you've seen it work end to end:

1. Create a new empty repo `xiangli-shaun/al-folio-test`
2. In `_config.yml` set `baseurl: "/al-folio-test"`
3. Push there, run Phases 3-5 against it
4. Confirm `https://xiangli-shaun.github.io/al-folio-test` renders
5. Set `baseurl: ""` again, then run the real migration

Costs an extra 20 minutes, removes essentially all risk.

---

## After the dust settles

- The 26 PDFs not linked from your old pages are still served — fine, but you could
  prune them later to speed up builds.
- `_config.yml` → `keep_files` is what protects `pdf/` and `img/`. Don't remove those
  two lines.
- Never edit the `gh-pages` branch by hand; it's regenerated on every push to `master`.
