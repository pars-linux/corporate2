#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "smile"

def setup():
    shelltools.system("qmake-qt4 smile.pro")

def build():
    autotools.make('CXX="%s" CXXFLAGS="%s"' % (get.CXX(), get.CXXFLAGS()))

def install():
    pisitools.dobin("smile")

    for data in ["BIB_ManSlide", "Interface", "*.qm"]:
        pisitools.insinto("/usr/share/smile", data)

    pisitools.dodoc("copying")
