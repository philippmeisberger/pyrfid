PyRfid
======

[![Documentation Status](https://readthedocs.org/projects/pyrfid/badge/?version=latest)](https://pyrfid.readthedocs.io/en/latest/?badge=latest)

PyRfid is a Python written library for an 125kHz RFID reader. It was developed with the RDM6300 RFID-sensor which uses the EM4100 protocol.

Installation
------------

There are two ways of installing PyRfid: Installation of the stable or latest version. The stable version is distributed through the PM Code Works APT repository and is fully tested but does not contain the latest changes.

### Installation of the stable version

Add PM Code Works repository

* Debian 9:

    `~# echo "deb http://apt.pm-codeworks.de stretch main" | tee /etc/apt/sources.list.d/pm-codeworks.list`

* Debian 10:

    `~# echo "deb http://apt.pm-codeworks.de buster main" | tee /etc/apt/sources.list.d/pm-codeworks.list`

Add PM Code Works signing key

    ~# wget -qO - http://apt.pm-codeworks.de/pm-codeworks.de.gpg | apt-key add -
    ~# apt-get update

The library supports Python 2 and Python 3. There are one Debian package for each. It's up to you which version you install.

For Python 3 use:

    ~# apt-get install python3-rfid

For Python 2 use:

    ~# apt-get install python-rfid

### Installation of the latest version

The latest version contains the latest changes that may not have been fully tested and should therefore not be used in production. It is recommended to install the stable version.

Install required packages for building

    ~# apt-get install git devscripts equivs

Clone this repository

    ~$ git clone https://github.com/philippmeisberger/pyrfid.git

Build the package

    ~$ cd ./pyrfid/src/
    ~$ sudo mk-build-deps -i debian/control
    ~$ dpkg-buildpackage -uc -us

The library supports Python 2 and Python 3. There are one Debian package for each. It's up to you which version you install.

For Python 3 use:

    ~# dpkg -i ../python3-rfid*.deb

For Python 2 use:

    ~# dpkg -i ../python-rfid*.deb

Install missing dependencies

    ~# apt-get install -f

Setup
-----

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
