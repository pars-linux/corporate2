#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # man pages are disabled because they are created by xsltproc and docbook-xsl dep is needed
    autotools.configure("--with-pam-module-dir=/lib/security/ \
                         --with-os-type=Pardus \
                         --with-polkit-user=polkit \
                         --with-polkit-group=polkit \
                         --disable-man-pages \
                         --localstatedir=/var \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s/" % get.installDIR())

    pisitools.removeDir("/usr/share/gtk-doc")
