SHELL := /bin/bash

all:
	./website.py
	$(MAKE) -C cv
	mkdir -p docs/cv/
	cp -r cv/*.pdf docs/cv/

local:	all
	pushd docs && python3 -m http.server 8000; popd

deploy:	all
	scp -r docs/* brghena@web.eecs.umich.edu:~/public_html/
	scp -r docs/* brghena@login.eecs.berkeley.edu:~/public_html/

clean: 
	rm -rf docs/
	rm -rf __pycache__
	$(MAKE) -C cv clean

.PHONY: all local deploy clean
