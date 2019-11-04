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
    long_description= 'PyRfid is a Python written library for an 125kHz RFID reader. It was developed with the RDM6300 RFID-sensor which uses the EM4100 protocol. See the example-read.py for an example of how to use this library.',
    author          = 'Philipp Meisberger',
    author_email    = 'team@pm-codeworks.de',
    url             = 'https://github.com/philippmeisberger/pyrfid',
    license         = 'D-FSL',
    package_dir     = {'': 'files'},
    packages        = ['pyrfid'],
    install_requires = ['pyserial'],
    classifiers     = [
        'Development Status :: 5 - Production/Stable'
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Terminals :: Serial',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
