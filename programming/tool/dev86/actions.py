#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="dev86-%s" % get.srcVERSION()

def build():
    if get.ARCH() == "x86_64":
        pisitools.dosed("makefile.in", "alt-libs elksemu", "alt-libs")
        pisitools.dosed("makefile.in", "install-lib install-emu", "install-lib")

    autotools.make("-j1 < /dev/null")

def install():
    for binary in ["bin/*","cpp/bcc-cpp","bcc/bcc-cc1"]:
        pisitools.dobin(binary)

    pisitools.rename("/usr/bin/Bcc","bcc")

    pisitools.doman("man/*.1")
    pisitools.dodoc("Changes","COPYING","MAGIC","README")
