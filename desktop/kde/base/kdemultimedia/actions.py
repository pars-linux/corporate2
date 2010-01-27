#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

KeepSpecial=["libtool"]
shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.export("DO_NOT_COMPILE", "mpeglib mpeglib_artsplug kaboodle noatun")
    autotools.make("-f Makefile.cvs")

    # Fix tunepimp detection
    autotools.autoconf()

    kde.configure("--with-extra-includes=/usr/include/speex \
                   --with-cdparanoia \
                   --with-akode \
                   --with-alsa \
                   --with-vorbis \
                   --with-lame \
                   --with-flac \
                   --with-xine \
                   --with-musicbrainz \
                   --without-arts")

def build():
    kde.make("-j1")

def install():
    kde.install()
