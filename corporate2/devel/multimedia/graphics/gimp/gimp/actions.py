#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--without-webkit \
                         --disable-gtk-doc \
                         --disable-default-binary \
                         --disable-altivec \
                         --enable-python \
                         --enable-mmx \
                         --enable-sse \
                         --enable-gimp-remote \
                         --with-libjpeg \
                         --with-libexif \
                         --with-librsvg \
                         --with-lcms \
                         --with-poppler \
                         --with-x \
                         --with-aa")

    # Add illustrator and other mime types
    pisitools.dosed("desktop/gimp.desktop.in", "^MimeType=application/postscript;application/pdf;(.*)$",
                    "MimeType=\\1;image/x-sun-raster;image/x-gray;image/x-pcx;image/jpg;image/x-bmp;image/pjpeg;image/x-png;application/illustrator;")


def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("gimp-remote-2.6", "/usr/bin/gimp-remote")
    pisitools.dosym("gimp-console-2.6", "/usr/bin/gimp-console")
    pisitools.dosym("gimp-2.6", "/usr/bin/gimp")

    pythonmodules.fixCompiledPy("/usr/lib/gimp/2.0/")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "HACKING", "NEWS", "README", "INSTALL", "LICENSE")

    pisitools.dodir("/usr/share/doc/gimp-i18n")
    pisitools.insinto("/usr/share/doc/gimp-i18n", "README.i18n")

