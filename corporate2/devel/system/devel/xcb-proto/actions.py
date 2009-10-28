#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def setup():
    autotools.autoreconf("-vif")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pythonmodules.fixCompiledPy()

    pisitools.dodoc("doc/*.txt", "COPYING", "NEWS", "README", "TODO")
