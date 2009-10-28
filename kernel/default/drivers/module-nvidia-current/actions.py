#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "NVIDIA-Linux-x86-%s" % get.srcVERSION()
KDIR = kerneltools.getKernelVersion()
NoStrip = ["/lib/modules"]

driver = "nvidia-current"
base = "/usr/lib/xorg/%s" % driver

def setup():
    # Remove VDPAU headers and wrapper library
    shelltools.unlinkDir("usr/include/vdpau")
    shelltools.unlink("usr/lib/libvdpau.so.%s" % get.srcVERSION())
    shelltools.unlink("usr/lib/libvdpau_trace.so.%s" % get.srcVERSION())

def build():
    shelltools.export("SYSSRC", "/lib/modules/%s/build" % KDIR)
    shelltools.cd("usr/src/nv")

    autotools.make("module")

def install():
    # Kernel driver
    pisitools.insinto("/lib/modules/%s/extra/nvidia" % KDIR, "usr/src/nv/nvidia.ko", "%s.ko" % driver)

    # Command line tools and their man pages
    pisitools.dobin("usr/bin/*")
    pisitools.doman("usr/share/man/*/*")

    # Libraries and X modules
    pisitools.insinto("%s/lib" % base, "usr/X11R6/lib/*")
    pisitools.insinto("%s/lib" % base, "usr/lib/*")
    pisitools.domove("%s/lib/modules/*" % base, base)
    pisitools.removeDir("%s/lib/modules" % base)

    # Headers
    pisitools.insinto(base, "usr/include")

    # Our libc is TLS enabled so use TLS library
    pisitools.remove("%s/lib/libnvidia-tls.so.*" % base)

    # xorg-server provides libwfb.so
    pisitools.remove("%s/libnvidia-wfb.so.*" % base)

    # Documentation
    pisitools.dodoc("usr/share/doc/[!h]*", destDir="xorg-video-%s" % driver)
    pisitools.dohtml("usr/share/doc/html/*", destDir="xorg-video-%s" % driver)
