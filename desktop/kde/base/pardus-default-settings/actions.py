#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.dosed("usr/kde/3.5/share/config/kdeglobals", "BCTango", "Tango")
    for d in ("etc", "usr"):
        pisitools.insinto("/", d)
