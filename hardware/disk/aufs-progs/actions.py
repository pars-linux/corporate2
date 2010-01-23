#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

from pisi.actionsapi import kerneltools

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().split("_")[1])

def setup():
    pisitools.dosed("Makefile", "-O -Wall", get.CFLAGS())
    pisitools.dosed("Makefile", "^KDIR = .*$", "KDIR = /lib/modules/%s/build" % kerneltools.getKernelVersion())

def build():
    autotools.make()

def install():
    pisitools.dodir("usr/bin")
    pisitools.dodir("sbin")
    pisitools.dodir("usr/share/aufs-progs")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING")
