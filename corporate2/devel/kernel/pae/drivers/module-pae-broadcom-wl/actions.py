#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
KDIR = kerneltools.getKernelVersion()

def build():
    autotools.make("-C /lib/modules/%s/build M=%s modules" % (KDIR, get.curDIR()))

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "wl.ko")
