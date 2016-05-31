PyRfid
======

PyRfid is a Python written library for an 125kHz RFID reader. It was developed with the RDM6300 RFID-sensor which uses the EM4100 protocol.

Installation
------------

Add PM Codeworks repository

    ~# wget http://apt.pm-codeworks.de/pm-codeworks.list -P /etc/apt/sources.d/

Add PM Codeworks key

    ~# wget -O - http://apt.pm-codeworks.de/pm-codeworks.de.gpg.key | apt-key add -
    ~# apt-get update

Install the packages

    ~# apt-get install python-rfid

Add group "dialout" for each user which should be able to use PyRfid

    ~# usermod -a -G dialout <username>
    ~# reboot

How to use the library
----------------------

Read a tag

    ~$ python2 /usr/share/doc/python-rfid/examples/example_read.py


Questions and suggestions
-------------------------

If you have any questions to this project just ask me via email:

<team@pm-codeworks.de>