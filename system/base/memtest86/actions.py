#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s+-%s" % (get.srcNAME(), get.srcVERSION())

def build():
    autotools.make()

def install():
    pisitools.insinto("/boot", "memtest.bin", "memtest")

    pisitools.dodoc("FAQ", "README*")

