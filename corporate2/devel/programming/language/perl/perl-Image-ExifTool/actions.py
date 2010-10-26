#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.removeDir("/usr/lib/perl5/vendor_perl/%s/%s-linux-thread-multi/" % (get.curPERL(), get.ARCH()))

    # add html and doc's
    pisitools.dohtml("html/*")
    pisitools.dodoc("README", "Changes")
