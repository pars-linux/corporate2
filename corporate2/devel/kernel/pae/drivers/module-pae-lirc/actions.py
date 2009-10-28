#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lirc-%s" % get.srcVERSION().replace("_", "")
ldflags = get.LDFLAGS().replace("-Wl,-O1", "")

KDIR = kerneltools.getKernelVersion()

def setup():
    shelltools.export("LDFLAGS", ldflags)
    autotools.autoreconf("-fi")
    pisitools.dosed("configure*", "portaudio.h", "PORTAUDIO_DISABLED")

    autotools.configure("--localstatedir=/var \
                         --enable-sandboxed \
                         --enable-shared \
                         --disable-static \
                         --disable-debug \
                         --with-transmitter \
                         --with-x \
                         --with-port=0x3f8 \
                         --with-irq=4 \
                         --with-driver=all \
                         --with-syslog=LOG_DAEMON \
                         --with-kerneldir=/lib/modules/%s/build \
                         --with-moduledir=/lib/modules/%s/extra" % (KDIR, KDIR))

def build():
    pisitools.dosed("Makefile", "SUBDIRS=", "M=")
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr")
