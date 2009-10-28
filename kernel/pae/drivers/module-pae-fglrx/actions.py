#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt


from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

KDIR = kerneltools.getKernelVersion()
NoStrip = ["/lib/modules/"]
WorkDir = "."

BuildDir = "common/lib/modules/fglrx/build_mod"

def setup():
    shelltools.export("SETUP_NOCHECK", "1")
    shelltools.system("sh ati-driver-installer-%s-x86.x86_64.run --extract ." % get.srcVERSION().replace(".", "-"))

    shelltools.sym("../../../../../arch/x86/lib/modules/fglrx/build_mod/libfglrx_ip.a.GCC4", "%s/libfglrx_ip.a.GCC4" % BuildDir)

    pisitools.dosed("%s/make.sh" % BuildDir, r"^linuxincludes=.*", "linuxincludes=/lib/modules/%s/build/include" % KDIR)
    pisitools.dosed("%s/make.sh" % BuildDir, r"^uname_r=.*", "uname_r=%s" % KDIR)
    pisitools.dosed("%s/2.6.x/Makefile" % BuildDir, r"^(GCC_VER_MAJ *=).*$", r"\1 4")

def build():
    shelltools.cd(BuildDir)
    shelltools.system("sh make.sh")

def install():
    # copy compiled kernel module
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "common/lib/modules/fglrx/fglrx.%s.ko" % KDIR, "fglrx.ko")
