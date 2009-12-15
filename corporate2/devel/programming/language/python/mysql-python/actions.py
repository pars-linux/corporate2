#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules

WorkDir = "MySQL-python-1.2.3c1"

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
