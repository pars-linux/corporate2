#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "ungrab-winmodem-20080126"
KDIR = kerneltools.getKernelVersion()

def setup():
    pisitools.dosed("Makefile", "SUBDIRS=", "M=")
    pisitools.dosed("Makefile", "^KERNEL_VER:=.*", "KERNEL_VER:= %s" % KDIR)

def build():
    autotools.make("KERNEL_DIR=/lib/modules/%s/build" % KDIR)

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "*.ko")
