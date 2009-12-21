#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-grapher \
                         --enable-sqlite \
                         --enable-pie \
                         --disable-server \
                         --disable-crash \
                         --disable-docs \
                         --without-rpm")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/cache/systemtap")
    pisitools.dodir("/var/run/systemtap")

    # Clean uprobes directory
    autotools.make("-C %s/usr/share/systemtap/runtime/uprobes clean" % get.installDIR())
