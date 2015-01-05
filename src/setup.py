#!/usr/bin/env python

from distutils.core import setup

setup(
    name            = 'python-rfid',
    version         = '1.0',
    description     = 'Python written library for an 125kHz RFID reader',
    author          = 'Philipp Meisberger',
    author_email    = 'team@pm-codeworks.de',
    url             = 'http://www.pm-codeworks.de/pyrfid.html',
    license         = 'BSD 3 License',
    package_dir     = {'': 'files'},
    packages        = ['PyRfid'],
)
