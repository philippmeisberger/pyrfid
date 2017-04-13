#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name            = 'pyrfid',
    version         = '1.2',
    description     = 'Python written library for an 125kHz RFID reader',
    author          = 'Philipp Meisberger',
    author_email    = 'team@pm-codeworks.de',
    url             = 'http://www.pm-codeworks.de/pyrfid.html',
    license         = 'D-FSL',
    package_dir     = {'': 'files'},
    packages        = ['pyrfid'],
)
