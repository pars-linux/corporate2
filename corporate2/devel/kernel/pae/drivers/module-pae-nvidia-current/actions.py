#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "NVIDIA-Linux-x86-%s" % get.srcVERSION()
KDIR = kerneltools.getKernelVersion()
NoStrip = ["/lib/modules"]

driver = "nvidia-current"

def build():
    shelltools.export("SYSSRC", "/lib/modules/%s/build" % KDIR)
    shelltools.cd("usr/src/nv")

    autotools.make("module")

def install():
    # Kernel driver
    pisitools.insinto("/lib/modules/%s/extra/nvidia" % KDIR, "usr/src/nv/nvidia.ko", "%s.ko" % driver)
