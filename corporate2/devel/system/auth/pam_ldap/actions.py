#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--with-ldap-lib=openldap \
                         --disable-dependency-tracking \
                         --libdir=/lib")

def build():
    autotools.make("-j1")

def install():
    pisitools.doexe("pam_ldap.so", "/lib/security")

    # This may be more useful in /etc/openldap/schema/
    pisitools.dodoc("ns-pwd-policy.schema")
    pisitools.doman("pam_ldap.5")

    pisitools.dodoc("ChangeLog", "README", "AUTHORS")
