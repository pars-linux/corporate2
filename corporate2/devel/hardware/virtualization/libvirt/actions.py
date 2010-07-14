#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():

    autotools.configure("--localstatedir=/var \
                         --with-init-script=none \
                         --with-remote-pid-file=/var/run/libvirtd.pid \
                         --with-qemu-user=qemu \
                         --with-qemu-group=qemu \
                         --with-lxc \
                         --without-esx \
                         --with-udev \
                         --without-vbox \
                         --with-qemu \
                         --with-sasl \
                         --without-yajl \
                         --with-avahi \
                         --without-netcf \
                         --with-libssh2=/usr/lib \
                         --with-capng \
                         --with-polkit \
                         --with-python \
                         --with-network \
                         --with-libvirtd \
                         --with-storage-fs \
                         --with-storage-scsi \
                         --with-storage-mpath \
                         --with-storage-disk \
                         --with-storage-lvm \
                         --without-storage-iscsi \
                         --without-hal \
                         --without-xen \
                         --without-pyhp \
                         --without-uml \
                         --without-openvz \
                         --without-selinux \
                         --without-apparmor \
                         --without-xen-proxy \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/gtk-doc/html")
    pisitools.dodoc("AUTHORS", "NEWS", "README*", "ChangeLog")
