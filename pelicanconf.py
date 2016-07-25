#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Config options for debugging only
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)

# Standard Configuration
from commonconf import *

RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
