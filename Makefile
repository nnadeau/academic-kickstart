# hugo commands

.PHONY: clean
clean:
	rm -rf public

.PHONY: serve
serve: clean
	hugo version
	hugo serve --gc --minify

.PHONY: serve-notebooks
serve-notebooks: clean
	pipenv run watchmedo tricks tricks.yaml

.PHONY: serve-future
serve-future: clean
	hugo version
	hugo serve --gc --minify --buildFuture

.PHONY: build-hugo
build-hugo:
	hugo --gc --minify

.PHONY: build-notebooks
build-notebooks:
	pipenv run python scripts/convert_notebooks.py

.PHONY: build
build: build-notebooks build-hugo

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# publications

.PHONY: publications
publications: format-publications
	academic import --bibtex publications.bib --normalize

.PHONY: format-publications
format-publications:
	bibtool -s publications.bib -o publications.bib

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# content

.PHONY: post
post:
	pipenv run python scripts/hugo_new.py new post

.PHONY: notebook
notebook:
	pipenv run python scripts/hugo_new.py new post --notebook

.PHONY: convert-notebooks
convert-notebooks:
	pipenv run python scripts/convert_notebooks.py

.PHONY: talk
talk:
	pipenv run python scripts/hugo_new.py new talk

.PHONY: project
project:
	pipenv run python scripts/hugo_new.py new project

.PHONY: featured-image
featured-image:
	pipenv run python scripts/featured_image.py create_image

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
