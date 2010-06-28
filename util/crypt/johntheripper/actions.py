#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "john-%s" % get.srcVERSION()

arch = "linux-x86-64" if get.ARCH() == "x86_64" else "linux-x86-sse2"

conf = {"CC": get.CC(),
        "CXX": get.CXX(),
        "CFLAGS": "%s -fno-PIC -fno-PIE" % get.CFLAGS(),
        "LDFLAGS": "%s -nopie" % get.LDFLAGS(),
        "ARCH": arch}

def build():
    shelltools.cd("src")
    autotools.make('CPP=%(CXX)s \
                    CC=%(CC)s \
                    AS=%(CC)s \
                    LD=%(CC)s \
                    CFLAGS="-c -Wall %(CFLAGS)s -DJOHN_SYSTEMWIDE -DJOHN_SYSTEMWIDE_HOME=\\\"\\\\\\\"/etc/john\\\\\\\"\\\"" \
                    LDFLAGS="%(LDFLAGS)s" \
                    OPT_NORMAL="" \
                    %(ARCH)s' % conf)

def install():
    pisitools.dosbin("run/john")
    pisitools.insinto("/usr/sbin", "run/mailer", "john-mailer")

    for f in ["unafs", "unique", "unshadow", "undrop"]:
        pisitools.dosym("john", "/usr/sbin/%s" % f)

    for f in ["john.conf", "password.lst", "*chr", "netscreen.py", "sap_prepare.pl"]:
        pisitools.insinto("/etc/john", "run/%s" % f)

    pisitools.dodoc("doc/*")
