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
TAGLINE = 'Senior Staff Data Scientist @Shopify'
SITEDESCRIPTION = 'Weblog for Ryan T. Harter'
USER_LOGO_URL = 'https://www.gravatar.com/avatar/8259d4073ed8ba5f61f5d60c978b0e69'
ROUND_USER_LOGO = True
BROWSER_COLOR = '#333'
INDEX_SAVE_AS = 'chrono.html'

MAIN_MENU = True
COPYRIGHT_YEAR = dt.date.today().year

ROBOTS = 'index, follow'

############
# External #
############

# Links on the side panel
LINKS = (
    ('Newsletter', 'https://harterrt.substack.com/'),
    ('Github', 'https://github.com/harterrt'),
    ('LinkedIn', 'http://www.linkedin.com/pub/ryan-harter/11/a24/a21'),
    ('Twitter', 'https://twitter.com/harterrt'),
)

# Small links at the top of the page
MENUITEMS = (
    ('Writing', '/chrono.html'),
    ('About', '/pages/about.html'),
    ('Talks', '/pages/talks.html'),
    ('Resume', '/resume.pdf'),
)

DISPLAY_PAGES_ON_MENU = False

# PLUGINS:
PLUGIN_PATHS = ['./plugins']
PLUGINS = []
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}


#########
# Admin #
#########

IGNORE_FILES = ['.*', 'README.*']
DEFAULT_PAGINATION = False

# Copy the CNAME into root dir for GitHub
STATIC_PATHS = ['images', 'static', 'extra/CNAME', 'extra/resume.pdf',
                'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/resume.pdf': {'path':'resume.pdf'},
    'extra/favicon.ico': {'path':'favicon.ico'},
}
ARTICLE_EXCLUDES = ['images', 'static']
