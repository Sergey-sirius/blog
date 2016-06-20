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
# LINKS = (
#     ('Pelican', 'http://getpelican.com/'),
#     ('Python.org', 'http://python.org/'),
#     ('Magnific Popup', 'http://dimsemenov.com/plugins/magnific-popup/'),
#     ('Linode', 'https://www.linode.com/'),
#     ('CloudFlare', 'https://www.cloudflare.com/'),
#     ('Jinja2', 'http://jinja.pocoo.org/')
# )

# Social widget
SOCIAL = (
    ('github', 'http://github.com/kwkelly'),
    ('twitter', 'http://twitter.com/keithkelly'),
    ('linkedin', 'https://www.linkedin.com/in/keith-kelly-b705379'),
)

DEFAULT_PAGINATION = 10

THEME = "../pelican-themes/pelican-bootstrap3/"
BOOTSTRAP_THEME = "flatly"

READERS = {'html': None}
STATIC_PATHS = [
    'images', 'extra/robots.txt',
    'thumbs', 'extra/favicons', 'embed_html',
    'extra'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

MATH_JAX = {
    'color': 'black', 'align': 'center', 'responsive': True,
    'responsive_break': True
}
PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = [
    'photos', 'liquid_tags.img', 'liquid_tags.video',
    'liquid_tags.youtube', 'liquid_tags.vimeo',
    'liquid_tags.include_code', 'liquid_tags.notebook',
    'html_rst_directive', 'render_math','summary'
]
NOTEBOOK_DIR = 'notebooks'
# EXTRA_HEADER = open('_nb_header.html').read()

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Relative vs absolute URLs and https
# https://github.com/getpelican/pelican/issues/1532
RELATIVE_URLS = False

MENUITEMS = (
    ('blog', '/blog/'), ('about', '/about/'),
)

INDEX = 'index.html'
ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + INDEX
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + INDEX
TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = TAG_URL + INDEX
CATEGORY_URL = 'blog/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + INDEX

INDEX_SAVE_AS = '/blog/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PHOTO_LIBRARY = "~/Pictures"
PHOTO_GALLERY = (4096, 4096, 80)
PHOTO_ARTICLE = (768, 768, 80)
PHOTO_THUMB = (512, 512, 60)
#HIDE_SIDEBAR=True
# DISQUS_SITENAME = "kwkelly"
HTMLLOGO = '<span style="color:#adacac">kw</span>kelly'
HIDE_SITENAME = True
