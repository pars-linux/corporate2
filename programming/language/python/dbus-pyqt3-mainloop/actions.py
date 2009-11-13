#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = 'dbus-pyqt3-mainloop'

def setup():
    cmaketools.configure("-DPYTHONVER=%s" % get.curPYTHON())

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    exampledir = "/usr/share/doc/%s/examples" % get.srcTAG()
    pisitools.dodir(exampledir)
    pisitools.insinto(exampledir, "examples/*")
    pisitools.dodoc("COPYING", "Authors", "README")
