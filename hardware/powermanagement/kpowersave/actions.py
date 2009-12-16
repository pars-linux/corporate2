#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

WorkDir = "kpowersave"
KeepSpecial = ["libtool"]

def setup():
    kde.make("-f admin/Makefile.common")
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    # Create correct symlinks
    for lang in ["cs", "de", "fi", "hu", "nb"]:
        pisitools.remove("/usr/kde/3.5/share/doc/HTML/%s/kpowersave/common" % lang)
        pisitools.dosym("/usr/kde/3.5/share/doc/HTML/en/kpowersave/common",
                        "/usr/kde/3.5/share/doc/HTML/%s/kpowersave/common" % lang)
