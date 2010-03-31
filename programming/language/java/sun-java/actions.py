#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = "/"
Name = "6u18"
Arch = "amd64" if get.ARCH() == "x86_64" else "i586"

def setup():
    shelltools.system("sh jdk-%s-dlj-linux-%s.bin --accept-license" % (Name, Arch))

def install():
    pisitools.dodir("/opt")
    shelltools.system("./construct . %s/opt/sun-jdk %s/opt/sun-jre"% (get.installDIR(),get.installDIR()))

    # Install mozilla plugin (not available for x86_64)
    if Arch == "i586":
        pisitools.dodir("/usr/lib/nsbrowser/plugins")
        pisitools.dosym("/opt/sun-jre/plugin/i386/ns7/libjavaplugin_oji.so", "/usr/lib/nsbrowser/plugins/javaplugin.so")

        # Next generation Java plugin is needed by Firefox 3.6+
        pisitools.dosym("/opt/sun-jre/lib/i386/libnpjp2.so", "/usr/lib/nsbrowser/plugins/javaplugin-new.so")

    for doc in ["COPYRIGHT", "LICENSE", "README.html", "README_ja.html", "README_zh_CN.html", "THIRDPARTYLICENSEREADME.txt"]:
        file = "%s/opt/sun-jdk/%s" % (get.installDIR(), doc)
        pisitools.dodoc(file)
        shelltools.unlink(file)
