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
Target = get.ARCH().replace("i686", "x86")
XDir = "x750" + ("_64a" if Target == "x86_64" else "")


def setup():
    shelltools.export("SETUP_NOCHECK", "1")
    shelltools.system("sh ati-driver-installer-%s-x86.x86_64.run --extract ." % get.srcVERSION().replace(".", "-"))

    shelltools.sym("../../../../../arch/%s/lib/modules/fglrx/build_mod/libfglrx_ip.a.GCC4" % Target, "%s/libfglrx_ip.a.GCC4" % BuildDir)

    pisitools.dosed("%s/make.sh" % BuildDir, r"^linuxincludes=.*", "linuxincludes=/lib/modules/%s/build/include" % KDIR)
    pisitools.dosed("%s/make.sh" % BuildDir, r"^uname_r=.*", "uname_r=%s" % KDIR)
    pisitools.dosed("%s/2.6.x/Makefile" % BuildDir, r"^(GCC_VER_MAJ *=).*$", r"\1 4")
    pisitools.dosed("common/etc/ati/authatieventsd.sh", "/var/lib/xdm/authdir/authfiles", "/var/run/xauth")

def build():
    shelltools.cd(BuildDir)
    shelltools.system("sh make.sh")

def install():
    pisitools.dobin("arch/%s/usr/X11R6/bin/*" % Target)
    pisitools.dobin("common/usr/X11R6/bin/*")
    pisitools.dosbin("arch/%s/usr/sbin/*" % Target)
    pisitools.dosbin("common/usr/sbin/*")

    DIRS = {
            "common/usr/share/doc/fglrx/examples/etc/acpi/events":  "/etc/acpi",
            "common/etc":                           "/",
            "common/usr/X11R6/include":             "/usr",
            "arch/%s/usr/X11R6/lib*/*" % Target:    "/usr/lib",
            "arch/%s/usr/lib*/*" % Target:          "/usr/lib",
            "common/usr/include/GL/":               "/usr/lib/xorg/fglrx/include",
            "common/usr/share":                     "/usr"
            }

    for source, target in DIRS.items():
        pisitools.insinto(target, source)

    pisitools.domove("/usr/lib/modules", "/usr/lib/xorg")
    pisitools.insinto("/usr/lib/xorg/modules", "%s/usr/X11R6/lib*/modules/*" % XDir)

    pisitools.domove("/usr/lib/libGL.so.1.2", "/usr/lib/xorg/fglrx/lib")
    pisitools.domove("/usr/lib/xorg/modules/extensions", "/usr/lib/xorg/fglrx")

    pisitools.dosym("libatiuki.so.1.0", "/usr/lib/libatiuki.so.1")
    pisitools.dosym("libatiuki.so.1", "/usr/lib/libatiuki.so")

    pisitools.dosym("libfglrx_dm.so.1.0", "/usr/lib/libfglrx_dm.so.1")
    pisitools.dosym("libfglrx_dm.so.1", "/usr/lib/libfglrx_dm.so")

    pisitools.dosym("libfglrx_gamma.so.1.0", "/usr/lib/libfglrx_gamma.so.1")
    pisitools.dosym("libfglrx_gamma.so.1", "/usr/lib/libfglrx_gamma.so")

    pisitools.dosym("libAMDXvBA.so.1.0", "/usr/lib/libAMDXvBA.so.1")
    pisitools.dosym("libAMDXvBA.so.1", "/usr/lib/libAMDXvBA.so")

    pisitools.dosym("libXvBAW.so.1.0", "/usr/lib/libXvBAW.so.1")
    pisitools.dosym("libXvBAW.so.1", "/usr/lib/libXvBAW.so")

    # compatibility links
    pisitools.dosym("/usr", "/usr/X11R6")
    pisitools.dosym("xorg/modules", "/usr/lib/modules")

    # copy compiled kernel module
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "common/lib/modules/fglrx/fglrx.%s.ko" % KDIR, "fglrx.ko")

    # remove static libs
    pisitools.remove("/usr/lib/*.a")
    if shelltools.isFile("/usr/lib/xorg/modules/esut.a"):
        pisitools.remove("/usr/lib/xorg/modules/esut.a")

    # not needed as xdg-utils package provides xdg-su
    pisitools.remove("/usr/bin/amdxdg-su")

    pisitools.domove("/usr/share/icons/ccc_large.xpm", "/usr/share/pixmaps", "amdcccle.xpm")
    pisitools.removeDir("/usr/share/icons")

    # Fix file permissions
    exec_file_suffixes = (".sh", ".so")
    exec_dir_suffixes = ("/bin", "/sbin", "/lib")

    import os
    for root, dirs, files in os.walk(get.installDIR()):
        for name in files:
            filePath = os.path.join(root, name)
            if root.endswith(exec_dir_suffixes) \
                or name.endswith(exec_file_suffixes):
                shelltools.chmod(filePath, 0755)
            else:
                shelltools.chmod(filePath, 0644)
