#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "QScintilla1-1.71-gpl-1.7"

def setup():
    shelltools.cd("qt/")

    pisitools.dosed("qscintilla.pro", "DESTDIR = \$\(QTDIR\)/lib", "DESTDIR = %s/%s/lib" % (get.installDIR(), get.qtDIR()))
    shelltools.system("qmake -o Makefile qscintilla.pro")

def install():
    pisitools.dodoc("ChangeLog", "LICENSE", "NEWS", "README")

    # execute install target of build system
    shelltools.cd("qt/")
    autotools.make("-j1 all staticlib") # there is only an install target foolish qmake

    # installs not managed by the build system
    pisitools.insinto("%s/include" % get.qtDIR(), "qextscintilla*.h")
    pisitools.insinto("%s/translations" % get.qtDIR(), "qscintilla*.qm")

    shelltools.cd("../")
    pisitools.dohtml("doc/html/")
    pisitools.insinto("/usr/share/doc/%s/Scintilla" % get.srcTAG(), "doc/Scintilla/*")

    # No static libs
    pisitools.remove("/usr/qt/3/lib/libqscintilla.a")
