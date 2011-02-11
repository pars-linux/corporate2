#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="minitube"

def setup():
    shelltools.system("qmake-qt4 PREFIX=/usr")

def build():
    autotools.make()

def install():
    pisitools.dobin("build/target/minitube")

    pisitools.insinto("/usr/share/applications", "minitube.desktop")
    pisitools.insinto("/usr/share/pixmaps", "images/app.png", "minitube.png")

    pisitools.insinto("/usr/share/minitube/locale", "build/target/locale/*.qm")

    pisitools.dodoc("AUTHORS", "CHANGES", "COPYING", "TODO")
