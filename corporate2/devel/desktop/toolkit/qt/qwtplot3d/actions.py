#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="qwtplot3d"

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make()
    shelltools.cd("doc")
    shelltools.system("doxygen Doxyfile.doxygen")

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "examples")
    pisitools.dohtml("doc/web/doxygen/*")

    pisitools.dodoc("COPYING")
