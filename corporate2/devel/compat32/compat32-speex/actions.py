#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="speex-%s" % get.srcVERSION().replace("_","")

shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

def setup():
    shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64" % get.CFLAGS())

    pisitools.dosed("libspeex/Makefile.am", "noinst_PROGRAMS", "check_PROGRAMS")

    autotools.autoreconf("-fi")
    autotools.configure("--enable-ogg \
                         --enable-sse \
                         --libdir=/usr/lib32 \
                         --disable-static")

    # Remove rpath from speexenc and speexdec
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s docdir=/usr/share/doc/speex" % get.installDIR())

    for _dir in ("/usr/bin", "/usr/include", "/usr/share"):
        pisitools.removeDir(_dir)
