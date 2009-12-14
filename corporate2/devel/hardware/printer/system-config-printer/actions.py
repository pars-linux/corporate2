#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")

    # Skip desktop-file-install's
    pisitools.dosed("Makefile.in", "desktop-file-install ", "/bin/true ")

    # Fix udev rules dir
    pisitools.dosed("Makefile.in", "@udevrulesdir = \$.*$", "@udevrulesdir = /lib/udev/rules.d")

    pisitools.dosed("Makefile.in", "xmlto man", "xmlto --skip-validation man")
    autotools.configure("--with-udev-rules")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/run/udev-configure-printer")

    pisitools.dodoc("README", "AUTHORS", "NEWS", "COPYING", "ChangeLog")
