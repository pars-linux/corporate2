#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

WorkDir = "tomcat-connectors-1.2.32-src/"

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

def setup():
    shelltools.cd("native")
    autotools.configure("--disable-static --with-apxs=/usr/sbin/apxs")

def build():
    shelltools.cd("native")
    autotools.make()

def install():
    pisitools.insinto("/usr/lib/apache2/modules/", "native/apache-2.0/mod_jk.so")
    pisitools.insinto("/etc/apache2/conf.d/", "conf/httpd-jk.conf")

    pisitools.dodoc("conf/uriworkermap.properties", "conf/workers.properties", "conf/workers.properties.minimal", "LICENSE")
    pisitools.insinto("/usr/share/doc/mod_jk/help/", "docs/*")
