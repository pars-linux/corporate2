#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr/kde/4/ -DWITH_ID3LIB=FALSE", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
