"""
PyFingerprint

@author Bastian Raschke <bastian.raschke@posteo.de>
@copyright Bastian Raschke
@license LGPL (GNU Lesser General Public License)
@link https://sicherheitskritisch.de
"""

import struct


def rightShift(n, x):
    """
    Shifts a byte.

    @param integer n
    @param integer x
    @return integer
    """

    return (n >> x & 0xFF)

def leftShift(n, x):
    """
    Shifts a byte.

    @param integer n
    @param integer x
    @return integer
    """

    return (n << x)

def bitAtPosition(n, p):
    """
    Gets the bit of n at position p.

    @param integer n
    @param integer p
    @return integer
    """

    ## A bitshift 2 ^ p
    twoP = 1 << p

    ## Binary AND composition (on both positions must be a 1)
    ## This can only happen at position p
    result = n & twoP
    return int(result > 0)

def byteToString(byte):
    """
    Converts a byte to string.

    @param byte byte
    @return string
    """

    return struct.pack('@B', byte)

def stringToByte(string):
    """
    Converts one "string" byte (like '0xFF') to real integer byte (0xFF).

    @param string string
    @return byte
    """

    return struct.unpack('@B', string)[0]
