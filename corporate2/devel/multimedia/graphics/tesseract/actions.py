#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

    # java install is broken, see http://code.google.com/p/tesseract-ocr/issues/detail?id=108
    pisitools.dosed("Makefile", "dlltest java", "dlltest")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # No development stuff
    pisitools.removeDir("/usr/include")
    pisitools.removeDir("/usr/lib")

    pisitools.dodoc("COPYING", "README", "ChangeLog", "AUTHORS")
