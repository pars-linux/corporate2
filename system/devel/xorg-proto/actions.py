#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
SkipFiles = ["filelist", "patches", "pisiBuildState"]

def setup():
    for package in shelltools.ls("."):
        if package in SkipFiles:
            continue
        shelltools.cd(package)
        if package.startswith("vncproto"):
            autotools.autoreconf("-vif")
        autotools.configure()
        shelltools.cd("../")

def build():
    for package in shelltools.ls("."):
        if package in SkipFiles:
            continue
        shelltools.cd(package)
        autotools.make()
        shelltools.cd("../")

def install():
    for package in shelltools.ls("."):
        if package in SkipFiles:
            continue
        shelltools.cd(package)
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")

    pisitools.domove("%s/*[!-]proto/*" % get.docDIR(), "/".join((get.docDIR(), get.srcNAME())))
    pisitools.removeDir("%s/*[!-]proto" % get.docDIR())
