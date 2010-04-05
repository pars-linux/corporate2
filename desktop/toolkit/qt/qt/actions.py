#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

WorkDir = "qt-x11-opensource-src-%s" % get.srcVERSION().replace('_','-')
qtbase = "/usr/qt/4"

def setup():
    #make sure we don't use them
    for d in ('libjpeg', 'freetype', 'libpng', 'zlib', 'libtiff'):
        shelltools.unlinkDir("src/3rdparty/%s" % d)

    filteredCFLAGS = get.CFLAGS().replace("-g3", "-g")
    filteredCXXFLAGS = get.CXXFLAGS().replace("-g3", "-g")

    vars = {"PARDUS_CC" :       get.CC(),
            "PARDUS_CXX":       get.CXX(),
            "PARDUS_CFLAGS":    filteredCFLAGS,
            "PARDUS_LDFLAGS":   get.LDFLAGS()}

    for k, v in vars.items():
        pisitools.dosed("mkspecs/common/g++.conf", k, v)

    shelltools.export("CFLAGS", filteredCFLAGS)
    shelltools.export("CXXFLAGS", filteredCXXFLAGS)

    #-no-pch makes build ccache-friendly
    autotools.rawConfigure("-no-pch \
                            -v \
                            -stl \
                            -fast \
                            -prefix %s \
                            -libdir %s/lib \
                            -qdbus \
                            -qvfb \
                            -glib \
                            -no-sql-sqlite2 \
                            -system-sqlite \
                            -plugin-sql-sqlite \
                            -plugin-sql-mysql \
                            -plugin-sql-psql \
                            -plugin-sql-ibase \
                            -I/usr/include/mysql/ \
                            -I/usr/include/firebird/ \
                            -I/usr/include/postgresql/server/ \
                            -release \
                            -no-separate-debug-info \
                            -phonon \
                            -no-phonon-backend \
                            -webkit \
                            -no-rpath \
                            -openssl-linked \
                            -dbus-linked \
                            -xmlpatterns \
                            -opensource \
                            -confirm-license " % (qtbase, qtbase))

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    pisitools.dodir("/usr/bin")

    #Remove phonon, we use KDE's phonon but we have to build Qt with Phonon support for webkit and some other stuff
    pisitools.remove("/usr/qt/4/lib/libphonon*")
    pisitools.removeDir("/usr/qt/4/include/phonon")
    pisitools.remove("/usr/qt/4/lib/pkgconfig/phonon*")

    # FIXME:
    pisitools.removeDir("/usr/share/dbus-1")

    for app in ["qmake", "designer", "assistant", "linguist", "qtconfig", "uic", "rcc", "moc", "lrelease", "lupdate", "lconvert"]:
        pisitools.dosym("/usr/qt/4/bin/%s" % app, "/usr/bin/%s-qt4" % app)

    pisitools.insinto("/usr/qt/4/bin", "tools/qdoc3/qdoc3")

    for app in ["qdbus", "qdbuscpp2xml", "qdbusxml2cpp", "qt3to4", "qtdemo", "uic3", "pixeltool", "qdoc3", "qhelpgenerator"]:
        pisitools.dosym("/usr/qt/4/bin/%s" % app, "/usr/bin/%s" % app)

    # Turkish translations
    shelltools.export("LD_LIBRARY_PATH", "%s/usr/qt/4/lib" % get.installDIR())
    shelltools.system("%s/usr/qt/4/bin/lrelease l10n-tr/*.ts" % get.installDIR())
    pisitools.insinto("/usr/qt/4/translations", "l10n-tr/*.qm")

    pisitools.insinto("/usr/lib/pkgconfig", "%s/usr/qt/4/lib/pkgconfig/*.pc" % get.installDIR())
    pisitools.remove("/usr/qt/4/lib/pkgconfig")

    # Fix all occurances of WorkDir in pc files
    pisitools.dosed("%s/usr/lib/pkgconfig/*.pc" % get.installDIR(), "%s/qt-x11-opensource-src-%s" % (get.workDIR(),get.srcVERSION()),"/usr/qt/4")

    mkspecPath = "/usr/qt/4/mkspecs"

    for root, dirs, files in os.walk("%s/usr/qt/4" % get.installDIR()):
        # Remove unnecessary spec files..
        if root.endswith(mkspecPath):
            for dir in dirs:
                if not dir.startswith("linux") and dir not in ["common", "qws", "features", "default"]:
                    pisitools.removeDir(os.path.join(mkspecPath,dir))
        for name in files:
            if name.endswith(".prl"):
                pisitools.dosed(os.path.join(root, name), "^QMAKE_PRL_BUILD_DIR.*", "")
