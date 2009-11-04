#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile.config", "pardusCC", get.CC())

def build():
    autotools.make('CFLAGS="%s -fPIC" LDFLAGS="%s" -j1' % (get.CFLAGS().replace("-O2", "-O3"), get.LDFLAGS()))

def install():
    pisitools.dodir("/")
    autotools.make('-j1 package pkgdir=%s/usr' % get.installDIR())

    pisitools.remove("/usr/bin/manweb")

    for data in ["VERSION","pkginfo","README","config_template"]:
        pisitools.remove("/usr/%s" % data)

    for directory in ["link", "man/web"]:
        pisitools.removeDir("/usr/%s" % directory)

    pisitools.domove("/usr/misc", "/usr/share/netpbm")
    pisitools.domove("/usr/man", "/usr/share")

    # remove conflicts with jbigkit
    for i in ["pbm", "pgm"]:
        pisitools.remove("/usr/share/man/man5/%s.5" % i)

    pisitools.dodoc("README", "doc/*LICENSE*")
