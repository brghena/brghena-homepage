#!/usr/bin/env python3
# vim: set noet ts=4 sts=4 sw=4:

import sys,os
from sh import cp, mkdir

import jinja2 as jinja
import markdown

import logger

jinja_env = jinja.Environment(loader=jinja.FileSystemLoader('templates'))
header_tmpl = jinja_env.get_template('header.html')

mkdir('-p', 'docs')

def md_to_html(path, md_file):
	page = os.path.splitext(md_file)[0]
	with open('docs/{}.html'.format(page), 'w') as o:
		logger.info('Processing ' + md_file)
		content = markdown.markdown(open(os.path.join(path, md_file)).read(), extensions=['toc'])
		o.write(header_tmpl.render(active_page=page, content=content))

for md in os.listdir('pages'):
	if md[-3:] == '.md':
		md_to_html('pages', md)

# Put all static content in the docs folder
logger.info('Copying static content...')
for dirpath,dirnames,filenames in os.walk('static'):

	# Create the mirrored folders in the docs directory
	if len(dirnames) > 0:
		for dirname in dirnames:
			path = os.path.join(dirpath, dirname)
			path = 'docs' + path[6:] # now that there is a hack
			mkdir('-p', path)


	if len(filenames) > 0:
		for filename in filenames:
			ext = os.path.splitext(filename)[1]

			spath = os.path.join(dirpath, filename)
			dpath = 'docs' + spath[6:]
			if ext in [
					'.css', '.js', '.ttf', '.eot', '.svg', '.woff', '.png',
					'.pdf', '.pptx', '.doc', '.txt', '.gz', '.tgz', '.jpg', 
					] or filename in ['CNAME', 'favicon.ico']:
				# These do not need to be compiled in any way
				# Just copy them
				cp(spath, dpath)
			else:
				logger.debug('Skipping file: ' + spath)
