#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "linux-2.6.32"
NoStrip = ["/"]

def setup():
    shelltools.copy("configs/kernel-%s-config" % get.ARCH(), ".config")
    kerneltools.configure()

    # Enable PAE and update kernel configuration
    pisitools.dosed(".config", "CONFIG_HIGHMEM64G is not set", "CONFIG_HIGHMEM4G is not set")
    pisitools.dosed(".config", "CONFIG_HIGHMEM4G=y", "CONFIG_HIGHMEM64G=y")

    kerneltools.updateKConfig()

def build():
    kerneltools.build(debugSymbols=False)

def install():
    kerneltools.install(installFirmwares=False)

    # Dump kernel version into /etc/kernel/
    kerneltools.dumpVersion()

    # Install kernel headers needed for out-of-tree module compilation
    # You can provide a list of extra directories from which to grab *.h files.
    kerneltools.installHeaders(extra=["drivers/media/dvb/dvb-core",
                                      "drivers/media/dvb/frontends",
                                      "drivers/media/video"])

    # Create source symlink in /lib/modules
    kerneltools.installSource(onlySymlink=True)

    # Clean module-init-tools related stuff
    kerneltools.cleanModuleFiles()
