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

WorkDir = "glib-%s" % get.srcVERSION()

shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

def setup():
    autotools.autoconf()
    autotools.configure("--libdir=/usr/lib32 \
                         --disable-gtk-doc \
                         --with-pcre=system \
                         --disable-fam \
                         --disable-systemtap \
                         --disable-static")

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    for _dir in ("/usr/share", "/usr/include", "/etc", "/usr/bin"):
        pisitools.removeDir(_dir)
