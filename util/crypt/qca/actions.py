# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "qca-%s" % get.srcVERSION()

def setup():
    autotools.rawConfigure("--prefix=/usr/qt/3")
    pisitools.dosed("Makefile", "^(CXXFLAGS .*)$", r"\1 -fPIC ")

def build():
    autotools.make("CXX=%s LINK=%s" % (get.CXX(), get.CXX()))

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    pisitools.dodoc("COPYING", "README")
