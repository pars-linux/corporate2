#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ptsp-client-rootfs"

def install():
    suffix = shelltools.ls("boot/kernel-*")[0].split("kernel-")[1]

    pisitools.insinto("/opt/ptsp/", "*")

    pisitools.insinto("/tftpboot/pts/%s-ptsp" % suffix, "boot/kernel-%s" % suffix)
    pisitools.insinto("/tftpboot/pts/%s-ptsp" % suffix, "boot/initramfs-%s" % suffix)

    # latest-ptsp also is used by AdditionalFiles
    pisitools.dosym("%s-ptsp" % suffix, "/tftpboot/pts/latest-ptsp")

    # tftp works in chroot
    pisitools.dosym("/pts/%s-ptsp/kernel-%s" % (suffix, suffix),
                    "/tftpboot/pts/%s-ptsp/latestkernel" % suffix)

    pisitools.dosym("/pts/%s-ptsp/initramfs-%s" % (suffix, suffix),
                    "/tftpboot/pts/%s-ptsp/latestinitramfs" % suffix)

    # create needed directories
    pisitools.dodir("/opt/ptsp/lib/udev/devices")
    pisitools.dodir("/opt/ptsp/lib/udev/devices/net")
    pisitools.dodir("/opt/ptsp/lib/udev/devices/pts")
    pisitools.dodir("/opt/ptsp/lib/udev/devices/shm")
