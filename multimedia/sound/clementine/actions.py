#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    #for i in ["libprojectm", "qxt", "qtiocompressor"]:
    for i in ["libprojectm", "qxt", "libechonest"]:
        shelltools.unlinkDir("3rdparty/%s" % (i))

    # Upstream supports only gstreamer engine, other engines are unstable and lacking features.
    # QTSINGLEAPPLICATION is builtin since we need to patch Qt just for this package and Gökçen has given OK
    # for using builtin qtsingleapplication.
    cmaketools.configure("-DHAVE_LIBNOTIFY=ON \
                          -DENGINE_GSTREAMER_ENABLED=ON \
                          -DENGINE_QT_PHONON_ENABLED=OFF \
                          -DENGINE_LIBVLC_ENABLED=OFF \
                          -DENGINE_LIBXINE_ENABLED=OFF \
                          -DUSE_SYSTEM_QXT=ON \
                          -DUSE_SYSTEM_QTSINGLEAPPLICATION=OFF \
                          -DSTATIC_SQLITE=OFF \
                          -DUSE_SYSTEM_PROJECTM=ON \
                          -DENABLE_WIIMOTEDEV=ON \
                          -DENABLE_LIBGPOD=ON \
                          -DENABLE_IMOBILEDEVICE=ON \
                          -DENABLE_LIBMTP=ON \
                          -DENABLE_GIO=ON \
                          -DENABLE_VISUALISATIONS=ON \
                          -DQXTCORE_INCLUDE_DIRS=/usr/qt/4/include/QxtCore \
                          -DQXTGUI_INCLUDE_DIRS=/usr/qt/4/include/QxtGui \
                          -DQXT_LIBRARIES=/usr/qt/4/lib/libQxtGui.so \
                          -DBUNDLE_PROJECTM_PRESETS=OFF", sourceDir=".")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    for i in ("16","32","64"):
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (i,i), "dist/clementine_%s.png" % i, "clementine.png")

    pisitools.insinto("/usr/share/clementine/locale", "src/translations/*.qm")
    pisitools.dosym("/usr/share/icons/hicolor/64x64/apps/clementine.png", "/usr/share/pixmaps/clementine.png")

    pisitools.dodoc("Changelog", "COPYING", "TODO")
