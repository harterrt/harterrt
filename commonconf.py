#!/usr/bin/env python
import os
import sys
import datetime as dt
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
TAGLINE = 'Principal Data Scientist @ Mozilla'
SITEDESCRIPTION = 'Weblog for Ryan T. Harter'
USER_LOGO_URL = 'https://www.gravatar.com/avatar/8259d4073ed8ba5f61f5d60c978b0e69'
ROUND_USER_LOGO = True
BROWSER_COLOR = '#333'

MAIN_MENU = True
COPYRIGHT_YEAR = dt.date.today().year

ROBOTS = 'index, follow'


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
)

# Small links at the top of the page
MENUITEMS = (
)

DISPLAY_PAGES_ON_MENU = False

# PLUGINS:
PLUGIN_PATHS = ['./plugins']
PLUGINS = []
MARKDOWN = {
    'markdown.extensions.codehilite': {},
    'markdown.extensions.toc': {},
    'markdown.extensions.extra': {},
}

GOOGLE_ANALYTICS = 'UA-83638505-1'

#########
# Admin #
#########

IGNORE_FILES = ['.*', 'README.*']
DEFAULT_PAGINATION = 20

# Copy the CNAME into root dir for GitHub
STATIC_PATHS = ['images', 'static', 'extra/CNAME', 'extra/resume.pdf']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/resume.pdf': {'path':'resume.pdf'},
}
ARTICLE_EXCLUDES = ['images', 'static']
