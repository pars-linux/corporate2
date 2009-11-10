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

WorkDir="mozilla"

def build():
    shelltools.export("BUILD_OPT","1")
    shelltools.export("NSS_ENABLE_ECC","1")
    shelltools.export("OPT_FLAGS","%s -g -fno-strict-aliasing" % get.CFLAGS())
    # use system zlib
    shelltools.export("PKG_CONFIG_ALLOW_SYSTEM_LIBS", "1")
    shelltools.export("PKG_CONFIG_ALLOW_SYSTEM_CFLAGS", "1")

    shelltools.cd("security/nss")
    autotools.make("nss_build_all -j1")

def install():
    for binary in ["certutil", "modutil", "pk12util", "signtool", "ssltap"]:
        pisitools.insinto("/usr/bin","dist/Linux*/bin/%s" % binary, sym=False)

    for lib in ["*.a","*.chk","*.so"]:
        pisitools.insinto("/usr/lib/nss","dist/Linux*/lib/%s" % lib, sym=False)

    # Headers
    for header in ["dist/private/nss/*.h","dist/public/nss/*.h"]:
        pisitools.insinto("/usr/include/nss", header, sym=False)

    # Drop executable bits from headers
    shelltools.chmod("%s/usr/include/nss/*.h" % get.installDIR(), mode=0644)

