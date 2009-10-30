#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir = "PyKDE-%s" % get.srcVERSION()

def setup():
    pythonmodules.run("configure.py \
                       -i \
                       -k %s" % get.kdeDIR())

def build():
    autotools.make()

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "THANKS")
