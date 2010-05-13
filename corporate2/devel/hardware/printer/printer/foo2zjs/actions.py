#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # Fix udev rule
    pisitools.dosed("hplj10xx.rules", "/etc/hotplug/usb", "/lib/udev")

    # Remove these. They are supported well by Splix.
    shelltools.unlink("foomatic-db/printer/Xerox-Phaser_6110.xml")
    shelltools.unlink("PPD/Xerox-Phaser_6110.ppd")

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/share/foomatic/db/source")
    pisitools.dodir("/usr/share/cups/model/foo2zjs")

    autotools.install("DESTDIR=%s install-udev" % get.installDIR())
