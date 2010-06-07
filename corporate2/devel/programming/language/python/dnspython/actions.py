#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def build():
    pythonmodules.compile()

def setup():
    shelltools.chmod("examples/*", 0644)

def install():
    pythonmodules.install()

    pisitools.insinto(examples, "examples/*")
    pisitools.dodoc("TODO")
