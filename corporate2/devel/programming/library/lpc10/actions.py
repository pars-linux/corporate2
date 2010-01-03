#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lpc10-%s/lpc55-C" % get.srcVERSION()

def build():
    autotools.make("-j1 LIBDIR=/usr/lib CC=%s" % get.CC())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.newdoc("README", "README.lpc55-C")
    pisitools.dodoc("../FAQ", "../README*")
