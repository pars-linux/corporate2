#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.export("DO_NOT_COMPILE", "dcoppython python")
    kde.configure("--with-java=/opt/sun-jdk \
                   --with-python-dir=/usr/lib/%s \
                   --without-arts" % get.curPYTHON())

def build():
    kde.make("-j1")

def install():
    kde.install()
