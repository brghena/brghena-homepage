SHELL := /bin/bash

all:
	./website.py
	$(MAKE) -C cv
	mkdir -p html/cv/
	cp -r cv/*.pdf html/cv/

local:	all
	pushd html && python3 -m http.server 8000; popd

deploy:	all
	scp -r html/* brghena@web.eecs.umich.edu:~/public_html/
	scp -r html/* brghena@login.eecs.berkeley.edu:~/public_html/

clean: 
	rm -rf html/
	rm -rf __pycache__
	$(MAKE) -C cv clean

.PHONY: all local deploy clean
