#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "decorator-%s" % get.srcVERSION()

def check():
    shelltools.system("nosetests --with-doctest -e documentation")

def install():
    pythonmodules.install()

    pisitools.dodoc("README.txt", "documentation.html", "documentation.py")
