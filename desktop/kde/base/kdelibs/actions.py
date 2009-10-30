#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

KeepSpecial=["libtool"]

shelltools.export("HOME", get.workDIR())

def setup():
    kde.make("-f admin/Makefile.common")
    kde.configure('--with-distribution="Pardus" \
                   --disable-libfam \
                   --enable-inotify \
                   --with-libart \
                   --with-libidn \
                   --with-utempter \
                   --with-alsa \
                   --with-ssl \
                   --with-tiff \
                   --with-gssapi \
                   --with-openexr \
                   --with-jasper \
                   --enable-cups \
                   --enable-dnssd \
                   --enable-gcc-hidden-visibility \
                   --with-aspell \
                   --with-acl \
                   --without-arts \
                   --without-lua \
                   --without-hspell')

def build():
    kde.make()

def install():
    kde.install()
