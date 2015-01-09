#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyRfid v1.1

Example RFID read.

Copyright 2015 Philipp Meisberger (PM Code Works).
All rights reserved.
"""

from pyrfid.PyRfid import PyRfid

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
    print('[Exception] '+ str(e))
