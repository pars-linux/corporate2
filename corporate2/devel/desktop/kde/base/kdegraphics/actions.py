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
from pisi.actionsapi import pisitools

KeepSpecial=["libtool"]
shelltools.export("HOME", get.workDIR())

def setup():
    # Fix automake and python detection
    pisitools.dosed("admin/cvs.sh", "automake\*1\.10\*", "automake*1.1[0-5]*")
    pisitools.dosed("admin/acinclude.m4.in", "KDE_CHECK_PYTHON_INTERN\(\"2.5", "KDE_CHECK_PYTHON_INTERN(\"%s" % get.curPYTHON().split("python")[1])
    kde.make("-f admin/Makefile.common")

    shelltools.export("DO_NOT_COMPILE", "kpovmodeler kmrml kview")

    # New fribidi do not have fribidi-config, make it use pkg-config instead
    # Caution: This is needed to enable KSVG support
    shelltools.export("FRIBIDI_CONFIG", "pkg-config fribidi")
    pisitools.dosed("ksvg/impl/libs/libtext2path/src/Converter.cpp", "fribidi_types.h", "fribidi-types.h")
    pisitools.dosed("ksvg/plugin/backends/Makefile.am", "agg", "") #disable agg backend, TODO: KSVG AGG backend needs to be ported to new AGG

    kde.configure("--with-poppler \
                   --with-kamera")

def build():
    kde.make()

def install():
    kde.install()

    # DO_NOT_COMPILE doesn't cover docs
    pisitools.removeDir("/usr/kde/3.5/share/doc/HTML/en/kpovmodeler/")
    pisitools.removeDir("/usr/kde/3.5/share/doc/HTML/en/kview/")
