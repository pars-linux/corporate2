# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DMUST_BUILD_CURL_CLIENT:BOOL=ON        \
                          -DMUST_BUILD_LIBWWW_CLIENT:BOOL=OFF     \
                          -DBUILD_SHARED_LIBS:BOOL=ON             \
                          -DENABLE_TOOLS:BOOL=ON", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()
    shelltools.cd("..")

    shelltools.chmod("%s/usr/lib/*.so" % get.installDIR(), 0755)

    pisitools.dodoc("README")
