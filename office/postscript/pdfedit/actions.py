#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

print get.docDIR()

def setup():
    autotools.configure("--enable-release \
                         --disable-doxygen-doc \
                         --docdir=/%s/%s" % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make("CXX=%s" % get.CXX())

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    for i in ("16", "32", "48", "64"):
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps/" % (i, i), "src/gui/icon/pdfedit_icon_%s.png" % i, "pdfedit.png")
