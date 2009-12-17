#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

KeepSpecial=["libtool"]
shelltools.export('HOME', get.workDIR())

def setup():
    kde.make("-f admin/Makefile.common")
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    pisitools.remove("/usr/kde/3.5/lib/kde3/*.a")
