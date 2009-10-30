#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dosed("Makefile", "mkdir -p $(bindir)", "")
    autotools.install("prefix=%s/usr" % get.installDIR())

    pisitools.dodoc("README")

    shelltools.cd("docs")
    pisitools.dodoc("*")
