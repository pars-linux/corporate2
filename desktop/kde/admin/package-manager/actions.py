#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def install():
    pythonmodules.install()

    # In C2 we dont need these desktop files 
    pisitools.remove("/usr/share/applications/package-manager-*.desktop")

