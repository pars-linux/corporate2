#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--exec-prefix=/usr \
                         --localstatedir=/var \
                         --disable-static \
                         --disable-docbook-docs \
                         --disable-gtk-doc \
                         --disable-dependency-tracking \
                         --disable-smbios \
                         --enable-man-pages \
                         --enable-console-kit \
                         --enable-policy-kit \
                         --enable-acl-management \
                         --enable-acpi-ibm \
                         --enable-sonypic \
                         --enable-umount-helper \
                         --with-eject=/usr/bin/eject \
                         --without-dell-backlight \
                         --with-hal-user=hal \
                         --with-hal-group=hal \
                         --with-udev-prefix=/lib")

    # Disable rpath
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gtk-doc")

    # Needed for hal's new cache infrastructure
    pisitools.dodir("/var/cache/hald")

    # Fix permissions of HAL directories
    for d in ["cache", "run"]:
        shelltools.chmod("%s/var/%s/hald" % (get.installDIR(), d), mode=0700)

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "HACKING")
