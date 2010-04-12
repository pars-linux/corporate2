# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "VirtualBox-%s_OSE" % get.srcVERSION()

VBoxLibDir = "/usr/lib/virtualbox"
VBoxDataDir = "/usr/share/virtualbox"
XorgVersion = "17"

def setup():
    pisitools.dosed("LocalConfig.kmk", "__VBOXLIBDIR__", VBoxLibDir)
    pisitools.dosed("LocalConfig.kmk", "__VBOXDATADIR__", VBoxDataDir)

    shelltools.echo("vbox.cfg", "INSTALL_DIR=%s" % VBoxLibDir)

    # TODO: Enable web service when we have soapcpp2
    autotools.rawConfigure("--disable-kmods \
                            --enable-hardening \
                            --with-gcc=%s \
                            --with-g++=%s \
                            --with-qt-dir=/usr/qt/4" % (get.CC(), get.CXX()))

def build():
    shelltools.system("source env.sh && kmk")

def install():
    pisitools.insinto("/etc/vbox", "vbox.cfg")
    pisitools.insinto("/etc/X11/Xsession.d", "src/VBox/Additions/x11/Installer/98vboxadd-xclient", "98-vboxclient.sh")
    pisitools.insinto("/usr/bin", "src/VBox/Additions/x11/Installer/VBoxRandR.sh", "VBoxRandR")
    pisitools.insinto("/usr/share/X11/pci", "src/VBox/Additions/x11/Installer/vboxvideo.ids")
    pisitools.insinto("/usr/share/hal/fdi/policy/20thirdparty", "src/VBox/Additions/linux/installer/90-vboxguest.fdi")

    shelltools.cd("out/linux.x86/release/bin")

    exclude = ("additions", "nls", "sdk", "src", "SUP", "vboxkeyboard",
               "VBox.sh", "VBoxSysInfo.sh", "VBoxTunctl", "testcase", "tst", "xpidl")

    for _file in shelltools.ls("."):
        if _file.startswith(exclude):
            continue

        print "Installing %s ..." % _file
        pisitools.insinto(VBoxLibDir, _file)

    pisitools.dobin("VBoxTunctl")

    pisitools.dobin("VBox*.sh", VBoxDataDir)
    pisitools.insinto(VBoxDataDir, "nls")

    # Symlinks
    # TODO: Add vboxwebsrv when ready
    apps = ("VBoxHeadless", "VBoxManage", "VBoxSDL", "VBoxVRDP", "VirtualBox")
    for link in apps:
        pisitools.dosym("../share/virtualbox/VBox.sh", "/usr/bin/%s" % link)

    # Desktop file and icon
    pisitools.domove("%s/*.desktop" % VBoxLibDir, "/usr/share/applications")
    pisitools.domove("%s/*.png" % VBoxLibDir, "/usr/share/pixmaps")

    # Guest additions
    pisitools.dobin("additions/VBoxClient")
    pisitools.dobin("additions/VBoxControl")

    pisitools.dosbin("additions/VBoxService")
    pisitools.dosbin("additions/mount.vboxsf", "/sbin")

    pisitools.dolib("additions/VBoxOGL*")
    pisitools.dosym("../../../VBoxOGL.so", "/usr/lib/xorg/modules/dri/vboxvideo_dri.so")

    pisitools.insinto("/usr/lib/xorg/modules/drivers", "additions/vboxvideo_drv_%s.so" % XorgVersion, "vboxvideo_drv.so")
    pisitools.insinto("/usr/lib/xorg/modules/input",   "additions/vboxmouse_drv_%s.so" % XorgVersion, "vboxmouse_drv.so")

    # Python bindings
    pisitools.insinto("%s/sdk/bindings/xpcom" % VBoxLibDir, "sdk/bindings/xpcom/python")

    shelltools.cd("sdk/installer")
    shelltools.copy("vboxapisetup.py", "setup.py")
    shelltools.export("VBOX_INSTALL_PATH", VBoxLibDir)
    pythonmodules.install()
