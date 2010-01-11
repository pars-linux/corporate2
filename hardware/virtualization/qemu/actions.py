#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip=["/usr/share/qemu"]

# Disabled linux-user targets: m68k, ppc, ppc64, ppc64abi32, sh4, sh4eb
# user_targets=["alpha","arm","armeb","cris","i386","mips","mipsel","sparc","sparc32plus","sparc64", "x86_64"]

# Disabled softmmu targets (in addition to above) : alpha, arm, armeb
# soft_targets=["cris","i386","mips","mipsel","sparc","sparc32plus","sparc64", "x86_64"]

# target_list=[]

# for target in user_targets:
#     target_list.append("%s-linux-user" % target)

# for target in soft_targets:
#     target_list.append("%s-softmmu" % target)

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
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # for i in ["pc-bios/README", "qemu-doc.html", "qemu-tech.html"]:
    for i in ["pc-bios/README", "LICENSE", "TODO", "README"]:
        pisitools.dodoc(i)

