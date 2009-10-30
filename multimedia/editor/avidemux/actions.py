#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = 'avidemux_%s' % get.srcVERSION()
SourceDir = '%s/%s' % (get.workDIR(), WorkDir)

shelltools.export("HOME", "%s" % get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.makedirs("plugins/build")

    shelltools.cd("build")
    shelltools.system("cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release")

def build():
    shelltools.cd("build")
    autotools.make()

    shelltools.cd("../plugins/build")
    shelltools.system("cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DAVIDEMUX_SOURCE_DIR=%s -DAVIDEMUX_INSTALL_PREFIX=%s/usr -DAVIDEMUX_CORECONFIG_DIR=%s/build/config -DCMAKE_BUILD_TYPE=Release" % (SourceDir, get.installDIR(), SourceDir))

def install():
    shelltools.cd("build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../plugins/build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../../")
    pisitools.insinto("/usr/share/pixmaps", "avidemux_icon.png", "avidemux.png")

    pisitools.dodoc("COPYING", "AUTHORS")
    pisitools.doman("man/*")
