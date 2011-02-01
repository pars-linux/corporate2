#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "v4l-utils-%s" % get.srcVERSION()

def build():
    shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())
    autotools.make(' \
                    PREFIX=/usr \
                    LIBDIR=/usr/lib32 \
                    CFLAGS="%s -m32"' % get.CFLAGS().replace("-O2", "-O3"))

def install():
    autotools.rawInstall("PREFIX=/usr \
                          LIBDIR=/usr/lib32 \
                          DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/include")

    #pisitools.dodoc("ChangeLog", "COPYING*", "README*", "TODO")

