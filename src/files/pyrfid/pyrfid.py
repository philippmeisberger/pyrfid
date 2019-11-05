#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyRfid
Copyright (C) 2015 Philipp Meisberger <team@pm-codeworks.de>
All rights reserved.

"""

import serial
import os
import struct

class PyRfid(object):
    """
    Manages 125kHz RFID readers.
    """

    RFID_STARTCODE = 0x02
    RFID_ENDCODE = 0x03
    __serial = None
    __rawTag = None

    def __init__(self, port = '/dev/ttyUSB0', baudRate = 9600):
        """
        Constructor for creating a PyRfid instance.

        Arguments:
            port (str): The port to use
            baudRate (int): The baud-rate to use. Must be a multiple of 9600!

        """

        ## Validates port
        if ( os.path.exists(port) == False ):
            raise Exception('The RFID sensor port "' + port + '" was not found!')

        ## Initializes connection
        self.__serial = serial.Serial(port = port, baudrate = baudRate, bytesize = serial.EIGHTBITS, timeout = 1)

    def __del__(self):
        """
        Destructor

        """

        ## Closes connection if established
        if ( ( self.__serial != None ) and ( self.__serial.isOpen() == True ) ):
            self.__serial.close()

    def __read(self):
        """
        Reads the complete tag and returns the status.

        Returns:
            True if successful or False otherwise.
        """

        self.__rawTag = None
        rawTag = ''
        calculatedChecksum = 0
        receivedPacketData = []
        index = 0

        while ( True ):

            ## Reads on byte
            receivedFragment = self.__serial.read()

            ## Collects RFID data
            if ( len(receivedFragment) != 0 ):

                ## Start and stop bytes are string encoded and must be byte encoded
                if ( ( index == 0 ) or ( index == 13 ) ):
                    receivedFragment = struct.unpack('@B', receivedFragment)[0]
                else:
                    rawTag += str(struct.unpack('@B', receivedFragment)[0])
                    receivedFragment = int(receivedFragment, 16)

                ## Collects RFID data (hexadecimal)
                receivedPacketData.append(receivedFragment)
                index += 1

            ## Packet completly received
            if ( index == 14 ):

                ## Checks for invalid packet data
                if ( ( receivedPacketData[0] != self.RFID_STARTCODE ) or ( receivedPacketData[13] != self.RFID_ENDCODE ) ):
                    raise Exception('Invalid start or stop bytes!')

                ## Calculates packet checksum
                for i in range(1, 11, 2):
                    byte = receivedPacketData[i] << 4
                    byte = byte | receivedPacketData[i+1]
                    calculatedChecksum = calculatedChecksum ^ byte

                ## Gets received packet checksum
                receivedChecksum = receivedPacketData[11] << 4
                receivedChecksum = receivedChecksum | receivedPacketData[12]

                ## Checks for wrong checksum
                if ( calculatedChecksum != receivedChecksum ):
                    raise Exception('Calculated checksum is wrong!')

                ## Sets complete tag for other methods
                self.__rawTag = rawTag

                return True

        return False

    def readTag(self):
        """
        Reads the complete tag.

        Returns:
            True if successful or False otherwise.
        """

        try:
            while ( self.__read() != True ):
                pass

        except KeyboardInterrupt:
            return False

        return True

    @property
    def rawTag(self):
        """
        Gets the raw tag in hex format "1A2B345C67" without checksum.

        Returns:
            The raw tag (10 bytes)
        """

        return self.__rawTag[0:10]

    @property
    def tagType(self):
        """
        Gets the type of read tag in hex format (first 4 bytes).

        Returns:
            The tag type
        """

        if ( self.__rawTag != None ):
            return hex(int(self.__rawTag[0:4], 16))

        return None

    @property
    def tagTypeFloat(self):
        """
        Gets the float type of read tag in hex format (first 2 bytes).

        Returns:
            The tag type
        """

        if ( self.__rawTag != None ):
            return hex(int(self.__rawTag[0:2], 16))

        return None

    @property
    def tagId(self):
        """
        Gets the tag ID in decimal format, e.g. "0001234567".

        Returns:
            The ID
        """

        if ( self.__rawTag != None ):

            ## Length of ID is 10 anyway
            return '%010i' % int(self.__rawTag[4:10], 16)

        return None

    @property
    def tagIdFloat(self):
        """
        Gets the tag ID in float format, e.g. "123,45678".

        Returns:
            The ID
        """

        if ( self.__rawTag != None ):
            pre = float.fromhex(self.__rawTag[2:6])
            post = float.fromhex(self.__rawTag[6:10]) / 100000
            tag = pre + post
            return str(tag)

        return None

    @property
    def tagChecksum(self):
        """
        Gets the checksum of read tag (last 2 bytes).

        Returns:
            The checksum
        """

        if ( self.__rawTag != None ):
            return hex(int(self.__rawTag[10:12], 16))

        return None
