#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("CC", "%s -m32" % get.CC())
shelltools.export("CXX", "%s -m32" % get.CXX())

shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

#libs = "libpulsecommon-%s.la libpulse.la libpulse-simple.la libpulse-mainloop-glib.la libpulsedsp.la" % get.srcVERSION()
libs = "libpulsecommon-%s.la libpulse.la libpulse-simple.la libpulse-mainloop-glib.la" % get.srcVERSION()

def setup():
    # Disable as-needed for now as it doesn't compile
    # Lennart has introduced a circular dep in the libraries. libpulse requires
    # libpulsecommon but libpulsecommon requires libpulse.
    shelltools.export("LDFLAGS", "%s -Wl,--no-as-needed" % get.LDFLAGS())

    autotools.configure("--disable-dependency-tracking \
                         --libdir=/usr/lib32 \
                         --libexecdir=/usr/lib32 \
                         --disable-static \
                         --disable-rpath \
                         --disable-hal \
                         --disable-gconf \
                         --disable-gtk2 \
                         --disable-jack \
                         --disable-bluez \
                         --disable-asyncns \
                         --disable-lirc \
                         --disable-x11 \
                         --disable-oss-output \
                         --disable-oss-wrapper \
                         --disable-solaris \
                         --disable-manpages \
                         --disable-samplerate \
                         --disable-default-build-tests")


def build():
    autotools.make("-C src %s" % libs)

def install():
    autotools.rawInstall("-C src lib_LTLIBRARIES=\"%s\" DESTDIR=%s" % (libs, get.installDIR()), "install-libLTLIBRARIES")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-pkgconfigDATA")
