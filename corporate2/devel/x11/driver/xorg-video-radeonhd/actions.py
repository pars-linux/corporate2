#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "xf86-video-radeonhd-%s" % get.srcVERSION()

def setup():
    shelltools.move("utils/conntest/README", "README.rhd_conntest")

    autotools.autoreconf("-vif")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dobin("utils/conntest/rhd_conntest")

    pisitools.dodoc("ChangeLog", "COPYING", "README", "README.rhd_conntest")
