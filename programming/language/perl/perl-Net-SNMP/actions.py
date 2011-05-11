#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "Net-SNMP-v6.0.1"

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("Changes", "LICENSE", "README")

    pisitools.removeDir("/usr/lib/perl5/vendor_perl/%s/%s-linux-thread-multi/" % (get.curPERL(), get.ARCH()))
