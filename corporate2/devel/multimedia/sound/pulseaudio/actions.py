#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Disable as-needed for now as it doesn't compile
    # Lennart has introduced a circular dep in the libraries. libpulse requires
    # libpulsecommon but libpulsecommon requires libpulse.
    shelltools.export("LDFLAGS", "%s -Wl,--no-as-needed" % get.LDFLAGS())

    # Needs autoconf >= 2.6.3
    # Avoid building and linking test programs outside of make check
    pisitools.dosed("src/Makefile.am", "noinst_PROGRAMS", "check_PROGRAMS")

    autotools.autoreconf("-fi")
    libtools.libtoolize()


    # Disable asyncns for now: thread cancellation issues
    autotools.configure("--enable-largefile \
                         --enable-glib2 \
                         --enable-gconf \
                         --enable-oss \
                         --enable-alsa \
                         --enable-avahi \
                         --enable-bluez \
                         --enable-hal \
                         --enable-tcpwrap \
                         --enable-jack \
                         --enable-lirc \
                         --disable-asyncns \
                         --disable-solaris \
                         --disable-static \
                         --disable-rpath \
                         --with-caps \
                         --localstatedir=/var \
                         --with-system-user=pulse \
                         --with-system-group=pulse \
                         --with-realtime-group=pulse-rt \
                         --with-access-group=pulse-access")

def build():
    autotools.make("LIBTOOL=/usr/bin/libtool")

    #generate html docs
    autotools.make("doxygen")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "LICENSE", "GPL", "LGPL", "todo", "ChangeLog")
    pisitools.dohtml("doxygen/html/*")

    # Needed for service.py
    pisitools.dodir("/var/run/pulse")
