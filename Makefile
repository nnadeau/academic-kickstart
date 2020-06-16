.PHONY: serve
serve:
	hugo version
	hugo serve --gc --minify

.PHONY: build
build:
	hugo --gc --minify

.PHONY: publications
publications: format-publications
	academic import --bibtex publications.bib

.PHONY: format-publications
format-publications:
	bibtool -s publications.bib -o publications.bib

.PHONY: post
post:
	python3 scripts/hugo_new.py new post

.PHONY: talk
talk:
	python3 scripts/hugo_new.py new talk

.PHONY: optimize
optimize: optimize-featured-size optimize-jpg optimize-png

FEATURED_IMAGES := $(shell find content assets static -iname "featured.*")
.PHONY: optimize-featured-size
optimize-featured-size:
	for F in $(FEATURED_IMAGES) ; do \
		mogrify -resize 1024x $$F ; \
	done

JPG_IMAGES := $(shell find content assets static -iname "*.jpg")
.PHONY: optimize-jpg
optimize-jpg:

PNG_IMAGES := $(shell find content assets static -iname "*.png")
.PHONY: optimize-png
optimize-png:
	for F in $(PNG_IMAGES) ; do \
		optipng $$F ; \
	done

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

.PHONY: featured-image
featured-image:
	python3 scripts/featured_image.py create_image
