#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

KeepSpecial = ["libtool"]

shelltools.export("HOME", get.workDIR())

def setup():
    kde.configure("--enable-shared \
                   --without-included-sqlite3")

def build():
    # it seems we hit a nasty compiler bug, workaround for a while
    pisitools.dosed("digikam/libs/greycstoration/Makefile", "-O2")

    kde.make()

def install():
    kde.install()
