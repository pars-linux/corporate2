#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "LVM2.%s" % get.srcVERSION()

def builddiet():
    dietCC = "diet %s %s %s -Os -static" % (get.CC(), get.CFLAGS(), get.LDFLAGS())
    shelltools.export("CC", dietCC)

    autotools.make("distclean")
    autotools.autoreconf("-fi")
    autotools.configure("ac_cv_lib_dl_dlopen=no \
                         --enable-debug \
                         --with-optimisation=\"%s -Os\" \
                         --enable-static_link \
                         --with-lvm1=internal \
                         --disable-readline \
                         --disable-nls \
                         --disable-selinux" % get.CFLAGS())

    pisitools.dosed("lib/misc/configure.h","rpl_malloc","malloc")

    autotools.make("-j1 -C include")
    autotools.make("-j1 -C lib LIB_SHARED= VERSIONED_SHLIB=")
    autotools.make("-j1 -C libdm LIB_SHARED= VERSIONED_SHLIB=")
    autotools.make("-j1 -C tools dmsetup.static lvm.static")

    pisitools.insinto("/usr/lib/dietlibc/lib-i386/", "libdm/ioctl/libdevmapper.a")
    pisitools.insinto("/sbin/", "tools/lvm.static")
    pisitools.insinto("/sbin/", "tools/dmsetup.static")

def mkdirAndfixPermisions():
    for dir in ["archive","backup","cache"]:
        pisitools.dodir("/etc/lvm/%s" % dir)
        shelltools.chmod(get.installDIR()+"/etc/lvm/%s" % dir, 0700)

def setup():
    shelltools.export("CLDFLAGS", get.LDFLAGS())
    shelltools.export("LIB_PTHREAD", "-lpthread")

    autotools.autoreconf("-fi")
    autotools.configure("--enable-lvm1_fallback \
                         --enable-fsadm \
                         --with-pool=internal \
                         --with-snapshots=internal \
                         --with-mirrors=internal \
                         --with-interface=ioctl \
                         --with-user= \
                         --with-group= \
                         --with-usrlibdir=/usr/lib \
                         --with-usrsbindir=%s \
                         --with-device-uid=0 \
                         --with-device-gid=6 \
                         --with-device-mode=0660 \
                         --enable-pkgconfig \
                         --enable-applib \
                         --enable-cmdlib \
                         --enable-dmeventd \
                         --enable-static_link=no \
                         --disable-readline \
                         --disable-realtime \
                         --disable-selinux" % get.sbinDIR())


def build():
    autotools.make("-C include")
    autotools.make("-C libdm")
    autotools.make("-C lib")
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())
    mkdirAndfixPermisions()
    #pisitools.move("/sbin/lvmconf","scripts/lvmconf.sh")

    builddiet()
    pisitools.dodoc("COPYING", "COPYING.LIB", "README", "VERSION", "VERSION_DM", "WHATS_NEW","WHATS_NEW_DM")
