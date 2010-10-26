#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "SDL_gfx-%s" % get.srcVERSION()
mmx = "--enable-mmx" if get.ARCH() == "i686" else "--disable-mmx"

def setup():
    pisitools.dosed("configure.in", "-O")
    shelltools.unlink("acinclude.m4")

    autotools.autoreconf("-fi")
    autotools.configure("--disable-dependency-tracking \
                         %s \
                         --disable-static" % mmx)

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "LICENSE", "README")
    pisitools.insinto("/%s/sdl-gfx/" % get.docDIR(), "Docs", "html")
