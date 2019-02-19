#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import sys
sys.path.insert(0, './files/')

import pyrfid

setup(
    name            = 'pyrfid',
    version         = pyrfid.__version__,
    description     = 'Python written library for an 125kHz RFID reader',
    author          = 'Philipp Meisberger',
    author_email    = 'team@pm-codeworks.de',
    url             = 'http://www.pm-codeworks.de/pyrfid.html',
    license         = 'D-FSL',
    package_dir     = {'': 'files'},
    packages        = ['pyrfid'],
)
