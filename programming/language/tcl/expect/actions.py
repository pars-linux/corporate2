#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

majorVersion = tuple(get.srcVERSION().split(".")[:2])
libname = "libexpect.so.%s" % get.srcVERSION()

WorkDir = "expect-%s.%s" % majorVersion

def setup():
    pisitools.dosed("expect.man", "/usr/local/bin", "/usr/bin")
    pisitools.dosed("expectk.man", "/usr/local/bin", "/usr/bin")

    pisitools.dosed("Makefile.in", "^install: .*", "install: all install-binaries install-doc")
    pisitools.dosed("Makefile.in", "^(SCRIPTS_MANPAGES = .*)$", "_\\1")

    shelltools.export("CFLAGS","%s -D_BSD_SOURCE" % get.CFLAGS())
    autotools.configure("--with-tcl=/usr/lib \
                         --with-tclinclude=/usr/include/tcl-private/generic/ \
                         --without-x \
                         --enable-shared")

def build():
    autotools.make("SONAME=%s" % libname)

def install():
    autotools.rawInstall('INSTALL_ROOT="%s"' % get.installDIR())

    pisitools.rename("/usr/lib/libexpect%s.%s.so" % majorVersion, libname)

    pisitools.dosym(libname, "/usr/lib/libexpect.so.%s.%s" % majorVersion)
    pisitools.dosym(libname, "/usr/lib/libexpect.so.%s" % majorVersion[0])
    pisitools.dosym(libname, "/usr/lib/libexpect.so")

    # No static
    pisitools.remove("/usr/lib/libexpect*.a")
    pisitools.remove("/usr/lib/expect*/libexpect*.a")

    pisitools.dodoc("FAQ", "ChangeLog", "NEWS", "README", "HISTORY")
