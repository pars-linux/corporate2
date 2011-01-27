#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
NoStrip = ["/"]

def install():
    for data in ["avatars", "lang", "sounds"]:
        pisitools.insinto("/usr/share/skype", data)

    pisitools.dobin("skype")
    pisitools.rename("/usr/bin/skype", "skype.bin")

    # Dbus config
    pisitools.insinto("/etc/dbus-1/system.d", "skype.conf")

    for size in ("16", "32", "48"):
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (size, size),
                          "icons/SkypeBlue_%sx%s.png" % (size, size),
                          "skype.png")

    pisitools.dodoc("README", "LICENSE")
