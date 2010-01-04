#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde

KeepSpecial = ["libtool"]

def setup():
    kde.make("-f admin/Makefile.common")
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    pisitools.removeDir("/usr/kde/3.5/share/autostart")
