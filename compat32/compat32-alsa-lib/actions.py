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

WorkDir = "alsa-lib"

shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-aload \
                         --disable-python \
                         --libdir=/usr/lib32")

    # rpath fix
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for _dir in ("/usr/bin", "/usr/include", "/usr/share"):
        pisitools.removeDir(_dir)

    pisitools.dodoc("COPYING")
