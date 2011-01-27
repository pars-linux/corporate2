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

WorkDir="util-linux-ng-%s" % get.srcVERSION().replace("_","-")

shelltools.export("CFLAGS", "%s -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 -m32" % get.CFLAGS())
shelltools.export("AUTOPOINT", "/bin/true")
shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

def setup():
    autotools.autoreconf("-fi")

    # Extra fedora switches:
    # --enable-login-utils will enable some utilities we ship in shadow
    # --enable-kill will enable the kill utility we ship in coreutils
    autotools.configure("--libdir=/usr/lib32 \
                         --disable-partx \
                         --disable-libblkid \
                         --disable-mount \
                         --disable-fsck \
                         --disable-libmount \
                         --disable-raw \
                         --disable-write \
                         --disable-login-utils \
                         --disable-use-tty-group \
                         --disable-makeinstall-chown \
                         --disable-rpath \
                         --disable-static \
                         --disable-wall \
                         --without-ncurses \
                         --without-audit")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for _dir in ("/usr/share", "/usr/include"):
        pisitools.removeDir(_dir)
