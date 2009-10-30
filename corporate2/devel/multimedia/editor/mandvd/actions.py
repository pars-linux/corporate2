#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("qmake mandvd.pro")

def build():
    autotools.make()

def install():
    pisitools.dobin("mandvd")
    pisitools.insinto("/usr/share/pixmaps", "mandvdico.png", "mandvd.png")

    pisitools.dodoc("COPYING")
