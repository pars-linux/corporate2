#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.cd("src")
    autotools.autoreconf("-fi")
    autotools.configure("--enable-plugin=../ppp-2.4.4")

def build():
    shelltools.cd("src")
    autotools.make()

def install():
    shelltools.cd("src")
    autotools.rawInstall("DESTDIR=\"%s\" docdir=/usr/share/doc/%s" % (get.installDIR(), get.srcNAME()))

    # Don't use compiled rp-pppoe plugin; use it from the current version of pppd
    pisitools.remove("/etc/ppp/plugins/rp-pppoe.so")
    pisitools.dosym("/usr/lib/pppd/2.4.4/rp-pppoe.so", "/etc/ppp/plugins/rp-pppoe.so")

    # Install symnlinks for easier usage
    for f in ["connect", "relay", "server", "setup", "sniff", "start", "status", "stop"]:
        pisitools.dosym("pppoe-%s" % f, "/usr/sbin/adsl-%s" % f)
