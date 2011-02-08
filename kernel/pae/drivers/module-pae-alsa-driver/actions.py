#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

from pisi.actionsapi import kerneltools

KDIR = kerneltools.getKernelVersion()
NoStrip = ["/"]

if "_" in get.srcVERSION():
    # Snapshot
    WorkDir = "alsa-driver"
else:
    # Upstream tarball
    WorkDir = "alsa-driver-%s" % get.srcVERSION()

def setup():
    autotools.configure("--with-oss \
                         --with-kernel=/lib/modules/%s/build \
                         --with-isapnp=yes \
                         --with-sequencer=yes \
                         --with-card-options=all \
                         --disable-verbose-printk \
                         --enable-dynamic-minors \
                         --with-cards=all" % KDIR)

    # Needed for V4L stuff
    shelltools.sym("../../include/config.h", "sound/include/config.h")
    shelltools.sym("../../include/config1.h", "sound/include/config1.h")

def build():
    autotools.make()

    # Build v4l drivers
    shelltools.copy("Module.symvers", "v4l/")
    autotools.make("-C /lib/modules/%s/build M=%s/v4l modules" % (KDIR, get.curDIR()))

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-modules")

    # Install v4l drivers
    for d in ["saa7134", "cx88", "cx231xx", "em28xx"]:
        pisitools.insinto("/lib/modules/%s/kernel/sound/drivers" % KDIR, "v4l/%s/*.ko" % d)

    # Copy symvers file for external module building like saa7134-alsa, cx2388-alsa, etc.
    pisitools.insinto("/lib/modules/%s/kernel/sound" % KDIR, "Module.symvers", "Module.symvers.alsa")
