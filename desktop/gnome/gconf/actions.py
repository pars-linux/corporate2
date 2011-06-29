#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static \
                         --enable-gtk \
                         --enable-defaults-service \
                         --with-gtk=2.0 \
                         --enable-silent-rules")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/etc/gconf/schemas")
    pisitools.dodir("/etc/gconf/gconf.xml.system")
    pisitools.dodir("/usr/share/GConf/gsettings")

    pisitools.dodoc("README", "TODO", "NEWS", "ChangeLog", "AUTHORS")
