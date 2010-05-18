#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "."))

def setup():
    # Remove version info from doc dir
    pisitools.dosed("CMakeLists.txt", "\"share\/doc\/\$\{MAIN_DIR_NAME\}.*", "\"share/doc/${MAIN_DIR_NAME}/\")")
    cmaketools.configure("-DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE \
                          -DCMAKE_SKIP_RPATH=TRUE")
    #-DLIB_INSTALL_DIR=%s -DWANT_CAIRO=1" % "/usr/lib/"

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "resources/icons/scribus.png")
    pisitools.insinto("/usr/share/pixmaps", "resources/icons/scribusdoc.png", "x-scribus.png")
