#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("./autogen.sh --with-qmake=qmake-qt4")
    shelltools.copy("/usr/share/gnuconfig/config.sub", get.srcDIR())
    shelltools.copy("/usr/share/gnuconfig/config.guess", get.srcDIR())
    autotools.configure("--with-qmake=qmake-qt4")

def build():
    shelltools.export("HOME", get.workDIR())
    autotools.make()

def install():
    autotools.install("INSTALL_ROOT=%s" % get.installDIR())
