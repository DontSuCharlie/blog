#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Charlie Su'
SITENAME = "Charlie Su's Blog"
SITEURL = 'https://charliesu.com'

PATH = 'content'

TIMEZONE = 'America/Mazatlan'

DEFAULT_LANG = 'English'

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_DATE = 'fs'
DEFAULT_PAGINATION = 12

STATIC_PATHS = ['extra/CNAME', 'images']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
THEME = './themes/notmyidea'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Disabling the other default pages that pelican makes
# (http://docs.getpelican.com/en/stable/settings.html)
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
TAGS_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''