#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ntp-%s" % get.srcVERSION().replace("_", "")

def setup():
    shelltools.export("CFLAGS", "%s -pie -fPIE -fno-strict-aliasing" % get.CFLAGS())

    # needed to link with avahi
    shelltools.export("ac_cv_header_dns_sd_h", "yes")
    shelltools.export("ac_cv_lib_dns_sd_DNSServiceRegister", "yes")

    autotools.configure("--enable-all-clocks \
                         --enable-parse-clocks \
                         --enable-linuxcaps \
                         --enable-ipv6 \
                         --with-crypto")

def build():
    autotools.make()

    shelltools.cd("html")
    shelltools.system("../scripts/html2man")
    shelltools.system("../fix-man-pages")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove autotools installed man pages
    pisitools.removeDir("/usr/share/man")

    pisitools.doman("html/man/man5/*.5", "html/man/man8/*.8")


    for sbin in ["sntp", "ntpdc", "ntpd", "ntp-keygen", "ntp-wait",
                 "ntpq", "ntptime", "ntptrace", "tickadj", "ntpsnmpd", "ntpdate"]:
        pisitools.domove("/usr/bin/%s" % sbin, "/usr/sbin")

    pisitools.dodir("/var/lib/ntp")

    pisitools.removeDir("/usr/lib")
    pisitools.removeDir("/usr/bin")

    pisitools.dohtml("html/*")
    pisitools.dodoc("ChangeLog", "NEWS", "README", "TODO", "WHERE-TO-START")
