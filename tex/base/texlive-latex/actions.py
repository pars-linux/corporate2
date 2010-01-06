#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import texlivemodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().split("_")[-1])

def build():
    texlivemodules.compile()

def install():
    texlivemodules.install()

    pisitools.remove("/var/lib/texmf/web2c/luatex/pdfluatex.log")
    pisitools.remove("/var/lib/texmf/web2c/pdftex/etex.log")
    pisitools.remove("/var/lib/texmf/web2c/luatex/lualatex.log")
    pisitools.remove("/var/lib/texmf/web2c/pdftex/pdftex.log")
    pisitools.remove("/var/lib/texmf/web2c/luatex/luatex.log")
    pisitools.remove("/var/lib/texmf/web2c/pdftex/latex.log")
    pisitools.remove("/var/lib/texmf/web2c/luatex/pdflualatex.log")
    pisitools.remove("/var/lib/texmf/web2c/pdftex/pdfetex.log")
    pisitools.remove("/var/lib/texmf/web2c/pdftex/pdflatex.log")
