.PHONY: serve build post

serve:
	hugo serve

build: 
	hugo

post:
	pipenv run -- python scripts/hugo_new.py post