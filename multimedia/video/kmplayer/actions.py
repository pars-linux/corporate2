#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

KeepSpecial = ["libtool"]

def setup():
    kde.make("-f admin/Makefile.common")
    kde.configure("--with-xine \
                   --with-gstreamer")

def build():
    kde.make()

def install():
    kde.install()

    pisitools.remove("%s/share/mimelnk/application/x-mplayer2.desktop" % get.kdeDIR())
