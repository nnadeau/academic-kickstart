.PHONY: serve build post

serve:
	hugo serve --gc --minify

build: 
	hugo --gc --minify

post:
	pipenv run -- python scripts/hugo_new.py post