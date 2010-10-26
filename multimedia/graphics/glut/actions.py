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

flags = "%s -Wall -O3 -g -fPIC -D_POSIX_SOURCE -D_POSIX_C_SOURCE=199309L -D_SVID_SOURCE -D_BSD_SOURCE -DPTHREADS -DUSE_XSHM -DUSE_X86_ASM -DUSE_MMX_ASM -DUSE_3DNOW_ASM -DUSE_SSE_ASM -std=c99 -ffast-math -fexceptions" % get.CFLAGS()

def build():
    shelltools.cd("src/glut/glx")
    autotools.make('CC="%s" \
                    CFLAGS="%s"' % (get.CC(), flags))

def install():
    pisitools.dodir("/usr/include")
    pisitools.dodir("/usr/lib")

    shelltools.copy("include/GL","%s/usr/include/GL" % get.installDIR())
    shelltools.copy("lib/*","%s/usr/lib/" % get.installDIR())

    pisitools.remove("/usr/lib/libglut.so")
    pisitools.remove("/usr/lib/libglut.so.3")
    pisitools.dosym("libglut.so.3","/usr/lib/libglut.so")
    pisitools.dosym("libglut.so.3.7.1","/usr/lib/libglut.so.3")
