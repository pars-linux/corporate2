#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#
# git clone http://repo.or.cz/r/microdia.git
#

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "microdia"
KDIR = kerneltools.getKernelVersion()

def setup():
    pisitools.dosed("Makefile", "^KVER=.*", "KVER=%s" % KDIR)

def build():
    autotools.make("KSRC=/lib/modules/%s/build driver" % KDIR)

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "*.ko")

    pisitools.dodoc("README*")
