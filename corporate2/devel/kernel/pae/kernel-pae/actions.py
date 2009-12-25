#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "linux-2.6.31"
NoStrip = ["/"]

def setup():
    kerneltools.configure()

    # Enable PAE and update kernel configuration
    pisitools.dosed(".config", "CONFIG_HIGHMEM64G is not set", "CONFIG_HIGHMEM4G is not set")
    pisitools.dosed(".config", "CONFIG_HIGHMEM4G=y", "CONFIG_HIGHMEM64G=y")
    #kerneltools.updateKConfig()
    shelltools.system('yes "" | make oldconfig')

def build():
    kerneltools.build(debugSymbols=False)

def install():
    #kerneltools.install(installFirmwares=False)
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

    # Clean module-init-tools related stuff
    kerneltools.cleanModuleFiles()
