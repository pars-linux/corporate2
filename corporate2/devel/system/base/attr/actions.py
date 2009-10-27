#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("OPTIMIZER", get.CFLAGS())
    shelltools.export("DEBUG", "-DNDEBUG")
    # shelltools.export("CC", "gcc")

    autotools.autoconf()
    autotools.rawConfigure("--libdir=/lib \
                            --mandir=/usr/share/man \
                            --libexecdir=/lib \
                            --bindir=/bin")
def build():
    autotools.make()

def install():
    autotools.make("DIST_ROOT=%s install install-lib install-dev" % get.installDIR())
