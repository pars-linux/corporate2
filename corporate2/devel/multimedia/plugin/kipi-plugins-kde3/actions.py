#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

WorkDir = "kipi-plugins"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
    pisitools.domove("/usr/kde/3.5/share/man/man1/images2mpg.1", "/usr/share/man/man1", "images2mpg.1")
    pisitools.removeDir("/usr/kde/3.5/share/man/")

