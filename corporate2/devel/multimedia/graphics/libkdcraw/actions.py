#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

KeepSpecial = ["libtool"]

def setup():
    kde.configure("--enable-openmp")

def build():
    kde.make()

def install():
    kde.install()

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README")
