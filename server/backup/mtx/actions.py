#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

contrib = "%s/%s/contrib" % (get.docDIR(), get.srcNAME())

def setup():
    for f in ["config_sgen_solaris.sh", "mtx-changer"]:
        shelltools.chmod("contrib/%s" % f, 644)

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES", "COMPATABILITY", "FAQ", "LICENSE*", \
                    "README*", "TODO", "mtx.doc", "mtxl.README.html")

    pisitools.insinto(contrib, "contrib/*")
