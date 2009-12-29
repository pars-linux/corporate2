#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-shared \
                         --disable-static \
                         --without-rpm \
                         --with-sys-location=Unknown \
                         --with-sys-contact=root@Unknown \
                         --with-default-snmp-version=3 \
                         --with-logfile=/var/log/snmpd.log \
                         --with-persistent-directory=/var/lib/net-snmp \
                         --with-mib-modules='host agentx smux ucd-snmp/diskio disman/event disman/schedule tcp-mib udp-mib misc/ipfwacc' \
                         --enable-ipv6 \
                         --enable-ucd-snmp-compatibility \
                         --with-openssl \
                         --with-pic \
                         --enable-embedded-perl \
                         --with-libwrap \
                         --enable-as-needed \
                         --without-root-access \
                         --enable-mfd-rewrites \
                         --enable-local-smux")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc/snmp/", "EXAMPLE.conf", "snmpd.conf.example")

    pisitools.dodir("/var/lib/net-snmp")
    pisitools.dodir("/etc/snmp")

    pisitools.dodoc("AGENT.txt", "ChangeLog", "FAQ", "NEWS", "PORTING", "README*", "TODO")

