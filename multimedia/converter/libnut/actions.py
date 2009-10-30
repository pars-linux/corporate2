#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# nut is done with checkouts from
# svn://svn.mplayerhq.hu/nut/src/trunk

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "nut"

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())

    pisitools.dodoc("COPYING", "README*")
