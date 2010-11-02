#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

KeepSpecial=["perl"]

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s htmldir=/usr/share/doc/%s/html" % (get.installDIR(), get.srcNAME()))

    for util in ("dvi", "html", "pdf", "ps", "rtf"):
        pisitools.dosym("docbook2%s" % util, "/usr/bin/db2%s" % util)
        pisitools.dosym("jw.1", "/usr/share/man/man1/db2%s.1" % util)
    pisitools.dosym("jw.1", "/usr/share/man/man1/docbook2txt.1")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
