#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "bctangokde"
docs = ["changelog", "credits", "links"]

def install():
    pisitools.dodir("/usr/share/icons/BCTango")

    shelltools.cd("..")
    shelltools.copytree("bctangokde", "%s/usr/share/icons/" % get.installDIR())
    shelltools.cd("bctangokde")

    for d in docs:
        pisitools.dodoc(d)
        pisitools.remove("/usr/share/icons/bctangokde/%s" % d)

    pisitools.rename("/usr/share/icons/bctangokde", "BCTango")
