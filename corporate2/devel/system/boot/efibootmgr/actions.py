#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    pisitools.dosbin("src/efibootmgr/efibootmgr")

    pisitools.doman("src/man/man8/efibootmgr.8")

    pisitools.dodoc("COPYING", "README", "AUTHORS", "doc/*")
