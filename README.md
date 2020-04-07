[![Netlify Status](https://api.netlify.com/api/v1/badges/96cf62a7-5c7d-4610-b84f-de0afc34773c/deploy-status)](https://app.netlify.com/sites/competent-panini-00973b/deploys)

# Nicholas Nadeau

Personal website, portfolio, and blog.

## Usage

### New Post

```bash
# new post
hugo new post/abc-xyz.md
```

### New Publication

- Add bib entry to [`publications.bib`](publications.bib)
- Run `make publications`

## Tips

- YouTube embeds work better as an iFrame instead of Hugo shortcode
- Use `<!--more-->` in posts to limit summary
- Blank post summaries with `summary = " "`
- Summarize web pages: https://smmry.com/
