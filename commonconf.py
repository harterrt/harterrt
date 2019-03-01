#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)

PATH = 'content'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

################
# Theme Config #
################
THEME = "themes/harter"

AUTHOR = u'Ryan T. Harter'
SITENAME = u'blog.harterrt.com'
SITEURL = 'https://blog.harterrt.com'
SITETITLE = 'Ryan T. Harter'
TAGLINE = 'Senior Staff Data Scientist @ Mozilla'
SITEDESCRIPTION = 'Weblog for Ryan T. Harter'
USER_LOGO_URL = 'https://www.gravatar.com/avatar/8259d4073ed8ba5f61f5d60c978b0e69'
ROUND_USER_LOGO = True
BROWSER_COLOR = '#333'

############
# External #
############

# Links on the side panel
LINKS = (
    ('About', '/pages/about.html'),
    ('Resume', 'resume.pdf'),
    ('Github', 'https://github.com/harterrt'),
    ('Twitter', 'https://twitter.com/harterrt'),
    ('LinkedIn', 'http://www.linkedin.com/pub/ryan-harter/11/a24/a21'),
    ('Work Snippets', 'https://github.com/harterrt/snippets'),
)

# PLUGINS:
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['asciidoc_reader']
MD_EXTENSIONS = ['toc', 'codehilite','extra']

GOOGLE_ANALYTICS = 'UA-83638505-1'

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
ARTICLE_EXCLUDES = ['images']
