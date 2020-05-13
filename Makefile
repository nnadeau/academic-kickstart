.PHONY: serve
serve:
	hugo version
	hugo serve --gc --minify

.PHONY: build
build:
	hugo --gc --minify

.PHONY: publications
publications: format-publications
	pipenv run -- academic import --bibtex publications.bib

.PHONY: format-publications
format-publications:
	bibtool -s publications.bib -o publications.bib

.PHONY: post
post:
	pipenv run python scripts/hugo_new.py new post

.PHONY: talk
talk:
	pipenv run python scripts/hugo_new.py new talk

.PHONY: optimize
optimize: optimize-featured-size optimize-jpg optimize-png

FEATURED_IMAGES := $(shell find content assets static -iname "featured.*")
.PHONY: optimize-featured-size
optimize-featured-size: $(FEATURED_IMAGES)
	mogrify -resize 1024x $?

JPG_IMAGES := $(shell find content assets static -iname "*.jpg")
.PHONY: optimize-jpg
optimize-jpg: $(JPG_IMAGES)
	jpegoptim -s $?

PNG_IMAGES := $(shell find content assets static -iname "*.png")
.PHONY: optimize-png
optimize-png: $(PNG_IMAGES)
	optipng $?

.PHONY: lighthouse
lighthouse:
	lighthouse https://www.nicholasnadeau.me --view
