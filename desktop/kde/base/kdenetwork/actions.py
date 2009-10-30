#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.export("DO_NOT_COMPILE", "ksirc wifi lanbrowsing")

    kde.make("-f Makefile.cvs")
    kde.configure("--with-slp \
                   --with-wifi \
                   --disable-sametime-plugin \
                   --without-xmms \
                   --without-arts \
                   --without-external-libgadu")

def build():
    kde.make()

def install():
    kde.install()

    pisitools.dodir("/etc")
    shelltools.touch("%s/etc/lisarc" % get.installDIR())

    # We replace this file
    pisitools.remove("/usr/kde/3.5/share/apps/konqueror/servicemenus/kget_download.desktop")
