#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="poppler-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --enable-cairo-output \
                         --enable-xpdf-headers \
                         --enable-libjpeg \
                         --enable-zlib \
                         --enable-poppler-glib \
                         --enable-poppler-qt4")

def build():
    shelltools.cd("poppler")

    # to compile qt4 binding
    autotools.make("libpoppler-arthur.la")

    # to compile glib binding with cairo support
    autotools.make("libpoppler-cairo.la")

    shelltools.cd("..")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gtk-doc")
