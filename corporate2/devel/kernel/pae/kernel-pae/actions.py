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

NoStrip = ["/lib", "/boot"]

# NOTE: Bump this on ABI/Config changes
abiVersion = "150"

def setup():
    kerneltools.configure(abiVersion)

    # Enable PAE and update kernel configuration
    pisitools.dosed(".config", "CONFIG_HIGHMEM64G is not set", "CONFIG_HIGHMEM4G is not set")
    pisitools.dosed(".config", "CONFIG_HIGHMEM4G=y", "CONFIG_HIGHMEM64G=y")

    kerneltools.updateKConfig()

def build():
    kerneltools.build(debugSymbols=False)

def install():
    kerneltools.install()

    # Install kernel headers needed for out-of-tree module compilation
    kerneltools.installHeaders()

    # Create source symlink in /lib/modules
    kerneltools.installSource(onlySymlink=True)

    # Generate some module lists to use within mkinitramfs
    shelltools.system("./generate-module-list %s/lib/modules/%s" % (get.installDIR(), kerneltools.__getSuffix()))

    # Build and install the new 'perf' tool
    # When bumping major version build man files and put them into files/man
    autotools.make("V=1 -C tools/perf perf LDFLAGS='%s'" % get.LDFLAGS())
    pisitools.insinto("/usr/bin", "tools/perf/perf", "perf.%s-%s" % (get.srcNAME(), get.srcVERSION()))
