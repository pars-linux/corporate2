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

    # Symlinks
    mapping = {"button_cancel.png": "actions/cancel.png",
               "kmenu.png": "apps/panel.png",
               "kmenu.png": "apps/panel_settings.png"}

    for size in (16, 22, 32, 48, 64, 128):
        for k in mapping.keys():
            try:
                pisitools.dosym(k, "usr/share/icons/BCTango/%dx%d/%s" % (size, size, mapping[k]))
            except:
                pass
