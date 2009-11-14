#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "PREFIX\ \= \/usr\/local", "PREFIX\ \=\ \/usr")

def build():
    # this package does *not* play well with optimisations
    # maybe we should define some static CFLAGS
    shelltools.export("CC", get.CC())
    autotools.make("-j1")

def install():
    autotools.install("PREFIX=%s/usr" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/dosfstools/")
    pisitools.dodoc("COPYING", "ChangeLog", "doc/*")

    pisitools.dosym("/usr/sbin/mkdosfs", "/usr/bin/mkdosfs")

