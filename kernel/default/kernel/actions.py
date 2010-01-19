#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "linux-2.6.32"
NoStrip = ["/"]

def setup():
    kerneltools.configure()

def build():
    kerneltools.build(debugSymbols=False)

def install():
    kerneltools.install()

    # Dump kernel version into /etc/kernel/
    kerneltools.dumpVersion()

    # Install kernel headers needed for out-of-tree module compilation
    # You can provide a list of extra directories from which to grab *.h files.
    kerneltools.installHeaders(extra=["drivers/media/dvb/dvb-core",
                                      "drivers/media/dvb/frontends",
                                      "drivers/media/video"])

    # Drop /usr/include/scsi directory as it's shipped within glibc
    kerneltools.installLibcHeaders(excludes=["scsi"])

    # Install kernel source
    kerneltools.installSource()

    # Clean module-init-tools related stuff
    kerneltools.cleanModuleFiles()

    # Build and install the new 'perf' tool
    autotools.make("V=1 -C tools/perf perf")
    pisitools.insinto("/usr/bin", "tools/perf/perf", "perf.%s-%s" % (get.srcNAME(), get.srcVERSION()))
    autotools.install("-C tools/perf/Documentation install-man mandir=%s/usr/share/man" % get.installDIR())
