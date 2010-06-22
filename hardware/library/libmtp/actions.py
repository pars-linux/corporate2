#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static \
                         --program-prefix=mtp-")

def build():
    autotools.make()

def install():
    autotools.install()

    # Install HAL file for portable audio players
    pisitools.insinto("/usr/share/hal/fdi/information/10freedesktop", "libmtp.fdi", "10-usb-music-players-libmtp.fdi")

    # Regenerate udev rules without MODE= property
    shelltools.system('examples/hotplug -a\'SYMLINK+="libmtp-%k", ENV{ACL_MANAGE}="1"\' > libmtp.rules')

    # Install UDEV rules
    pisitools.insinto("/lib/udev/rules.d/", "libmtp.rules", "60-mtp.rules")

    pisitools.removeDir("/usr/share/doc/libmtp-*")

    pisitools.dodoc("ChangeLog", "COPYING", "README", "AUTHORS", "TODO")
