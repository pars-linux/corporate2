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

WorkDir = "avahi-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--with-distro=none \
                         --disable-monodoc \
                         --disable-static \
                         --disable-xmltoman \
                         --disable-doxygen-doc \
                         --disable-mono \
                         --disable-autoipd \
                         --disable-core-docs \
                         --disable-libdaemon \
                         --enable-dbus \
                         --enable-python-dbus \
                         --enable-gdbm \
                         --disable-compat-howl \
                         --disable-compat-libdns_sd \
                         --disable-pygtk \
                         --enable-shared \
                         --enable-qt3 \
                         --enable-qt4 \
                         --enable-gtk \
                         --enable-glib \
                         --enable-gobject \
                         --enable-python \
                         --enable-pygtk \
                         --localstatedir=/var \
                         --with-avahi-user=avahi \
                         --with-avahi-group=avahi \
                         --with-autoipd-user=avahi \
                         --with-autoipd-group=avahi \
                         --with-avahi-priv-access-group=avahi")

def build():
    # for mono sandbox errors
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.make()

def install():
    # for mono sandbox errors
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove unneded files and directory
    pisitools.remove("/usr/lib/pkgconfig/avahi-core.pc")
    pisitools.remove("/usr/lib/pkgconfig/avahi-client.pc")
    pisitools.remove("/usr/lib/pkgconfig/avahi-ui.pc")

    pisitools.remove("/usr/bin/avahi-bookmarks")
    pisitools.remove("/usr/bin/avahi-discover")

    pisitools.removeDir("/usr/lib/python2.6/site-packages/avahi_discover")

    pisitools.remove("/usr/share/applications/avahi-discover.desktop")
