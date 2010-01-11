#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "gspca-1496806932f0"
KDIR = kerneltools.getKernelVersion()

def setup():
    pisitools.dosed("v4l/Makefile", "^v4l_modules.*lsmod.*$", "")

def build():
    autotools.make("VER=%s" % KDIR)

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "v4l/*.ko")

