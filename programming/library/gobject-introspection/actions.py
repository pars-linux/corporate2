#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    #pisitools.dosed("giscanner/Makefile.in", "py_compile = .*", "py_compile = /bin/true")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static")

def build():
    autotools.make("V=1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "NEWS", "README")

