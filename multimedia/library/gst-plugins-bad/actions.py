#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) TUBITAK / UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("NOCONFIGURE", "1")
    shelltools.system("./autogen.sh")

    """The following is a list of disabled plugins:
    celt -> (celtdec, celtenc) -> Not available in Pardus repos,
    qtwrapper, checks for QuickTime/Movies.h -> Not available in Pardus repos,
    divx -> divx4linux,
    dirac -> needs dirac-research package, http://dirac.sourceforge.net
    """

    autotools.configure("--disable-static \
                         --disable-gtk-doc \
                         --disable-gtk-doc \
                         --disable-rpath \
                         --with-package-name='Pardus gstreamer-plugins-bad package' \
                         --with-package-origin='http://www.pardus.org.tr/eng' \
                         --disable-experimental \
                         --disable-wininet \
                         --disable-wildmidi \
                         --disable-timidity \
                         --disable-quicktime \
                         --disable-ivorbis \
                         --disable-mythtv \
                         --disable-swfdec \
                         --disable-dirac \
                         --disable-divx \
                         --disable-spc \
                         --disable-celt \
                         --disable-acm \
                         --disable-nas \
                         --disable-assrender")

def build():
    autotools.make()

def check():
    autotools.make("-C tests/check check")

def install():
    autotools.install()

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "RELEASE", "REQUIREMENTS")
