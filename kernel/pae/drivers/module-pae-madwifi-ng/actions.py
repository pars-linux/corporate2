#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "madwifi-%s" % get.srcVERSION()
WorkDir = "madwifi-hal-0.10.5.6-r3835"

def setup():
    for dir in ["ath", "ath_hal", "net80211", "ath_rate/amrr", "ath_rate/onoe", "ath_rate/sample"]:
        pisitools.dosed("%s/Makefile" % dir, "SUBDIRS=", "M=")

    pisitools.dosed("Makefile.inc", "-Werror", "")
    pisitools.dosed("tools/Makefile", "CFLAGS=", "CFLAGS+=")
    pisitools.dosed("tools/Makefile", "LDFLAGS=", "LDFLAGS+=")

def build():
    shelltools.export("KERNELPATH", "/usr/src/linux")
    shelltools.export("TARGET", "i386-elf")
    shelltools.export("TOOLPREFIX", "/usr/bin/")
    shelltools.export("KERNELRELEASE", get.curKERNEL())

    autotools.make("all")

def install():
    autotools.rawInstall("DESTDIR=%s KMODPATH=/lib/modules/%s/extra  BINDIR=/usr/bin MANDIR=/usr/share/man" % (get.installDIR(), get.curKERNEL()))
    pisitools.domove("/usr/bin/wlanconfig", "/sbin")

    pisitools.dodoc("README", "COPYRIGHT", "docs/users-guide.pdf", "docs/WEP-HOWTO.txt")

    # install headers for use by wpa_supplicant and hostapd
    pisitools.insinto("/usr/include/madwifi/include/","include/*.h")
    pisitools.insinto("/usr/include/madwifi/net80211", "net80211/*.h")

