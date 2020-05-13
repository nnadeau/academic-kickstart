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


FEATURED_IMAGES := $(shell find content -iname "featured.*")
.PHONY: optimize-featured-size
optimize-featured-size: $(FEATURED_IMAGES)
	mogrify -resize 1024x $?

JPG_IMAGES := $(shell find content -iname "*.jpg")
.PHONY: optimize-jpg
optimize-jpg: $(JPG_IMAGES)
	jpegoptim -s $?

PNG_IMAGES := $(shell find content -iname "*.png")
.PHONY: optimize-png
optimize-png: $(PNG_IMAGES)
	optipng $?
