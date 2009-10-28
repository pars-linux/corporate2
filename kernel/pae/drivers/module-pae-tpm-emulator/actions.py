#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="tpm_emulator-0.5.1"

def build():
    autotools.make("-j1")

def install():
    # create needed directory
    pisitools.dodir("/etc/udev/rules.d")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
