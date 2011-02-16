#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    repo_uri = "http://packages.pardus.org.tr/pardus/kurumsal2/stable/%s/pisi-index.xml.xz" % get.ARCH()
    pisitools.dosed("yali/constants.py", "@REPO_URI@", repo_uri)

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
