#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

################
# Theme Config #
################
THEME = "themes/Flex"

AUTHOR = u'Ryan T. Harter'
SITENAME = u'blog.harterrt.com'
SITEURL = 'http://blog.harterrt.com'
SITETITLE = 'Ryan T. Harter'
SITESUBTITLE = 'Data Engineer @ Mozilla'
SITEDESCRIPTION = 'Weblog for Ryan T. Harter'
SITELOGO = 'https://www.gravatar.com/avatar/8259d4073ed8ba5f61f5d60c978b0e69'
BROWSER_COLOR = '#333'

MAIN_MENU = True
COPYRIGHT_YEAR = 2016

ROBOTS = 'index, follow'


############
# External #
############

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Links on the side panel
LINKS = (
        )

# Small links at the top of the page
MENUITEMS = (
            )

# PLUGINS:
PLUGIN_PATHS = ['./plugins']
PLUGINS = []
MD_EXTENSIONS = ['toc', 'codehilite','extra']

# Social widget
SOCIAL = (
          ('github', 'https://github.com/harterrt'),
          ('twitter', 'https://twitter.com/harterrt'),
          ('linkedin', 'http://www.linkedin.com/pub/ryan-harter/11/a24/a21'),
         )

# ADD_THIS_ID = 'ra-77hh6723hhjd'
# DISQUS_SITENAME = 'yoursite'
# GOOGLE_ANALYTICS = 'UA-1234-5678'
# GOOGLE_TAG_MANAGER = 'GTM-ABCDEF'
# STATUSCAKE = { 'trackid': 'your-id', 'days': 7, 'rumid': 1234 }


#########
# Admin #
#########
DEFAULT_PAGINATION = 10

# Copy the CNAME into root dir for GitHub
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# EXTRA_PATH_METADATA = {
#     'extra/custom.css': {'path': 'static/custom.css'},
# }
# CUSTOM_CSS = 'static/custom.css'
