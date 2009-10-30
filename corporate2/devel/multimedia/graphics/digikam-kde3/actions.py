#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

WorkDir = "digikam"

def setup():
    kde.configure("--enable-shared")

def build():
    # it seems we hit a nasty compiler bug, workaround for a while
    pisitools.dosed("digikam/libs/greycstoration/Makefile", "-O2")

    kde.make()

def install():
    kde.install()

    # kdelibs already has this
    pisitools.remove("/usr/kde/3.5/share/mimelnk/image/x-raw.desktop")
