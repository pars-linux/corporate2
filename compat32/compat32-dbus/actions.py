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
shelltools.export("CXXFLAGS", "%s -m32" % get.CXXFLAGS())

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--with-xml=expat \
                         --with-system-pid-file=/var/run/dbus/pid \
                         --with-system-socket=/var/run/dbus/system_bus_socket \
                         --with-session-socket-dir=/tmp \
                         --with-dbus-user=dbus \
                         --libdir=/usr/lib32 \
                         --disable-libaudit \
                         --disable-selinux \
                         --disable-static \
                         --disable-tests \
                         --disable-asserts \
                         --disable-doxygen-docs \
                         --disable-xml-docs")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for _dir in ("/usr/include",):
        pisitools.removeDir(_dir)

