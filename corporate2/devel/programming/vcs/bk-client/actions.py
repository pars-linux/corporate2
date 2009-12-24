#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="."

def setup():
    shelltools.system("sh bk-client2.0.shar")

def build():
    shelltools.cd("bk-client2.0")
    autotools.make()

def install():
    shelltools.cd("bk-client2.0")
    pisitools.insinto("/usr/bin","bkf","bk-client")
