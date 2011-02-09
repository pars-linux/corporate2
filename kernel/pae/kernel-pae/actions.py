#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = ["/lib", "/boot"]

def setup():
    kerneltools.configure()

    # Enable PAE and update kernel configuration
    # pisitools.dosed(".config", "CONFIG_HIGHMEM64G is not set", "CONFIG_HIGHMEM4G is not set")
    # pisitools.dosed(".config", "CONFIG_HIGHMEM4G=y", "CONFIG_HIGHMEM64G=y")
    # autotools.make("oldconfig")

def build():
    kerneltools.build(debugSymbols=False)

def install():
    kerneltools.install()

    # Install kernel headers needed for out-of-tree module compilation
    kerneltools.installHeaders()

    # Generate some module lists to use within mkinitramfs
    shelltools.system("./generate-module-list %s/lib/modules/%s" % (get.installDIR(), kerneltools.__getSuffix()))
