#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir="xdelta%s" % get.srcVERSION()

def build():
    autotools.make('CFLAGS="%s"' % get.CFLAGS())

def install():
    pisitools.dobin("xdelta3")
    pythonmodules.install()

    pisitools.dodoc("COPYING", "README")
