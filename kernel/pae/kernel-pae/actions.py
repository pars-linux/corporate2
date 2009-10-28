#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import pisitools

WorkDir = "linux-2.6.30"
NoStrip = ["/"]

def setup():
    kerneltools.configure()

def build():
    kerneltools.build(debugSymbols=False)

def install():
    kerneltools.install()

    # Ugly hack to remove the firmwares
    pisitools.removeDir("/lib/firmware")

    # Dump kernel version into /etc/kernel/
    kerneltools.dumpVersion()

    # Install kernel headers needed for out-of-tree module compilation
    # You can provide a list of extra directories from which to grab *.h files.
    kerneltools.installHeaders(extra=["drivers/media/dvb/dvb-core",
                                      "drivers/media/dvb/frontends",
                                      "drivers/media/video"])

    # kerneltools.installSource()

    kerneltools.cleanModuleFiles()
