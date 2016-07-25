#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ryan T. Harter'
SITENAME = u'blog.harterrt.com'
SITEURL = 'http://blog.harterrt.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
          ('github', 'https://github.com/harterrt'),
         )

DEFAULT_PAGINATION = 10

# Copy the CNAME into root dir for GitHub
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Theme Configuration
# THEME = "themes/bootlex"
