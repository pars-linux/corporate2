#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "qca-ossl-2.0.0-beta3"

def setup():
    autotools.rawConfigure("--qtdir=/usr/qt/4")

def build():
    autotools.make()

def install():
    pisitools.dolib("lib/libqca-ossl.so", "/usr/qt/4/plugins/crypto")

    pisitools.dodoc("COPYING", "README", "TODO")
