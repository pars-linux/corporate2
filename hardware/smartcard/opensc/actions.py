#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile.am", "win32 ", "")
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --disable-assert \
                         --enable-pcsc \
                         --with-pcsc-provider=libpcsclite.so.1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/sbin")

    pisitools.insinto("/etc", "etc/opensc.conf")

    pisitools.dodoc("README")
