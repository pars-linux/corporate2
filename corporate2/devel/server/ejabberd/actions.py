#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.cd("src")
    autotools.configure("--enable-pam")

def build():
    shelltools.cd("src")
    autotools.make("-j1")

def install():
    # ejabberdctl
    #pisitools.insinto("/usr/sbin", "tools/*")

    # mnesia path
    pisitools.dodir("/var/lib/ejabberd/db")
    pisitools.dodir("/etc/ejabberd")

    shelltools.cd("src")
    # NOTE: Don't forget to update service.py with new versions...
    destdir = get.installDIR()
    ejabberddir = "%s/usr/lib/ejabberd/" % destdir
    etcdir = "%s/etc/ejabberd/" % destdir
    logdir = "%s/var/log/ejabberd/" % destdir
    autotools.rawInstall("DESTDIR=%s EJABBERDDIR=%s ETCDIR=%s LOGDIR=%s" % (
            destdir,
            ejabberddir,
            etcdir,
            logdir))

    pisitools.dosed("%s/etc/ejabberd/ejabberd.cfg" % get.installDIR(),
                    "/path/to/ssl.pem",
                    "/etc/ejabberd/ssl.pem")
    shelltools.cd("../")
    pisitools.dodoc("ChangeLog", "COPYING")
