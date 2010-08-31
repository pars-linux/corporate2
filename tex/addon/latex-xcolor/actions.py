#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir= "xcolor"

def build():
    shelltools.system("latex --interaction=batchmode ./xcolor.ins")

    texdocs = shelltools.ls("*.tex")
    texdocs.extend(shelltools.ls("*.dtx"))
    for texdoc in texdocs:
        print texdoc
        shelltools.system("texi2dvi -q -c --language=latex ./%s" % texdoc)

def install():
    dvidocs = []
    for i in ["dvi", "pdf"]:
        dvidocs.extend(shelltools.ls("*.%s" % i))
    for dvidoc in dvidocs:
        print dvidoc
        pisitools.dodoc(dvidoc)
        pisitools.dosym("/usr/share/doc/%s/%s" % (get.srcTAG(), dvidoc), "/usr/share/texmf/doc/latex/%s/%s" % (WorkDir, dvidoc))

    for stylesdoc in ["sty", "def"]:
        print stylesdoc
        pisitools.insinto("/usr/share/texmf/tex/latex/%s/" % WorkDir, "*.%s" %stylesdoc)

    pisitools.dodoc("ChangeLog", "README")
