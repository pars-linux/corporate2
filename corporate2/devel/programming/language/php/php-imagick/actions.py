#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

shelltools.export("HOME", "%s" % get.installDIR())

def setup():
    shelltools.system("phpize")
    autotools.autoconf("-f -i")
    autotools.configure("--enable-shared \
                         --with-imagick")

    flagorderrx = (r"(\\\$libobjs \\\$deplibs) (\\\$compiler_flags)", r"\2 \1")
    pisitools.dosed("libtool", *flagorderrx)

def build():
    autotools.make()

def check():
    autotools.make("test")

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
