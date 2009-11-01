#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "tdb-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-python")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/lib/*.a")

    # Create symlinks for so file
    pisitools.dosym("libtdb.so.%s" % get.srcVERSION(), "/usr/lib/libtdb.so.%s" % get.srcVERSION().split(".")[0])
    pisitools.dosym("libtdb.so.%s" % get.srcVERSION(), "/usr/lib/libtdb.so")

    pisitools.dodoc("docs/README")
