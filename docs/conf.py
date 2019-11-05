#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import sys
sys.path.insert(0, '../src/files/')

import pyrfid

project = u'PyRfid'
master_doc = 'index'
author = 'Philipp Meisberger <team@pm-codeworks.de>'
copyright = '2015-{}, {}'.format(datetime.date.today().year, author)
version = pyrfid.__version__
release = version
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store'
]
extensions = [
    'sphinx.ext.autodoc',
]
autoclass_content = "both"
