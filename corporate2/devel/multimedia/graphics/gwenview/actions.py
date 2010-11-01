#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())
KeepSpecial=["libtool"]

def setup():
    kde.make("-f admin/Makefile.common")

    kde.configure("--without-arts \
                   --with-kipi")

def build():
    kde.make()

def install():
    kde.install()

    # Remove gwenview.desktop, we have a custom one
    pisitools.remove("/usr/kde/3.5/share/applications/kde/gwenview.desktop")
