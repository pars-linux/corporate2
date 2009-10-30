#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # Fix build with 1.2.2
    pisitools.dosed("build.xml", "property name=\"src_dir\" value=\"src\"", "property name=\"src_dir\" value=\".\"")

    shelltools.cd("lib/")
    shelltools.chmod("jsapi.sh")
    shelltools.system("./jsapi.sh")

def build():
    shelltools.system("ant")

def install():
    pisitools.insinto("/usr/share/freetts/lib", "lib/*.jar")
    pisitools.insinto("/usr/share/freetts/lib", "mbrola/*.jar")

    pisitools.insinto("/usr/share/freetts", "speech.properties")

    pisitools.insinto("/usr/share/freetts", "demo/")
    pisitools.insinto("/usr/share/freetts", "tools/")

    pisitools.dodoc("README.txt", "RELEASE_NOTES")


