#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "qt-x11-free-%s" % get.srcVERSION()

# Where to install
QTBASE = "/usr/qt/3"
# For which platform
PLATFORM = "linux-g++"

def define_global():
    shelltools.export("PATH", "%s/bin:%s" % (get.curDIR(), get.ENV("PATH")))
    shelltools.export("LD_LIBRARY_PATH", "%s/lib:%s" % (get.curDIR(), get.ENV("LD_LIBRARY_PATH")))

def setup():
    define_global()

    # Yeah, we accept your licence :)
    pisitools.dosed("configure", "read acceptance", "acceptance=yes")

    # Qt has serious security issue,
    # see http://bugs.gentoo.org/show_bug.cgi?id=75181 and http://www.gentoo.org/security/en/glsa/glsa-200503-01.xml
    pisitools.dosed("mkspecs/linux-g++/qmake.conf", "QMAKE_RPATH.*= -Wl,-rpath,", "QMAKE_RPATH\t=")

    # Set c/xxflags and ldflags
    pisitools.dosed("mkspecs/%s/qmake.conf" % PLATFORM, "QMAKE_CFLAGS_RELEASE.*=.*", "QMAKE_CFLAGS_RELEASE=%s" % get.CFLAGS())
    pisitools.dosed("mkspecs/%s/qmake.conf" % PLATFORM, "QMAKE_CXXFLAGS_RELEASE.*=.*", "QMAKE_CXXFLAGS_RELEASE=%s" % get.CXXFLAGS())
    pisitools.dosed("mkspecs/%s/qmake.conf" % PLATFORM, "QMAKE_LFLAGS_RELEASE.*=.*", "QMAKE_LFLAGS_RELEASE=%s" % get.LDFLAGS())

    autotools.rawConfigure("-sm \
                            -thread \
                            -stl \
                            -system-libjpeg \
                            -verbose \
                            -largefile \
                            -qt-imgfmt-{jpeg,mng,png} \
                            -tablet \
                            -system-libmng \
                            -system-libpng \
                            -lpthread \
                            -xft \
                            -platform %s \
                            -xplatform %s \
                            -xrender \
                            -prefix %s \
                            -libdir %s/lib \
                            -fast \
                            -qt-gif \
                            -cups \
                            -enable-module=opengl \
                            -xinerama \
                            -system-zlib \
                            -ipv6 \
                            -no-sql-ibase \
                            -plugin-sql-sqlite \
                            -plugin-sql-mysql \
                            -plugin-sql-psql \
                            -I/usr/include/mysql/ \
                            -I/usr/include/postgresql \
                            -I/usr/include/postgresql/server \
                            -no-sql-odbc \
                            -release \
                            -no-g++-exceptions \
                            -dlopen-opengl" % (PLATFORM, PLATFORM, QTBASE, QTBASE ))

def build():
    define_global()

    shelltools.export("SYSCONF", "%s/etc/settings" % QTBASE)
    autotools.make()

def install():
    define_global()

    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    # Correct Makefile's
    pisitools.dosed("examples/Makefile", get.curDIR() , QTBASE)
    for file in shelltools.ls("examples/*/Makefile"):
        pisitools.dosed(file, get.curDIR() , QTBASE)

    pisitools.dosed("tutorial/Makefile", get.curDIR() , QTBASE)
    for file in shelltools.ls("tutorial/*/Makefile"):
        pisitools.dosed(file, get.curDIR() , QTBASE)

    # Move tutorial and example into QTBASE
    pisitools.insinto(QTBASE, "tutorial")
    pisitools.insinto(QTBASE, "examples")

    # Correct .qmake.cache
    pisitools.insinto(QTBASE, ".qmake.cache")
    pisitools.dosed("%s/usr/qt/3/.qmake.cache" % get.installDIR(), get.curDIR() , QTBASE)

    # No static libs
    pisitools.remove("/usr/qt/3/lib/*.a")

    # No designer prl files
    pisitools.remove("/usr/qt/3/lib/libdesignercore.prl")
    pisitools.remove("/usr/qt/3/lib/libeditor.prl")

    # This symlink was pointing to a nonsense location in /var/pisi, causing
    # pisi to bork about the package integrity.
    pisitools.remove("/usr/qt/3/mkspecs/linux-g++/linux-g++")

    # Symlink pkgconfig file
    pisitools.dosym("/usr/qt/3/lib/pkgconfig/qt-mt.pc","/usr/lib/pkgconfig/qt-mt.pc")
