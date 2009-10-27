#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.aclocal("-I m4")
    autotools.automake()
    autotools.autoconf()

    autotools.libtoolize("--force")

    autotools.configure("--with-xml=libxml \
                         --localstatedir=/var \
                         --disable-doxygen-docs \
                         --disable-static \
                         --disable-xml-docs")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", "README")
