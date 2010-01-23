#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "pam_krb5-%s-1" % get.srcVERSION()

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--libdir=/lib \
                         --with-os-distribution='Pardus Linux'")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dosym("pam_krb5.so", "/lib/security/pam_krb5afs.so")

    pisitools.dodoc("README*", "NEWS", "ChangeLog", "COPYING*")
