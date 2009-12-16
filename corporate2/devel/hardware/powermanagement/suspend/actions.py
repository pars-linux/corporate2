#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "suspend-0.8.20081103"

def setup():
    autotools.configure("--enable-static \
                         --enable-compress \
                         --disable-encrypt \
                         --with-initramfsdir=/usr/sbin")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # will be created by postInstall script
    pisitools.remove("/etc/suspend.conf")

    shelltools.touch("%s/etc/suspend.key" % get.installDIR())
