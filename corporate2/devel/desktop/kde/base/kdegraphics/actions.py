#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

KeepSpecial=["libtool"]
shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.export("DO_NOT_COMPILE", "kpovmodeler kmrml kview ksvg")
    kde.configure("--with-poppler \
                   --with-kamera \
                   --without-arts")

def build():
    kde.make()

def install():
    kde.install()
