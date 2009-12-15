#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
#from pisi.actionsapi import shelltools

def install():
    pythonmodules.install()
    #documentation can be created after python-sphinx package is merged.
    #shelltools.cd("doc")
    #pythonmodules.run("make.py all")
