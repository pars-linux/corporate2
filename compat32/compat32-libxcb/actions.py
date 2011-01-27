#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -m32 -DNDEBUG" % get.CFLAGS())
shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

# For xcb-proto which is not arch dependent
shelltools.export("PKG_CONFIG_PATH", "/usr/lib/pkgconfig")

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --disable-xevie \
                         --disable-xprint \
                         --disable-build-docs \
                         --libdir=/usr/lib32")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "NEWS", "README")

    pisitools.removeDir("/usr/include")
    pisitools.removeDir("/usr/share/doc/libxcb")
