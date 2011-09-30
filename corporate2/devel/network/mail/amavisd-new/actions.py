#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def install():
    pisitools.insinto("/etc/amavis", "amavisd.conf", "amavisd.conf")

    pisitools.insinto("/usr/sbin", "amavisd")
    pisitools.insinto("/usr/sbin", "amavisd-agent")
    pisitools.insinto("/usr/sbin", "amavisd-nanny")
    pisitools.insinto("/usr/sbin", "amavisd-release")
    pisitools.insinto("/usr/sbin", "amavisd-snmp-subagent")
    shelltools.chmod("%s/usr/sbin/amavisd*" % get.installDIR())

    pisitools.dodir("/var/tmp/amavisd")
    pisitools.dodir("/var/db/amavisd")
    pisitools.dodir("/var/spool/amavis")
    pisitools.dodir("/var/run/amavisd")
    pisitools.dodir("/var/spool/amavis/virusmails")

    shelltools.chmod("%s/var/spool/amavis/virusmails" % get.installDIR(), 0750)

    pisitools.dodoc("README_FILES/README.*", "AAAREADME*", "LICENSE", "RELEASE_NOTES")
