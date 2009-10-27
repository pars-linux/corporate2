#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #autotools.autoreconf("-fi")

    autotools.configure("--exec-prefix= \
                         --libexecdir=/lib/udev \
                         --libdir=/usr/lib \
                         --enable-logging")

def build():
    autotools.make("all")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # These were explicitly not installed in udev-125, so I remove them.
    pisitools.remove("/lib/udev/fstab_import")
    pisitools.remove("/lib/udev/rules.d/79-fstab_import.rules")

    # Manually install gentoo rules

    # I don't think that we'll need these weird compat rules in 2009
    # pisitools.insinto("/lib/udev/rules.d", "rules/gentoo/30-kernel-compat.rules")

    # Let's keep it for a while, I'm not sure
    pisitools.insinto("/lib/udev/rules.d", "rules/gentoo/40-gentoo.rules")

    # Install additional rules from packages/ directory

    # pisitools.insinto("/lib/udev/rules.d", "rules/packages/40-alsa.rules")            // Shipped with alsa-utils
    # pisitools.insinto("/lib/udev/rules.d", "rules/packages/64-device-mapper.rules")   // Shipped with device-mapper
    # pisitools.insinto("/lib/udev/rules.d", "rules/packages/40-ppc.rules")             // Unsupported architecture
    # pisitools.insinto("/lib/udev/rules.d", "rules/packages/40-s390.rules")            // Unsupported architecture

    pisitools.insinto("/lib/udev/rules.d", "rules/packages/64-md-raid.rules")
    pisitools.insinto("/lib/udev/rules.d", "rules/packages/40-ia64.rules")
    pisitools.insinto("/lib/udev/rules.d", "rules/packages/40-infiniband.rules")
    pisitools.insinto("/lib/udev/rules.d", "rules/packages/40-isdn.rules")
    pisitools.insinto("/lib/udev/rules.d", "rules/packages/40-pilot-links.rules")
    pisitools.insinto("/lib/udev/rules.d", "rules/packages/40-zaptel.rules")

    # FIXME: We have GROUP conversions here!
    # Only some gentoo and 50-udev-default.rules are affected by the renamings below

    pisitools.dosed("%s/lib/udev/rules.d/50-udev-default.rules" % get.installDIR(), 'GROUP="floppy"', 'GROUP="pnp"')
    pisitools.dosed("%s/lib/udev/rules.d/50-udev-default.rules" % get.installDIR(), 'GROUP="lp"', 'GROUP="pnp"')
    pisitools.dosed("%s/lib/udev/rules.d/50-udev-default.rules" % get.installDIR(), 'GROUP="cdrom"', 'GROUP="removable"')
    pisitools.dosed("%s/lib/udev/rules.d/40-gentoo.rules" % get.installDIR(), 'GROUP="usb"', 'GROUP="removable"')
    # pisitools.dosed("%s/lib/udev/rules.d/30-kernel-compat.rules" % get.installDIR(), 'GROUP="usb"', 'GROUP="removable"')

    # Compat symlinks
    pisitools.dosym("/sbin/udevadm", "/usr/bin/udevinfo")
    pisitools.dosym("/sbin/udevadm", "/usr/bin/udevtest")
    pisitools.dosym("/sbin/udevadm", "/usr/bin/udevsettle")
    pisitools.dosym("/sbin/udevadm", "/usr/bin/udevtrigger")
    pisitools.dosym("/sbin/udevadm", "/usr/bin/udevmonitor")
    pisitools.dosym("/sbin/udevadm", "/usr/bin/udevcontrol")

    # create needed directories
    pisitools.dodir("/lib/udev/devices")
    pisitools.dodir("/lib/udev/devices/net")
    pisitools.dodir("/lib/udev/devices/pts")
    pisitools.dodir("/lib/udev/devices/shm")

    # Create vol_id and scsi_id symlinks in /sbin probably needed by multipath-tools
    pisitools.dosym("/lib/udev/scsi_id", "/sbin/scsi_id")

    # Create /etc/udev/rules.d for backward compatibility
    pisitools.dodir("/etc/udev/rules.d")

    # Remove gtk-doc
    pisitools.removeDir("/usr/share/gtk-doc")

    # FIXME: Remove keymap and hid2hci stuff for now
    for p in ["keymap", "hid2hci"]:
        pisitools.remove("/lib/udev/%s" % p)
        pisitools.remove("/lib/udev/rules.d/*%s*.rules" % p)

    pisitools.removeDir("/lib/udev/keymaps")
    pisitools.remove("/lib/udev/findkeyboards")

    # Install docs
    pisitools.dodoc("COPYING", "ChangeLog", "README", "TODO")
