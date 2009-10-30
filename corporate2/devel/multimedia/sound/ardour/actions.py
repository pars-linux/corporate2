#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    # Required for scons to "see" intermediate install location
    pisitools.dodir(get.installDIR())

    # P.S: VST = 1 enables VST support which is only for personal use
    scons.make('%s DESTDIR="%s" \
                FPU_OPTIMIZATION=1 \
                FFT_ANALYSIS=1 \
                SYSLIBS=1 \
                SURFACES=1 \
                TRANZPORT=1 \
                NLS=1 \
                FREEDESKTOP=1 \
                AIBO=1 \
                FREESOUND=1 \
                WIIMOTE=1 \
                LIBLO=1 \
                CFLAGS="%s -ffast-math" \
                LDFLAGS="%s" \
                LV2=1 \
                AUSTATE=1 \
                ARCH="-DARCH_X86 -DBUILD_SSE_OPTIMIZATIONS -msse -mfpmath=sse -DUSE_XMMINTRIN" \
                PREFIX=/usr' % (get.makeJOBS(), get.installDIR(), get.CFLAGS(), get.LDFLAGS()))

def install():
    # Required for scons to "see" intermediate install location
    pisitools.dodir(get.installDIR())

    scons.install()

    for s in ("16", "22", "32", "48"):
        pisitools.dodir("/usr/share/icons/hicolor/%sx%s/apps" % (s, s))
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (s, s), "gtk2_ardour/icons/ardour_icon_%spx.png" % s, "ardour2.png")
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/mimetypes" % (s, s), "gtk2_ardour/icons/application-x-ardour_%spx.png" % s, "application-x-ardour2.png")

    pisitools.insinto("/usr/share/applications", "gtk2_ardour/ardour2.desktop.in", "ardour2.desktop")
    pisitools.insinto("/usr/share/mime/packages", "gtk2_ardour/ardour2.xml")

    pisitools.doman("ardour.1")
    #install translated man pages
    for man in shelltools.ls("ardour.1.*"):
        lang = man.split(".")[2]
        pisitools.dodir("/usr/share/man/%s/man1" % lang)
        pisitools.insinto("/usr/share/man/%s/man1" % lang, man)

