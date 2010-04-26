#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("drivers.c", "RTCM2_PACKET;", "RTCM2_PACKET,")
    pisitools.dosed("gpsd.rules", "SYSFS", "ATTRS")
    shelltools.touch("%s/ChangeLog" % get.curDIR())

    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --enable-dbus")


def build():
    autotools.make("-j1")

def install():
    autotools.install()

    # Install UDEV rule
    pisitools.insinto("/lib/udev/rules.d", "gpsd.rules", "99-gpsd.rules")
    pisitools.dobin("gpsd.hotplug", "/lib/udev")

    # Fix *.so permissions
    shelltools.chmod("%s/usr/lib/%s/site-packages/gpspacket.so" % (get.installDIR(), get.curPYTHON()))
    shelltools.chmod("%s/usr/lib/%s/site-packages/gps.py" % (get.installDIR(), get.curPYTHON()))

    pisitools.dodoc("README", "TODO", "AUTHORS", "COPYING")
