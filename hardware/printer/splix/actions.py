#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())
    shelltools.export("OS_CFLAGS", get.CFLAGS())
    shelltools.export("OS_LDFLAGS", get.LDFLAGS())
    shelltools.export("OS_CXXFLAGS", get.CXXFLAGS())

    autotools.make()

def install():
    pisitools.dodir("/usr/lib/cups/filter")
    pisitools.dodir("/usr/share/cups/model")

    autotools.install("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "THANKS", "TODO")
