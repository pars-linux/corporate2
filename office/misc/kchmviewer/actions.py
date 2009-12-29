#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

KeepSpecial=["libtool"]

def setup():
    kde.configure("--disable-static --with-kde")

def build():
    kde.make()

def install():
    kde.install()

    pisitools.remove("%s/lib/*.a" % get.kdeDIR())
