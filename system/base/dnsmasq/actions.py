#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/config.h", "/\* #define HAVE_DBUS \*/", "#define HAVE_DBUS")
    pisitools.dosed("Makefile", "AWK = nawk", "AWK = /bin/awk")

def build():
    autotools.make()

def install():
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())
    pisitools.insinto("/etc/dbus-1/system.d", "dbus/dnsmasq.conf", "dnsmasq.conf")
    pisitools.dodoc("CHANGELOG", "COPYING", "COPYING-v3", "FAQ")
    pisitools.dohtml("doc.html", "setup.html")
