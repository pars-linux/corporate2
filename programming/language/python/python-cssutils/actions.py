#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

WorkDir="%s-%s" % (get.srcNAME().split("python-")[1], get.srcVERSION().replace("_alph", ""))
examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def build():
    pythonmodules.compile()

def setup():
    shelltools.chmod("examples/*", 0644)


def install():
    pythonmodules.install()
    pisitools.insinto(examples, "examples/*")

    pisitools.removeDir("usr/lib/%s/site-packages/tests" % get.curPYTHON())

    pisitools.dodoc("docs/*.txt", "CHANGELOG.txt")
