#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "omnibook-%s" % get.srcVERSION().split("_")[1]
KDIR = kerneltools.getKernelVersion()

def setup():
    pisitools.dosed("Makefile", "^KVERS.*$", "KVERS = %s" % KDIR)

def build():
    autotools.make()

def install():
    pisitools.dosed("Makefile", "^KSRC.*$", "KSRC = /lib/modules/%s/build" % KDIR)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
