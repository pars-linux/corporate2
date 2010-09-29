#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = get.srcNAME()

def setup():
    autotools.rawConfigure("-prefix /usr \
                            -libdir /usr/qt/4/lib \
                            -headerdir /usr/qt/4/include \
                            -qmake-bin /usr/qt/4/bin/qmake")

def build():
    autotools.make()

def install():
    autotools.install("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.removeDir("/usr/doc")
