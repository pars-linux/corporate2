#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

WorkDir = "ImageMagick-%s-%s" % (get.srcVERSION()[:-3], get.srcVERSION()[-2:])
KeepSpecial=["libtool"]

def setup():
    autotools.autoreconf("-vif")
    pisitools.dosed("configure","DOCUMENTATION_RELATIVE_PATH=.*","DOCUMENTATION_RELATIVE_PATH=%s/html" % get.srcNAME())
    autotools.configure("--with-gs-font-dir=/usr/share/fonts/default/ghostscript \
                         --enable-hdri \
                         --enable-shared \
                         --disable-static \
                         --with-threads \
                         --with-djvu \
                         --with-bzlib \
                         --with-modules \
                         --with-zlib \
                         --with-x \
                         --with-rsvg \
                         --with-wmf \
                         --with-dps \
                         --with-fpx \
                         --with-perl \
                         --without-jbig \
                         --with-tiff \
                         --with-lcms \
                         --with-xml \
                         --with-jp2 \
                         --with-jpeg \
                         --with-gslib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS.txt", "ChangeLog", "LICENSE", "NEWS.txt")
