#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "fw"

def install():
    pisitools.insinto("/lib/firmware", "acx*")
    pisitools.dosym("/lib/firmware/acx111_2.3.1.31/tiacx111c16", "/lib/firmware/tiacx111c16")
