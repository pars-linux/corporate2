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
    mapping = { "lock.png" : ["actions/object-locked.png"],
                "systemsettings.png": ["apps/multimedia-volume-control.png"],
                "printer.png": ["devices/printer-printing.png"],
                "button_cancel.png": ["actions/no.png", "actions/cancel.png"],
                "kmenu.png": ["apps/panel.png", "apps/panel_settings.png"],
                "mail_replyall.png": ["actions/mail-reply-all.png"],
                "mail_reply.png": ["actions/mail-reply.png"],
                }

    for size in (16, 22, 32, 48, 64, 128):
        for k,values in mapping.items():
            for icon in values:
                try:
                    pisitools.dosym(k, "usr/share/icons/BCTango/%dx%d/%s" % (size, size, icon))
                except:
                    pass
