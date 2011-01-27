#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

def setup():
    shelltools.makedirs("m4")

    autotools.rawConfigure("--libdir=/usr/lib32 \
                            --includedir=/usr/include \
                            --prefix=/usr")

def build():
    autotools.make()

def check():
    autotools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib32/*.a")

    for _dir in ("/usr/share", "/usr/include"):
        pisitools.removeDir(_dir)
