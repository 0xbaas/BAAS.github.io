# Security blog (Jekyll + Chirpy)

A Jekyll blog using the [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) theme, set up for security writeups, CTF notes, and infosec research — similar to [snowscan.io](https://snowscan.io) and [vuln.dev](https://vuln.dev).

## Features

- **Chirpy theme**: Clean layout with sidebar, dark/light mode, search, categories, archives, custom tabs
- **Navigation**: Home, Categories, Certifications, Archives, Tools, About
- **Syntax highlighting**: Rouge for code blocks (bash, python, etc.)
- **Atom feed**: Generated at `/feed.xml` for RSS readers
- **GitHub Pages**: Ready for deployment via GitHub Actions

## Quick start

### 1. Install Ruby and Bundler

- **Windows**: [RubyInstaller](https://rubyinstaller.org/) (use the one with DevKit), then `gem install bundler`
- **macOS**: `brew install ruby` then `gem install bundler`
- **Linux**: `sudo apt install ruby-full build-essential` then `gem install bundler`

### 2. Install dependencies

```bash
cd "My own website"
bundle install
```

### 3. Customize `_config.yml`

Edit at the top of `_config.yml`:

- `title` – blog name
- `tagline` – subtitle
- `url` – full site URL (e.g. `https://yourusername.github.io` for GitHub Pages)
- `social` – your name, email, Twitter, GitHub, LinkedIn, etc.
- `avatar` – path to your avatar (e.g. `/assets/img/avatar.png`)

Put your avatar image in `assets/img/avatar.png` (or another path you set).

### 4. Run locally

```bash
bundle exec jekyll serve
```

Open [http://localhost:4000](http://localhost:4000).

### 5. Write posts

Add a new file in `_posts/`:

- **Filename**: `YYYY-MM-DD-slug.md` (e.g. `2025-03-16-my-htb-box.md`)
- **Front matter**:

```yaml
---
title: Your post title
date: 2025-03-16 12:00:00 +0000
categories: [Hack The Box]   # or [Vulnlab], [Research], [Tools]
tags: [sqli, linux, privesc]
---
```

Write the body in Markdown. Use triple backticks for code with a language (e.g. `bash`, `python`). For images, place them in `assets/img/` or e.g. `assets/posts/2025-03-16-my-htb-box/` and link with `![alt](/assets/...)`.

## Deploy to GitHub Pages

1. Create a repo (e.g. `yourusername.github.io` for a user site).
2. Push this project to the repo.
3. In the repo: **Settings → Pages → Build and deployment**:
   - Source: **GitHub Actions**.
4. Push a commit (or run the “Build and Deploy” workflow manually). The site will be built and published.

If the repo is **not** `username.github.io`, set in `_config.yml`:

- `url: "https://yourusername.github.io"`
- `baseurl: "/your-repo-name"`

## Project structure

```
├── _config.yml       # Site config (title, url, social, theme options)
├── _posts/           # Blog posts (YYYY-MM-DD-title.md)
├── _tabs/            # Sidebar pages (categories, tags, archives, misc, about)
├── assets/img/       # Images (avatar, post images)
├── index.html        # Homepage
├── Gemfile           # Ruby dependencies
└── .github/workflows/pages-deploy.yml   # GitHub Actions for Pages
```

## License

Content is yours. The Chirpy theme is under [MIT](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/LICENSE).
