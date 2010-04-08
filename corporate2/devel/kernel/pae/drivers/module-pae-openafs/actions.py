#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

from pisi.actionsapi import kerneltools

KDIR = kerneltools.getKernelVersion()
WorkDir = "openafs-%s" % get.srcVERSION()

def setup():
    autotools.configure("--with-linux-kernel-headers=/lib/modules/%s/build" % KDIR)

def build():
    autotools.make("-j1 only_libafs")

def install():
    for m in ("libafs.ko", "afspag.ko"):
        pisitools.insinto("/lib/modules/%s/kernel/extra/openafs" % KDIR, "src/libafs/MODLOAD-%s-SP/%s" % (KDIR, m))
