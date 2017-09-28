PyRfid
======

PyRfid is a Python written library for an 125kHz RFID reader. It was developed with the RDM6300 RFID-sensor which uses the EM4100 protocol.

Installation
------------

Add PM Codeworks repository

* Debian 8:

    `~# echo "deb http://apt.pm-codeworks.de jessie main" | tee /etc/apt/sources.list.d/pm-codeworks.list`

* Debian 9:

    `~# echo "deb http://apt.pm-codeworks.de stretch main" | tee /etc/apt/sources.list.d/pm-codeworks.list`

Add PM Codeworks key

    ~# wget -qO - http://apt.pm-codeworks.de/pm-codeworks.de.gpg | apt-key add -
    ~# apt-get update

The library supports Python 2 and Python 3. There are one Debian package for each. It's up to you which version you install.

For Python 3 use:

    ~# apt-get install python3-rfid

For Python 2 use:

    ~# apt-get install python-rfid

Add group "dialout" for each user which should be able to use PyRfid

    ~# usermod -a -G dialout <username>
    ~# reboot

How to use the library
----------------------

Read a tag

    ~$ python /usr/share/doc/python-rfid/examples/example_read.py


Questions and suggestions
-------------------------

If you have any questions to this project just ask me via email:

<team@pm-codeworks.de>
