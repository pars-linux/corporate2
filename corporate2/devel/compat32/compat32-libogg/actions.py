#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())
shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")


def setup():
    pisitools.dosed("doc/Makefile.in", "^docdir = .*$", "docdir = $(datadir)/doc/$(PACKAGE)")
    pisitools.dosed("doc/libogg/Makefile.in", "^docdir = .*$", "docdir = $(datadir)/doc/$(PACKAGE)/ogg")
    autotools.configure("--disable-static \
                         --libdir=/usr/lib32")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for i in ["include", "share"]:
        pisitools.removeDir("/usr/%s" % i)
