#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-qt=/usr/qt/4")

def build():
    autotools.make("CXX=%s CXXFLAGS='%s'" % (get.CXX(), get.CXXFLAGS()))

def install():
    autotools.install("-j1")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO", "TRANSLATORS")
