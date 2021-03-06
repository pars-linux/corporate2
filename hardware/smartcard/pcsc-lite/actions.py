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
    autotools.autoreconf("-fi")
    autotools.configure("--enable-usbdropdir=/usr/lib/pcsc/drivers \
                         --disable-dependency-tracking \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/lib/pcsc/drivers")
    pisitools.dodir("/etc/reader.conf.d")


    pisitools.dodoc("AUTHORS", "ChangeLog", "DRIVERS", "HELP", "NEWS",
                    "README", "SECURITY", "doc/README.DAEMON")
