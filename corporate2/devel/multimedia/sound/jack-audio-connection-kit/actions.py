# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    # for using posix-shm see https://bugzilla.novell.com/show_bug.cgi?id=337972
    autotools.configure("--enable-html-docs \
                         --with-html-dir=/usr/share/doc/%s \
                         --enable-timestamps \
                         --enable-freebob \
                         --enable-firewire \
                         --enable-resize \
                         --disable-optimize \
                         --disable-oss \
                         --disable-portaudio \
                         --disable-ensure-mlock \
                         --disable-dependency-tracking \
                         --with-default-tmpdir=/dev/shm" % get.srcNAME())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README", "TODO")
