#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

KeepSpecial=["libtool"]
shelltools.export("HOME", get.workDIR())

def setup():
    # Fix automake and python detection
    pisitools.dosed("admin/cvs.sh", "automake\*1\.10\*", "automake*1.1[0-5]*")
    pisitools.dosed("admin/acinclude.m4.in", "KDE_CHECK_PYTHON_INTERN\(\"2.5", "KDE_CHECK_PYTHON_INTERN(\"%s" % get.curPYTHON().split("python")[1])
    kde.make("-f admin/Makefile.common")

    shelltools.export("DO_NOT_COMPILE", "mpeglib mpeglib_artsplug kaboodle noatun arts krec")    # krec doesn't compile without arts

    kde.configure("--with-extra-includes=/usr/include/speex \
                   --with-cdparanoia \
                   --with-akode \
                   --with-alsa \
                   --with-vorbis \
                   --with-lame \
                   --with-flac \
                   --with-xine \
                   --with-musicbrainz")

def build():
    kde.make("-j1")

def install():
    kde.install()

    # DO_NOT_COMPILE doesn't cover docs
    pisitools.removeDir("/usr/kde/3.5/share/doc/HTML/en/artsbuilder/")
    pisitools.removeDir("/usr/kde/3.5/share/doc/HTML/en/kaboodle/")
    pisitools.removeDir("/usr/kde/3.5/share/doc/HTML/en/krec/")
    pisitools.removeDir("/usr/kde/3.5/share/doc/HTML/en/noatun/")
