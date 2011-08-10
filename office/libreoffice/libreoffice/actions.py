#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os
import re
import glob
import locale

WorkDir = "%s-bootstrap-%s" % (get.srcNAME(), get.srcVERSION())
AppDir = "/opt/LibreOffice"
NoStrip = ["%s/lib/libreoffice/basis-link/share" % AppDir, "%s/lib/libreoffice/share" % AppDir]

def getJobCount():
    # If jobs field in pisi.conf is greater than 1, use 'this value - 1' as number of cpus. There is also a max-jobs configure opt. but it's buggy now
    return max(int(get.makeJOBS().strip().replace("-j", "")) - 1, 1)

def setup():

    # Remove previous Linux build scripts if any
    for f in glob.glob("Linux*Set.sh"):
        shelltools.unlink(f)

    autotools.autoconf("-f")

    #TODO: packaging internal stuff like altlinuxhyph, mythes etc. and removing all --without-system-* would be a good job

    #libdir is needed to set exec_prefix
    #enable-cairo to make HW Acceleration enabled
    shelltools.system('./configure \
                       --prefix=%s \
                       --libdir=%s/lib \
                       --sysconfdir=/etc \
                       --disable-fontooo \
                       --disable-rpath \
                       --disable-odk \
                       --disable-qadevooo \
                       --disable-gnome-vfs \
                       --disable-kde \
                       --disable-mono \
                       --enable-dbus \
                       --enable-vba \
                       --enable-opengl \
                       --enable-minimizer \
                       --enable-presenter-console \
                       --enable-pdfimport \
                       --enable-wiki-publisher \
                       --enable-report-builder \
                       --enable-epm=\"no\" \
                       --without-nas \
                       --without-writer2latex \
                       --without-myspell-dicts \
                       --with-lang=\"de en-US es fr hu it nl pt-BR ru sv tr\" \
                       --with-vendor=\"Pardus\" \
                       --with-system-agg \
                       --with-system-boost \
                       --with-system-cairo \
                       --with-system-cppunit \
                       --with-system-curl \
                       --with-system-db \
                       --with-system-expat \
                       --with-system-hunspell \
                       --with-system-hsqldb \
                       --with-system-icu \
                       --with-system-jpeg \
                       --with-system-libwpd \
                       --with-system-libwpg \
                       --with-system-libwps \
                       --with-system-libxslt \
                       --with-system-lpsolve \
                       --with-system-mozilla \
                       --with-system-neon \
                       --with-system-stdlibs \
                       --with-system-odbc-headers \
                       --with-system-openssl \
                       --with-system-poppler \
                       --with-system-python \
                       --with-system-redland \
                       --with-system-sane-header \
                       --with-system-servlet-api \
                       --with-system-xrender-headers \
                       --with-system-vigra \
                       --with-system-zlib \
                       --with-system-dicts \
                       --with-openldap \
                       --with-ant-home=/usr/share/ant \
                       --with-jdk-home=/opt/sun-jdk \
                       --with-intro-bitmap=\"%s/src/openintro_pardus.png\" \
                       --with-about-bitmap=\"%s/src/openabout_pardus.png\" \
                       --with-external-dict-dir=/usr/share/hunspell \
                       --with-jdk-home=/opt/sun-jdk \
                       --with-hsqldb-jar=/usr/share/java/hsqldb.jar \
                       --with-dict=ALL \
                       --with-extension-integration \
                       --with-max-jobs=%s' % (AppDir, AppDir, os.path.join(get.workDIR(),WorkDir), os.path.join(get.workDIR(),WorkDir), getJobCount()))

def build():
    oldLocale = locale.setlocale(locale.LC_ALL)
    locale.setlocale(locale.LC_ALL, 'C') # Turkish build is broken

    autotools.make()

    locale.setlocale(locale.LC_ALL, oldLocale) # Restore default locale

def install():
    shelltools.export("HOME", get.workDIR())

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #dosym main executables
    for bin in ("lobase", "localc", "lodraw", "loimpress", "lomath", "loweb", "lowriter", "soffice", "unopkg"):
        pisitools.dosym("libreoffice", "/usr/bin/%s" % bin)

    # Icons
    for icon in glob.glob("sysui/desktop/icons/hicolor/48x48/apps/*.png"):
        pisitools.insinto("/usr/share/pixmaps", icon, "libreoffice-%s" % os.path.basename(icon))
    pisitools.insinto("/usr/share/pixmaps", "sysui/desktop/icons/hicolor/48x48/mimetypes/oasis-web-template.png", "libreoffice-web.png")

    #Put pyuno to python directory and add python modules directory to sys.path in uno.py
    unoPath = "%s/lib/libreoffice/basis-link/program/uno.py" % AppDir
    unopy = open(get.installDIR() + unoPath).read()
    pisitools.dodir("/usr/lib/%s/site-packages/" % get.curPYTHON())
    newunopy = open("%s/usr/lib/%s/site-packages/uno.py" % (get.installDIR(), get.curPYTHON()), "w")
    newunopy.write("import sys\nsys.path.append('%s/lib/libreoffice/basis-link/program')\n%s" % (AppDir, unopy))
    newunopy.close()
    pisitools.remove(unoPath)
    pisitools.domove("%s/lib/libreoffice/basis-link/program/unohelper.py" % AppDir, "/usr/lib/%s/site-packages" % get.curPYTHON())

    pisitools.dodoc("ChangeLog","COPYING*")

    #install our own sofficerc file
    pisitools.insinto("%s/lib/libreoffice/program" % AppDir, "sofficerc.pardus", "sofficerc")

    # Remove installation junk
    pisitools.remove("/gid*")
