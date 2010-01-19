#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    pisitools.dosed("giscanner/Makefile.in", "py_compile = .*", "py_compile = /bin/true")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static")

def build():
    autotools.make("-j1 V=1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.domove("/usr/lib/gobject-introspection/giscanner", "/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.removeDir("/usr/lib/gobject-introspection")

    pisitools.dodoc("AUTHORS", "COPYING*", "NEWS", "README")

