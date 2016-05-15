#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Keith Kelly'
SITENAME = 'Keith Kelly'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('github', 'http://github.com/kwkelly'),
        ('twitter', 'http://twitter.com/keithkelly'),)

DEFAULT_PAGINATION = 10

THEME = "./pelican-themes/pelican-bootstrap3/"
BOOTSTRAP_THEME = "flatly"


STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'thumbs']
EXTRA_PATH_METADATA = {
        'extra/robots.txt': {'path': 'robots.txt'},
        'extra/favicon.ico': {'path': 'favicon.ico'}
        }

PLUGIN_PATHS = ['./pelican-plugins/']

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

RELATIVE_URLS = False

MENUITEMS = (('Blog', '/blog/'), ('About' ,'/about/'),)

ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

INDEX_SAVE_AS = '/blog/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
