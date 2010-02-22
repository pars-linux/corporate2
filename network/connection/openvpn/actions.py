#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# this package needs a lot of work for init scripts etc.
def setup():
    autotools.configure("--enable-pthread \
                         --enable-ssl \
                         --enable-iproute2 \
                         --enable-crypto")

def build():
    autotools.make()

    for dir in ["plugin/auth-pam", "plugin/down-root", "easy-rsa/2.0"]:
        shelltools.cd(dir)
        autotools.make()
        shelltools.cd("../..")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("easy-rsa/2.0")
    autotools.rawInstall("DESTDIR=%s/usr/share/easy-rsa" % get.installDIR())
    shelltools.cd("../..")

    for val in ["auth-pam", "down-root"]:
        pisitools.dolib_so("plugin/%s/openvpn-%s.so" % (val, val))

    for val in ["contrib", "sample-config-files", "sample-keys", "sample-scripts"]:
        pisitools.insinto("/%s/openvpn/%s" % (get.dataDIR(), val), "%s/*" % val)

    pisitools.dodir("/etc/openvpn")
    pisitools.dodoc("AUTHORS", "COPYING", "COPYRIGHT.GPL", "ChangeLog", "README")

