#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."
JBOSS_HOME = "/opt/jboss5"

NoStrip = ["/"]

def install():
    pisitools.dodir(JBOSS_HOME)
    pisitools.insinto(JBOSS_HOME, "jboss-5.1.0.GA/*")

    shelltools.cd("./jboss-5.1.0.GA/")

    # For support JAX-WS 2.0 in java 6 environment
    for f in ("jbossws-native-jaxrpc.jar", "jbossws-native-jaxws-ext.jar", "jbossws-native-jaxws.jar", "jbossws-native-saaj.jar"):
        pisitools.insinto("%s/lib/endorsed" % JBOSS_HOME, "client/%s" % f)

    # Doc operations
    pisitools.dodoc("copyright.txt", "lgpl.html", "readme.html")
    for f in ("copyright.txt", "lgpl.html", "readme.html"):
        pisitools.remove("%s/%s" %(JBOSS_HOME, f))

    # Remove unsupported files
    pisitools.remove("%s/bin/*bat" % JBOSS_HOME)
    pisitools.remove("%s/bin/*exe" % JBOSS_HOME)
