#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    pythonmodules.run('configure.py \
                       -b /usr/bin \
                       -d /usr/lib/%s/site-packages \
                       -e /usr/include/%s \
                       CFLAGS+="%s" CXXFLAGS+="%s"' % (get.curPYTHON(), get.curPYTHON(), get.CFLAGS(), get.CXXFLAGS()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/")
    pisitools.dodoc("ChangeLog", "LICENSE", "NEWS", "README")
