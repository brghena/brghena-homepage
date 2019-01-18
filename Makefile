SHELL := /bin/bash

all:
	./website.py
	$(MAKE) -C cv
	mkdir -p docs/cv/
	cp -r cv/*.pdf docs/cv/

local:	all
	pushd docs && python3 -m http.server 8000; popd

# Actually, make deploy isn't needed anymore since we're serving the docs/ folder from github
# But we can use it to push a redirect page to academic servers
deploy:	all
	scp -r redirect/. brghena@login.eecs.berkeley.edu:~/public_html/

clean: 
	rm -rf docs/
	rm -rf __pycache__
	$(MAKE) -C cv clean

.PHONY: all local deploy clean
