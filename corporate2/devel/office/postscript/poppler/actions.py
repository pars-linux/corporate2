#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --enable-xpdf-headers \
                         --disable-cairo-output \
                         --disable-poppler-qt \
                         --disable-poppler-qt4 \
                         --disable-poppler-glib \
                         --disable-zlib \
                         --enable-libjpeg \
                         --enable-libopenjpeg")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "AUTHORS", "ChangeLog", "NEWS", "README-XPDF", "TODO")
