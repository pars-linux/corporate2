#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Remove welcome e-mails from Novell
    pisitools.dosed("mail/default/*/Inbox", "^.*$", "")
    autotools.autoreconf("-fi")
    autotools.configure("--enable-plugins=all \
                         --enable-nm=no \
                         --enable-mono=no \
                         --enable-python=no \
                         --enable-nss=yes \
                         --enable-smime=yes \
                         --enable-pst-import=yes \
                         --enable-image-inline=yes \
                         --enable-weather=yes \
                         --enable-audio-inline=yes \
                         --enable-contacts-map=yes \
                         --enable-gtk-doc=yes \
                         --with-openldap \
                         --disable-scrollkeeper \
                         --with-kde-applnk-path=no \
                         --with-help=yes \
                         --with-krb5=/usr")

def build():
    autotools.make()
    autotools.make("-C plugins/tnef-attachments")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C plugins/tnef-attachments DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "COPYING*", "MAINTAINERS", "NEWS", "README")
