#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007,2008,2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def install():
    pythonmodules.install()

    pisitools.doman("doc/*.1")
    pisitools.doman("doc/*.5")

    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("doc/*.txt")
