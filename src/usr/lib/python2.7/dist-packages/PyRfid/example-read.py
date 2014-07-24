#!/usr/bin/env python

"""
PyRfid v1.0

Example RFID read.

Copyright 2014 Philipp Meisberger (PM Code Works).
All rights reserved. 
"""

from PyRfid import *
import sys
   
rfid = PyRfid('/dev/ttyUSB0', 9600)

try:
    print 'Waiting for tag...\n'

    if ( rfid.readTag() != True ):
        raise Exception('User aborted!')

    print 'RAW:      '+ rfid.rawTag
    print 'Checksum: '+ rfid.tagChecksum +'\n'

    print 'Hexadecimal-format:'
    print 'ID:       '+ rfid.tagId
    print 'Type:     '+ rfid.tagType +'\n'

    print 'Float-format:'
    print 'ID:       '+ rfid.tagIdFloat
    print 'Type:     '+ rfid.tagTypeFloat

except Exception as e:
    sys.err.write('[Exception] '+ e.message)
