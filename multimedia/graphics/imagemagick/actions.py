#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "ImageMagick-%s-%s" % (get.srcVERSION()[:-2], get.srcVERSION()[-1])
KeepSpecial=["libtool"]

def setup():
    autotools.autoreconf("-vif")
    #libtools.libtoolize("--copy --force")
    #autotools.aclocal("-I m4")
    #autotools.autoconf()
    #autotools.automake()

    pisitools.dosed("configure", "DOCUMENTATION_RELATIVE_PATH=.*", "DOCUMENTATION_RELATIVE_PATH=%s/html" % get.srcNAME())
    autotools.configure("--with-gs-font-dir=/usr/share/fonts/default/ghostscript \
                         --enable-hdri \
                         --enable-shared \
                         --disable-static \
                         --with-modules \
                         --with-perl \
                         --with-perl-options='INSTALLDIRS=vendor' \
                         --with-x \
                         --with-threads \
                         --with-magick_plus_plus \
                         --with-gslib \
                         --with-wmf \
                         --with-lcms \
                         --with-rsvg \
                         --with-xml \
                         --with-djvu \
                         --with-bzlib \
                         --with-zlib \
                         --with-fpx \
                         --with-tiff \
                         --with-jp2 \
                         --with-jpeg \
                         --without-jbig \
                         --without-fpx \
                         --without-dps")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS.txt", "ChangeLog", "LICENSE", "NEWS.txt")
    pisitools.remove("/usr/lib/perl5/vendor_perl/%s/%s-linux-thread-multi/auto/Image/Magick/.packlist" % (get.curPERL(), get.ARCH()))
    pisitools.remove("/usr/lib/*.la")

