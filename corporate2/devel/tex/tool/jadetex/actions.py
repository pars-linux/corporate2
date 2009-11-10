#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed('Makefile','tex -ini','latex -ini')

def build():
    shelltools.export("VARTEXFONTS", "%s/fonts" % get.curDIR())
    autotools.make()

def install():
    shelltools.export("VARTEXFONTS", "%s/fonts" % get.curDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/bin/latex", "/usr/bin/jadetex")
    pisitools.dosym("/usr/bin/pdftex", "/usr/bin/pdfjadetex")

    pisitools.dodoc("ChangeLog*")
    pisitools.doman("*.1")
