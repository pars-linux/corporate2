#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "QScintilla-gpl-%s" % get.srcVERSION()
NoStrip = ["/usr/share/doc"]
Qt4DIR = "usr/qt/4"
qmake = "qmake-qt4"

def setup():
    shelltools.cd("Qt4/")
    shelltools.system("%s -o Makefile qscintilla.pro" % qmake)

    # Change C/XXFLAGS
    pisitools.dosed("Makefile", "^CFLAGS.*\\$\\(DEFINES\\)", "CFLAGS   = %s -fPIC $(DEFINES)" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS.*\\$\\(DEFINES\\)", "CXXFLAGS   = %s -fPIC $(DEFINES)" % get.CXXFLAGS())

    # Get designer plugin's Makefile
    shelltools.cd("../designer-Qt4/")
    shelltools.system("%s -o Makefile designer.pro" % qmake)

    # Change C/XXFLAGS of designer plugin's makefile
    pisitools.dosed("Makefile", "^CFLAGS.*\\$\\(DEFINES\\)", "CFLAGS   = %s -fPIC $(DEFINES)" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS.*\\$\\(DEFINES\\)", "CXXFLAGS   = %s -fPIC $(DEFINES)" % get.CXXFLAGS())
    pisitools.dosed("Makefile", "\\$\\(SUBLIBS\\)  -L/usr/qt/4/lib", "$(SUBLIBS)")

def build():
    shelltools.cd("Qt4/")
    autotools.make("all staticlib CC=\"%s\" CXX=\"%s\" LINK=\"%s\"" % (get.CC(), get.CXX(), get.CXX()))

    shelltools.cd("../designer-Qt4/")
    autotools.make("DESTDIR=\"%s/%s/plugins/designer\"" % (get.installDIR(), Qt4DIR))

    # Get Makefile of qscintilla-python via sip
    shelltools.cd("../Python")
    pythonmodules.run("configure.py -p 4 -n ../Qt4 -o ../Qt4")
    autotools.make()

def install():
    # installs not managed by the build system
    shelltools.cd("Qt4/")
    pisitools.insinto("/%s/lib" % Qt4DIR, "libqscintilla2.so*")
    shelltools.makedirs("%s/%s/include" % (get.installDIR(), Qt4DIR))
    shelltools.copytree("Qsci", "%s/%s/include/Qsci" % (get.installDIR(), Qt4DIR))
    pisitools.insinto("%s/translations" % Qt4DIR, "qscintilla*.qm")

    shelltools.cd("../")
    pisitools.insinto("%s/plugins/designer" % Qt4DIR, "designer-Qt4/libqscintillaplugin.so")

    #build and install qscintilla-python
    shelltools.cd("Python")
    autotools.install("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dohtml("doc/html-Qt4/")
    pisitools.insinto("/usr/share/doc/%s/Scintilla" % get.srcNAME(), "doc/Scintilla/*")

    pisitools.dodoc("GPL*", "LICENSE*", "NEWS", "README", "OPENSOURCE-NOTICE.TXT")
