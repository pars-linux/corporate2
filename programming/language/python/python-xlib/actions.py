#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get


examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())
utils = "%s/%s/utils" % (get.docDIR(), get.srcNAME())

def setup():
    shelltools.chmod("examples/*", 0644)
    shelltools.chmod("utils/*", 0644)

def build():
    pythonmodules.compile()

    # we need texi to create ps
    # for d in ["doc/html", "doc/info", "doc/ps"]:
    for d in ["doc/html", "doc/info"]:
        shelltools.cd(d)
        autotools.make()
        shelltools.cd("../..")

def install():
    pythonmodules.install()

    pisitools.dohtml("doc/html/")
    pisitools.dodoc("TODO", "COPYING", "NEWS", "README")
    pisitools.doinfo("doc/info/*.info*")

    pisitools.insinto(examples, "examples/*")
    pisitools.insinto(utils, "utils/*")

    pythonmodules.fixCompiledPy()
