#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "qca-tls-1.0"

def setup():
    autotools.rawConfigure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    pisitools.dodoc("README")
