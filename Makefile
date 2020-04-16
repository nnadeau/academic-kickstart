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
