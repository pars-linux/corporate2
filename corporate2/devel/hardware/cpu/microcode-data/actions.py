#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = ["/"]
WorkDir = "."
datafile = "microcode-%s.dat" % get.srcVERSION().split("_")[1]

def setup():
    shelltools.chmod(datafile, 0644)

def install():
    pisitools.insinto("/lib/firmware", datafile, "microcode.dat")

