#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyRfid v1.0

Example RFID read.

Copyright 2014 Philipp Meisberger (PM Code Works).
All rights reserved.
"""

import PyRfid.PyRfid as PyRfid
import sys

rfid = PyRfid('/dev/ttyUSB0', 9600)

try:
    print 'Waiting for tag...\n'

    if ( rfid.readTag() != True ):
        raise Exception('User aborted!')

    print 'RAW:      '+ rfid.rawTag
    print 'Checksum: '+ rfid.tagChecksum +'\n'

    print 'Decimal-format:'
    print 'ID:       '+ rfid.tagId
    print 'Type:     '+ rfid.tagType +'\n'

    print 'Float-format:'
    print 'ID:       '+ rfid.tagIdFloat
    print 'Type:     '+ rfid.tagTypeFloat

except Exception as e:
    sys.stderr.write('[Exception] '+ e.message + '\n')
