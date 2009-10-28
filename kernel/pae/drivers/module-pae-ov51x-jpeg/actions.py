#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ov51x-jpeg-%s" % get.srcVERSION()
KDIR = kerneltools.getKernelVersion()

def setup():
    pisitools.dosed("Makefile", "\$\(shell uname -r\)", KDIR)

def build():
    autotools.make("KERNEL_DIR=/usr/src/linux-headers-%s" % KDIR)

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "*.ko")
