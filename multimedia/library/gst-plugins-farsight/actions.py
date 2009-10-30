#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) TUBITAK / UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-jrtplib \
                         --disable-gconf \
                         --enable-mimic \
                         --enable-gsm \
                         --enable-jasper \
                         --enable-jingle-p2p \
                         --with-libj2k")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "README")
