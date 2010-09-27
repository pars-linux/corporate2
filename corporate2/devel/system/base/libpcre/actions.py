#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="pcre-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-utf8 \
                         --enable-unicode-properties \
                         --docdir=/%s/%s \
                         --disable-static" % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
