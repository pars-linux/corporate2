#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

version = get.srcVERSION()
version_underscore, patch_release = version.replace(".", "_").rsplit("_", 1)

WorkDir = "boost_%s_%s" % (version_underscore, patch_release)

prefix = "/%s" % get.defaultprefixDIR()
shelltools.export("EXPAT_INCLUDE", "%s/include" % prefix)
shelltools.export("EXPAT_LIBPATH", "%s/lib" % prefix)

def setup():
    pisitools.dosed("tools/build/v2/tools/gcc.jam", "PARDUS_CXX_", get.CXX())
    pisitools.dosed("tools/build/v2/tools/gcc.jam", "PARDUS_CXXFLAGS", "%s -fPIC" % get.CXXFLAGS())
    pisitools.dosed("tools/build/v2/tools/gcc.jam", "PARDUS_LDFLAGS", get.LDFLAGS())
    pisitools.dosed("libs/python/build/Jamfile.v2", "PARDUS_PYTHON", get.curPYTHON())

    autotools.rawConfigure("--with-toolset=gcc \
                            --with-icu \
                            --prefix=%s/usr" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.install()

    # Remove static libraries
    pisitools.remove("/usr/lib/*.a")

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("LICENSE*")
