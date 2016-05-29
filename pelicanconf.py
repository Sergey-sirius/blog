#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Keith Kelly'
SITENAME = 'kwkelly'
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
         ('Magnific Popup', 'http://dimsemenov.com/plugins/magnific-popup/'),
         ('Linode', 'https://www.linode.com/'),
         ('CloudFlare', 'https://www.cloudflare.com/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('github', 'http://github.com/kwkelly'),
        ('twitter', 'http://twitter.com/keithkelly'),
        ('linkedin', 'https://www.linkedin.com/in/keith-kelly-b705379'),)

DEFAULT_PAGINATION = 10

THEME = "../pelican-themes/pelican-bootstrap3/"
BOOTSTRAP_THEME = "flatly"


STATIC_PATHS = ['images', 'extra/robots.txt', 'thumbs', 'extra/favicons']
EXTRA_PATH_METADATA = {
        'extra/robots.txt': {'path': 'robots.txt'},
        }

PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = ['photos', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']
NOTEBOOK_DIR = 'notebooks'
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

RELATIVE_URLS = True

MENUITEMS = (('Blog', '/blog/'), ('About' ,'/about/'),)

ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

INDEX_SAVE_AS = '/blog/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PHOTO_LIBRARY = "~/Pictures"
PHOTO_GALLERY = (4096, 4096, 80)
PHOTO_ARTICLE = (768, 768, 80)
PHOTO_THUMB = (512, 512, 60)
