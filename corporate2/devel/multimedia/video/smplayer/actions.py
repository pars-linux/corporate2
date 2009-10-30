#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def build():
    autotools.make("QMAKE=qmake-qt4 LRELEASE=lrelease-qt4 PREFIX=/usr")

def install():
    autotools.rawInstall("QMAKE=qmake-qt4 LRELEASE=lrelease-qt4 PREFIX=/usr DESTDIR=%s DOC_PATH=/usr/share/doc/%s" % (get.installDIR(),get.srcNAME()))
