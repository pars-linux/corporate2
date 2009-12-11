#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s%s" % (get.srcNAME(), get.srcVERSION())
NoStrip=["/usr/share/doc"]

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --libdir=/usr/lib \
                            --docdir=%s/usr/share/doc/%s/html \
                            --with-tiff \
                            --with-jpeg \
                            --with-png \
                            --with-zlib \
                            --with-fftw \
                            --enable-shared \
                            --disable-static" % (get.installDIR(), get.srcNAME()))
def build():
    autotools.make()

def install():
    autotools.rawInstall("libdir=\"%s/usr/lib\" prefix=\"%s/usr\"" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("*.txt")
