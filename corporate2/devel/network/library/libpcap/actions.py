#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-ipv6 \
                         --enable-bluetooth")

def build():
    autotools.make("all shared")

def install():
    # rawInstall borks somehow, don't know how to fix it
    autotools.make('DESTDIR="%s" install install-shared' % get.installDIR())

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dolib_so("libpcap.so.%s" % get.srcVERSION())
    pisitools.dosym("libpcap.so.1", "/usr/lib/libpcap.so")
    pisitools.dosym("libpcap.so.1.0.0", "/usr/lib/libpcap.so.1")

    pisitools.dodoc("CHANGES", "CREDITS", "README*", "VERSION", "TODO")
