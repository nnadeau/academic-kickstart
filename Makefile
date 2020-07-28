# hugo commands

.PHONY: clean
clean:
	rm -rf public

.PHONY: serve
serve:
	hugo version
	hugo serve --gc --minify

.PHONY: build
build:
	hugo --gc --minify

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# publications

.PHONY: publications
publications: format-publications
	academic import --bibtex publications.bib

.PHONY: format-publications
format-publications:
	bibtool -s publications.bib -o publications.bib

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# content

.PHONY: post
post:
	python3 scripts/hugo_new.py new post

.PHONY: notebook
notebook:
	python3 scripts/hugo_new.py new post --notebook

.PHONY: talk
talk:
	python3 scripts/hugo_new.py new talk

.PHONY: featured-image
featured-image:
	python3 scripts/featured_image.py create_image

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# web deployment

# test google lighthouse metrics
.PHONY: lighthouse
lighthouse:
	lighthouse https://www.nicholasnadeau.me --view

.PHONY: lighthouse-local
lighthouse-local:
	lighthouse http://localhost:1313/ --view

# test netlify pipeline
.PHONY: netlify-build
netlify-build:
	netlify build

.PHONY: netlify-deploy
netlify-deploy: netlify-build
	netlify deploy --open

.PHONY: netlify-lighthouse
netlify-lighthouse: netlify-build
	lighthouse --view $(shell netlify deploy --json | jq -r ".deploy_url")
