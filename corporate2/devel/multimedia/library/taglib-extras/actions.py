#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="taglib-extras-%s" % get.srcVERSION()

def setup():
    cmaketools.configure("-DWITH_KDE=1", sourceDir=".", installPrefix = "/%s/usr/kde/4" % get.installDIR())

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("PREFIX=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING.LGPL")
