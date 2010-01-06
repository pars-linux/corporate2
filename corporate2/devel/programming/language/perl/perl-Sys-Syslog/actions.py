#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Sys-Syslog-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

# sandbox violation trying to access /dev/log
#def check():
#    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("Changes", "README")

    # conflicts with the man page in perl-doc package
    pisitools.remove("usr/share/man/man3/Sys::Syslog.3pm")
