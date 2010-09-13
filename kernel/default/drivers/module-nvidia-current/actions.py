# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
KDIR = kerneltools.getKernelVersion()
NoStrip = ["/lib/modules"]

arch = get.ARCH().replace("i686", "x86")
driver = "nvidia-current"
base = "/usr/lib/xorg/%s" % driver

def setup():
    shelltools.system("sh NVIDIA-Linux-%s-%s.run -x --target tmp"
                      % (arch, get.srcVERSION()))
    shelltools.move("tmp/*", ".")

    # Our libc is TLS enabled so use TLS library
    shelltools.unlink("*-tls.so*")
    shelltools.move("tls/*", ".")

    # xorg-server provides libwfb.so
    shelltools.unlink("libnvidia-wfb.so.*")

    # Remove VDPAU headers and wrapper library
    shelltools.unlink("vdpau*.h")
    shelltools.unlink("libvdpau.so.%s" % get.srcVERSION())
    shelltools.unlink("libvdpau_trace.so.%s" % get.srcVERSION())

def build():
    shelltools.export("SYSSRC", "/lib/modules/%s/build" % KDIR)
    shelltools.cd("kernel")

    autotools.make("module")

def install():
    # Kernel driver
    pisitools.insinto("/lib/modules/%s/extra/nvidia" % KDIR,
                      "kernel/nvidia.ko", "%s.ko" % driver)

    # Command line tools and their man pages
    pisitools.dobin("nvidia-smi")
    pisitools.doman("nvidia-smi.1.gz")

    # Libraries and X modules
    for lib in ("GL", "OpenCL", "XvMCNVIDIA", "cuda", "nvidia"):
        pisitools.dolib("lib%s*.so*" % lib, "%s/lib" % base)

    pisitools.dolib("nvidia_drv.so", "%s/drivers" % base)
    pisitools.dolib("libglx.so*", "%s/extensions" % base)
    pisitools.dolib("libvdpau_nvidia.so*", "%s/lib/vdpau" % base)

    pisitools.insinto("/etc/OpenCL/vendors", "nvidia.icd")

    # Documentation
    docdir = "xorg-video-%s" % driver
    pisitools.dodoc("LICENSE", "NVIDIA_Changelog", "README.txt", destDir=docdir)
    pisitools.dohtml("html/*", destDir=docdir)
