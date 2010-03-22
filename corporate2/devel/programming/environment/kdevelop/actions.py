#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

KeepSpecial = ["libtool"]

def setup():
    # Update the admin dir used in KDE template projects.
    for i in shelltools.ls("admin/*"):
        shelltools.copy(i, "parts/appwizard/common/admin/")

    # Fix automake and python detection
    pisitools.dosed("admin/cvs.sh", "automake\*1\.10\*", "automake*1.1[0-5]*")
    pisitools.dosed("admin/acinclude.m4.in", "KDE_CHECK_PYTHON_INTERN\(\"2.5", "KDE_CHECK_PYTHON_INTERN(\"%s" % get.curPYTHON().split("python")[1])
    kde.make("-f admin/Makefile.common")

    kde.configure("--with-kdelibsdoxy-dir=%s/share/doc/HTML/en/kdelibs-apidocs \
                   --enable-java \
                   --enable-python \
                   --enable-ruby \
                   --enable-ada \
                   --enable-fortran \
                   --enable-haskell \
                   --enable-pascal \
                   --enable-perl \
                   --enable-php \
                   --enable-sql \
                   --enable-antproject \
                   --enable-subversion" % get.kdeDIR())

def build():
    kde.make()

def install():
    kde.install()
