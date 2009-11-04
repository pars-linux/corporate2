#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "gtk+-%s" % get.srcVERSION()

def setup():
    files = ["gtkmarshalers.c", "gtkmarshalers.h"]
    for f in files:
        shelltools.unlink("gtk/%s" % f)

    autotools.configure("--with-libjpeg \
                         --with-libtiff \
                         --with-libjasper\
                         --with-libpng \
                         --with-gdktarget=x11 \
                         --enable-xinerama \
                         --enable-xkb \
                         --enable-shm")
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "README*", "HACKING", "ChangeLog*", "NEWS*")
