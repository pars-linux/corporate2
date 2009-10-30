#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -Wno-pointer-sign %s" % (get.CFLAGS(), get.LDFLAGS()))

    autotools.autoreconf("-fi")
    autotools.configure("--with-x \
                         --enable-xfree-ext \
                         --enable-xvideo \
                         --enable-dv \
                         --enable-mmx \
                         --disable-motif \
                         --enable-quicktime \
                         --enable-alsa \
                         --enable-lirc \
                         --enable-gl \
                         --enable-zvbi \
                         --prefix=/usr \
                         --enable-aa")

def build():
    autotools.make("-j1")

def install():
    autotools.install("libdir=%(D)s/usr/lib/xawtv \
                       resdir=%(D)s/etc/X11" % {"D": get.installDIR()})

    pisitools.dobin("x11/v4lctl")
    pisitools.dodoc("COPYING", "Changes", "README*", "TODO")

    pisitools.removeDir("/usr/share/man/fr")
    pisitools.removeDir("/usr/share/man/es")

    pisitools.dodir("/usr/share/xawtv")
    pisitools.domove("/usr/share/*.list", "/usr/share/xawtv/")
    pisitools.domove("/usr/share/Index*", "/usr/share/xawtv/")

    shelltools.chmod("contrib/xawtv48x48.xpm", 0644)
    pisitools.insinto("/usr/share/pixmaps", "contrib/xawtv48x48.xpm", "xawtv.xpm")
