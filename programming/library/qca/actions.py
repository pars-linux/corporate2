#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "qca-1.0"

def setup():
    autotools.rawConfigure("--prefix=/usr/qt/3")
    pisitools.dosed("Makefile", "(?m)^(CFLAGS.*)",  "CFLAGS =" + get.CFLAGS())
    pisitools.dosed("Makefile", "(?m)^(CXXFLAGS.*)", "CXXFLAGS =" + get.CXXFLAGS())

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    pisitools.dodoc("COPYING", "README")
