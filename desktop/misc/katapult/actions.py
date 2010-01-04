#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

shelltools.export("HOME", get.workDIR())

KeepSpecial = ["libtool"]

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    pisitools.remove("%s/lib/libkatapult.la" % get.kdeDIR())
