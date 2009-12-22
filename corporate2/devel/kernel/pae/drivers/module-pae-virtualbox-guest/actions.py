# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "."
KDIR = kerneltools.getKernelVersion()

def build():
    modules = ("vboxguest", "vboxvfs", "vboxvideo")
    for module in modules:
        if module != "vboxguest":
            shelltools.copy("vboxguest/Module.symvers", module)
        autotools.make("-C %s KERN_DIR=/lib/modules/%s/build" % (module, KDIR))

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "*/*.ko")
