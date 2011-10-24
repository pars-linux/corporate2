#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "tzdata"
tzcode  = "tzcode2011i"
tzdata  = "tzdata2011l"

# Switch to POSIX locale
shelltools.export("LANG", "POSIX")
shelltools.export("LC_ALL", "POSIX")
shelltools.export("LANGUAGE", "POSIX")

def setup():
    pisitools.dosed("config.mk", "@@INSTALL_ROOT@@", get.installDIR())
    pisitools.dosed("config.mk", "@@CFLAGS@@", get.CFLAGS())
    pisitools.dosed("config.mk", "@@OBJDIR@@", "%s/%s/obj/" % (get.workDIR(), WorkDir))
    shelltools.sym("Makeconfig.in", "Makeconfig")

def build():
    autotools.make()

def install():
    autotools.rawInstall()

    for doc in ["README", "Theory", "tz-link.htm"]:
        pisitools.dodoc("%s/%s" % (tzcode, doc))

    print "====================TESTING========================="
    autotools.make("check")
    print "====================TESTING END====================="

    # Create Timezone db in /usr/share/zoneinfo
    shelltools.system("./dump-tz-db %s" % get.installDIR())

