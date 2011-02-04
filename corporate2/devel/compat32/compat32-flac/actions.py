#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
shelltools.export("CXXFLAGS", "%s -m32" % get.CXXFLAGS())
shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())
shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

def setup():
    autotools.autoconf()

    autotools.configure("--with-pic \
                         --libdir=/usr/lib32 \
                         --enable-ogg \
                         --enable-sse \
                         --disable-doxygen-docs \
                         --disable-dependency-tracking \
                         --disable-xmms-plugin \
                         --disable-static")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for i in ["share", "include", "bin"]:
        pisitools.removeDir("/usr/%s" % i)

