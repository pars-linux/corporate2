#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="ATLAS"

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    shelltools.system("../configure \
                       -Si cputhrchk 0 \
                       -Fa alg -fPIC \
                       -b 32 \
                       --with-netlib-lapack=/usr/lib/liblapack.a")

def build():
    shelltools.cd("build")

    autotools.make("-j1")

    shelltools.cd("lib")
    autotools.make("shared")

def install():
    for lib in ["atlas","cblas","f77blas"]:
        pisitools.dolib("build/lib/lib%s.so" % lib)

    for header in ["cblas.h","clapack.h"]:
        pisitools.insinto("/usr/include", "include/%s" % header)

    pisitools.dodoc("README","doc/*")
