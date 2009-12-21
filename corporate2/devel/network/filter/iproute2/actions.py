#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="iproute2-2.6.29-1"

def setup():
    pisitools.dosed("Makefile", "-O2", get.CFLAGS())
    pisitools.dosed("tc/m_ipt.c", "/usr/local", "/usr")

    autotools.configure()

def build():
    autotools.make('CC="%s"' % get.CC())

def install():
    autotools.rawInstall("DESTDIR=\"%s\" \
                          SBINDIR=/sbin \
                          DOCDIR=/%s/%s \
                          MANDIR=/usr/share/man \
                          " % (get.installDIR(), get.docDIR(), get.srcNAME()))

    pisitools.dodir("/usr/sbin")
    pisitools.dodir("/var/lib/arpd")
    pisitools.domove("/sbin/arpd", "/usr/sbin/")
