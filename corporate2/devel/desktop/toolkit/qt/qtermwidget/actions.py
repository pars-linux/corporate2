#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "qtermwidget"

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make("-j1")

def install():
    # Binaries
    pisitools.dobin("consoleq", "/usr/bin")
    pisitools.dobin("consoleq_d", "/usr/bin")

    # Libs
    pisitools.dolib("libqtermwidget*", "/usr/lib")

    # Headers
    pisitools.dodir("/usr/include/qtermwidget")
    pisitools.insinto("/usr/include/qtermwidget", "lib/*.h")

    # Docs
    pisitools.dodoc("AUTHORS", "README", "COPYING")

