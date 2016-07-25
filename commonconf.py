#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)

# Theme Configuration
from flex_config import *

AUTHOR = u'Ryan T. Harter'
SITENAME = u'blog.harterrt.com'
SITEURL = 'http://blog.harterrt.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

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
