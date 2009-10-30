#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir="%s-%s" % (get.srcNAME(), get.srcVERSION().replace("0.0_", ""))

def setup():
    pisitools.dosed("Makefile", '^CFLAGS\?=.*', "CFLAGS=-std=c99 %s" % get.CFLAGS())
    pisitools.dosed("Makefile", '^LDFLAGS\+=.*', "LDFLAGS=$(LIBS) %s" % get.LDFLAGS())

    pisitools.dosed("Makefile", '-L/usr/local/lib', "-L/usr/lib")
    pisitools.dosed("Makefile", '-I/usr/local/include', "-I/usr/include")

def build():
    autotools.make()

def install():
    docDir = os.path.join(get.docDIR(), get.srcNAME())

    pisitools.dobin("xdotool")
    pisitools.doman("xdotool.1")

    pisitools.dodoc("CHANGELIST", "COPYRIGHT", "README")
    pisitools.insinto(docDir, "examples")
