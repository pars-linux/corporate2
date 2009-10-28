#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kerneltools
from pisi.actionsapi import get

KVERSION = kerneltools.getKernelVersion()

def setup():
    pisitools.dosed("Makefile", "KVERSION =.*$", "KVERSION = %s" % KVERSION)

def build():
    autotools.make()

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KVERSION, "lenovo-sl-laptop.ko")

    pisitools.dodoc("README")
