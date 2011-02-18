#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

def setup():
    pisitools.dosed("Make.Rules", "pardusCFLAGS", get.CFLAGS())
    pisitools.dosed("Make.Rules", "pardusLDFLAGS", get.LDFLAGS())

def build():
    autotools.make('CC="%s"' % get.CC())

def install():
    autotools.rawInstall("FAKEROOT=%s LIBDIR=%s/usr/lib32" % ((get.installDIR(),)*2))

    pisitools.remove("/usr/lib32/*.a")

    for _dir in ("/sbin", "/usr/include", "/usr/share"):
        pisitools.removeDir(_dir)

