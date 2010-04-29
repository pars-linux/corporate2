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

KeepSpecial=["libtool"]
shelltools.export("HOME", get.workDIR())

def setup():
    # Fix automake and python detection
    pisitools.dosed("admin/cvs.sh", "automake\*1\.10\*", "automake*1.1[0-5]*")
    pisitools.dosed("admin/acinclude.m4.in", "KDE_CHECK_PYTHON_INTERN\(\"2.5", "KDE_CHECK_PYTHON_INTERN(\"%s" % get.curPYTHON().split("python")[1])
    kde.make("-f admin/Makefile.common")

    shelltools.export("DO_NOT_COMPILE", "ksirc wifi lanbrowsing")
    kde.configure("--with-slp \
                   --with-wifi \
                   --disable-sametime-plugin \
                   --without-xmms \
                   --without-external-libgadu")

def build():
    kde.make()

def install():
    kde.install()

    pisitools.dodir("/etc")
    shelltools.touch("%s/etc/lisarc" % get.installDIR())

    # We replace this file
    pisitools.remove("/usr/kde/3.5/share/apps/konqueror/servicemenus/kget_download.desktop")

    pisitools.insinto("/etc/ppp/peers", "kppp_peers", "kppp")
