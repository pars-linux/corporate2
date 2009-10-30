#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

WorkDir = "kaffeine"

def setup():
    kde.configure()

def build():
    kde.make()

def install():

    # Fix for #7916
    pisitools.dosed("po/Makefile", "\$\(PACKAGE\)\.mo", "kaffeine.mo")

    kde.install()

    # kdelibs already have this
    pisitools.remove("/usr/kde/3.5/share/mimelnk/application/x-mplayer2.desktop")

    # This line can be removed when Turksat data is merged
    pisitools.remove("/usr/kde/3.5/share/apps/kaffeine/dvbdata.tar.gz")
