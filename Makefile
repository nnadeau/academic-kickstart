.PHONY: serve build post publications format-publications

serve:
	hugo version
	hugo serve --gc --minify

build:
	hugo --gc --minify

post:
	pipenv run -- python scripts/hugo_new.py post

publications:
	pipenv run -- academic import --bibtex publications.bib

format-publications:
	bibtool -s publications.bib -o publications.bib
