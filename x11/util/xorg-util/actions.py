#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def setup():
    for package in shelltools.ls("."):
        if package in ["patches", "pisiBuildState"] or package.startswith("."):
            continue

        shelltools.cd(package)
        autotools.configure()
        shelltools.cd("../")

def build():
    for package in shelltools.ls("."):
        if package in ["patches", "pisiBuildState"] or package.startswith("."):
            continue

        shelltools.cd(package)
        autotools.make()
        shelltools.cd("../")

def install():
    for package in shelltools.ls("."):
        if package in ["patches", "pisiBuildState"] or package.startswith("."):
            continue

        shelltools.cd(package)
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")
