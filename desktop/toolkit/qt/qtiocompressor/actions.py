#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s-2.3_1-opensource" % get.srcNAME()
INCLUDE_DIR = "/usr/qt/4/include/QtSolutions"

def setup():
    shelltools.touch(".licenseAccepted")
    autotools.rawConfigure("-library")

def build():
    shelltools.system("qmake-qt4")
    autotools.make()

def install():
    pisitools.insinto(INCLUDE_DIR, "src/QtIOCompressor")
    pisitools.insinto(INCLUDE_DIR, "src/qtiocompressor.h")

    pisitools.insinto("/usr/qt/4/lib", "lib/*")

    pisitools.dodoc("LICENSE*", "README.TXT")
