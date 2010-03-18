#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--with-gui=openssl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.chmod("%s/etc/tcsd.conf" % get.installDIR(), 0600)
    """
    pisitools.insinto("/etc", "dist/tcsd.conf")
    pisitools.dobin("tools/ps_convert", "/usr/share/doc/%s/tools" % get.srcNAME())
    pisitools.dobin("tools/ps_inspect", "/usr/share/doc/%s/tools" % get.srcNAME())
    """

    pisitools.dodir("/var/lib/tpm")
    pisitools.chmod("%s/var/lib/tpm" % get.installDIR(), 0700)

    pisitools.dodoc("README", "AUTHORS", "ChangeLog", "NICETOHAVES", "TODO")
