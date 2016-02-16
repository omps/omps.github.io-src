#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'omps'
SITENAME = u'omps.in'
SITEURL = ''

PATH = 'content'
BOOTSTRAP_FLUID = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
BANNER = ''
BANNER_SUBTITLE = 'Just Hanging Around'
TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'
THEME = '/Users/omps/pelican-themes/pelican-bootstrap3'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://www.github.com/omps/'),
          ('linkedin', 'https://twitter.com/ohgnis'),
          ('twitter', 'https://in.linkedin.com/in/ompsingh'),
          ('stackoverflow', 'http://stackexchange.com/users/1543748/omps'),)

HIDE_SIDEBAR = False
DEFAULT_PAGINATION = 10

DOCUTIL_CSS = True
GITHUB_USER = 'omps'
GITHUB_REPO_COUNT = 'omps'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
