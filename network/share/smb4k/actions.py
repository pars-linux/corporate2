#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

KeepSpecial = ["libtool"]

def setup():
    # Fix automake and python detection
    pisitools.dosed("admin/cvs.sh", "automake\*1\.10\*", "automake*1.1[0-5]*")
    pisitools.dosed("admin/acinclude.m4.in", "KDE_CHECK_PYTHON_INTERN\(\"2.5", "KDE_CHECK_PYTHON_INTERN(\"%s" % get.curPYTHON().split("python")[1])

    kde.make("-f admin/Makefile.common")
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    # Fix #3460
    shelltools.chmod("%s/usr/kde/3.5/bin/smb4k_mount" % get.installDIR(), 04755)
    shelltools.chmod("%s/usr/kde/3.5/bin/smb4k_umount" % get.installDIR(), 04755)
