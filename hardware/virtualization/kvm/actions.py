#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip=["/usr/share/kvm"]
WorkDir="qemu-kvm-%s" % get.srcVERSION()

soundDrivers = "alsa pa sdl oss"
cflags = get.CFLAGS().replace("-fpie", "").replace("-fstack-protector", "")
def setup():
    # disable fdt until dtc is in repo
    # pisitools.dosed("configure", 'fdt="yes"', 'fdt="no"')

    shelltools.export("CFLAGS", cflags)
    autotools.rawConfigure('--prefix=/usr \
                            --disable-werror \
                            --audio-drv-list="%s" \
                            --cc="%s" \
                            --host-cc="%s" \
                            --enable-system \
                            --enable-linux-user \
                            --disable-bsd-user \
                            --disable-darwin-user' % (soundDrivers, get.CC(), get.CC()))
                            # --audio-card-list="ac97 es1370 sb16 cs4231a adlib gus" \
                            # --target-list="%s"' % " ".join(target_list))
                            # --disable-bluez \
                            # --kerneldir="/lib/modules/%s/build" \


def build():
    autotools.make("V=1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/bin/qemu-system-x86_64", "/usr/bin/", "qemu-kvm")
    pisitools.domove("/usr/share/man/man1/qemu.1", "/usr/share/man/man1/", "qemu-kvm.1")

    # Use the one qemu provides
    pisitools.remove("/usr/bin/qemu-img")
    pisitools.remove("/usr/share/man/man1/qemu-img.1")
    pisitools.remove("/usr/bin/qemu-nbd")
    pisitools.remove("/usr/share/man/man8/qemu-nbd.8")
    pisitools.removeDir("/usr/share/doc")
