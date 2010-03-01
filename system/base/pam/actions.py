#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "Linux-PAM-%s" % get.srcVERSION()

def setup():
    shelltools.export("CFLAGS", "%s -fPIC -D_GNU_SOURCE" % get.CFLAGS())

    libtools.libtoolize("-f")
    autotools.autoreconf()
    autotools.rawConfigure("--disable-prelude \
                            --disable-dependency-tracking \
                            --enable-audit \
                            --enable-db=no \
                            --enable-nls \
                            --enable-securedir=/lib/security \
                            --enable-isadir=/lib/security")

def build():
    autotools.make()

def check():
    autotools.make("check")

    # dlopen check
    shelltools.system("./dlopen-test.sh")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/Linux-PAM/")
    pisitools.removeDir("/var")

    pisitools.doman("doc/man/*.[0-9]")
    pisitools.dodoc("CHANGELOG", "Copyright", "README")
