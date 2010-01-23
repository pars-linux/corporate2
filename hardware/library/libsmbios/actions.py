#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-doxygen \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/include", "src/include/smbios")

    # Symlink to /usr/sbin/DellWirelessCtl for the new HAL
    pisitools.dosym("/usr/sbin/smbios-wireless-ctl", "/usr/sbin/DellWirelessCtl")

    # Remove yum specific stuff
    pisitools.remove("/etc/yum/pluginconf.d/dellsysidplugin2.conf")
    pisitools.remove("/usr/lib/yum-plugins/dellsysidplugin2.py")
    pisitools.removeDir("/etc/yum")
    pisitools.removeDir("/usr/lib/yum-plugins")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
