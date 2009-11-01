#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pisitools.dosed("Makefile", "-Werror", "")
    autotools.make("INSTPREFIX=%s" % get.installDIR())

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/etc/acpi/actions")
    pisitools.dodir("/etc/acpi/events")

    autotools.rawInstall("INSTPREFIX=%s" % get.installDIR())

    pisitools.doman("acpid.8", "acpi_listen.8")

    pisitools.dodoc("Changelog", "README", "COPYING", "TODO")
