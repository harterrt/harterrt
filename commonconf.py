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
THEME = "themes/harterrt-svbhack"

AUTHOR = u'Ryan T. Harter'
SITENAME = u'blog.harterrt.com'
SITEURL = 'https://blog.harterrt.com'
SITETITLE = 'Ryan T. Harter'
TAGLINE = 'Staff Data Engineer @ Mozilla'
SITEDESCRIPTION = 'Weblog for Ryan T. Harter'
USER_LOGO_URL = 'https://www.gravatar.com/avatar/8259d4073ed8ba5f61f5d60c978b0e69'
ROUND_USER_LOGO = True
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
    ('Work Snippets', 'https://github.com/harterrt/snippets'),
    ('Resume', 'resume.pdf'),
    ('Github', 'https://github.com/harterrt'),
    ('Twitter', 'https://twitter.com/harterrt'),
    ('LinkedIn', 'http://www.linkedin.com/pub/ryan-harter/11/a24/a21'),
)

# Small links at the top of the page
MENUITEMS = (
)

# PLUGINS:
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['asciidoc_reader']
MD_EXTENSIONS = ['toc', 'codehilite','extra']

# Social widget
# SOCIAL = (
#          )

# ADD_THIS_ID = 'ra-77hh6723hhjd'
# DISQUS_SITENAME = 'blog-harterrt-com'
GOOGLE_ANALYTICS = 'UA-83638505-1'
# GOOGLE_TAG_MANAGER = 'GTM-ABCDEF'
# STATUSCAKE = { 'trackid': 'your-id', 'days': 7, 'rumid': 1234 }


#########
# Admin #
#########

IGNORE_FILES = ['.*', 'README.*']
DEFAULT_PAGINATION = 10

# Copy the CNAME into root dir for GitHub
STATIC_PATHS = ['images', 'extra/CNAME', 'extra/resume.pdf']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/resume.pdf': {'path':'resume.pdf'},
}

# EXTRA_PATH_METADATA = {
#     'extra/custom.css': {'path': 'static/custom.css'},
# }
# CUSTOM_CSS = 'static/custom.css'
