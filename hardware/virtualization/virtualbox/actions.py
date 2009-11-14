#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "VirtualBox-%s_OSE" % get.srcVERSION()

installDir = "/usr/lib/virtualbox"
XorgVersion = "16"

def setup():
    shelltools.makedirs("build")
    shelltools.sym("build/linux.x86/release/bin", "out")

    # TODO: Enable web service when we have soapcpp2
    autotools.rawConfigure("--disable-kmods \
                            --enable-hardening \
                            --with-gcc=%s \
                            --with-g++=%s \
                            --with-qt-dir=/usr/qt/4 \
                            --out-path=build" % (get.CC(), get.CXX()))

def build():
    shelltools.system("source build/env.sh && kmk")

def install():
    exclude = ("additions", "sdk", "src", "SUP", "testcase", "vboxkeyboard", "tst", "xpidl")

    for _file in shelltools.ls("out"):
        if _file.startswith(exclude):
            continue

        print "Installing %s ..." % _file
        pisitools.insinto(installDir, "out/%s" % _file)

    # Symlinks
    # TODO: Add vboxwebsrv when ready
    apps = ("VBoxHeadless", "VBoxManage", "VBoxSDL", "VBoxVRDP", "VirtualBox")
    relativeInstallDir = os.path.relpath(installDir, "/usr/bin")
    for link in apps:
        pisitools.dosym("%s/VBox.sh" % relativeInstallDir, "/usr/bin/%s" % link)

    pisitools.dosym("%s/VBoxTunctl" % relativeInstallDir, "/usr/bin/VBoxTunctl")

    # Configuration file
    pisitools.dodir("/etc/vbox")
    shelltools.echo("%s/etc/vbox/vbox.cfg" % get.installDIR(), "INSTALL_DIR=%s" % installDir)

    # Desktop file
    pisitools.domove("%s/*.desktop" % installDir, "/usr/share/applications")
    pisitools.domove("%s/*.png" % installDir, "/usr/share/pixmaps")

    # Guest additions
    pisitools.dobin("out/additions/VBoxClient")
    pisitools.dosbin("out/additions/VBoxControl")
    pisitools.dosbin("out/additions/VBoxService")

    pisitools.insinto("/sbin", "out/additions/mountvboxsf", "mount.vboxsf")

    pisitools.insinto("/etc/X11/Xsession.d", "src/VBox/Additions/x11/Installer/98vboxadd-xclient", "98-vboxclient.sh")
    pisitools.insinto("/usr/bin", "src/VBox/Additions/x11/Installer/VBoxRandR.sh", "VBoxRandR")

    pisitools.dolib("out/additions/VBoxOGL*")
    pisitools.dosym("../../../VBoxOGL.so", "/usr/lib/xorg/modules/dri/vboxvideo_dri.so")

    pisitools.insinto("/usr/share/X11/pci", "src/VBox/Additions/x11/Installer/vboxvideo.ids")
    pisitools.insinto("/usr/lib/xorg/modules/drivers", "out/additions/vboxvideo_drv_%s.so" % XorgVersion, "vboxvideo_drv.so")
    pisitools.insinto("/usr/lib/xorg/modules/input",   "out/additions/vboxmouse_drv_%s.so" % XorgVersion, "vboxmouse_drv.so")

    pisitools.insinto("/usr/share/hal/fdi/policy/10osvendor", "src/VBox/Additions/linux/installer/90-vboxguest.fdi")
