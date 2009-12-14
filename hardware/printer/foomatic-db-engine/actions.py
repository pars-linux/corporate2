#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "foomatic-db-engine-devel-%s" % get.srcVERSION().replace("4.0.3_", "4.0-")

def setup():
    # The LANG vars aren't reset early enough so when sed tries to use [a-zA-Z], it borks
    shelltools.export("LC_ALL", "C")
    shelltools.export("LANG", "C")

    autotools.autoconf()
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("lib")
    perlmodules.configure()
    perlmodules.make()
    perlmodules.install()

    # Clean .packlists
    pisitools.removeDir("/usr/lib/perl5/%s" % get.curPERL())
    pisitools.removeDir("/usr/lib/perl5/vendor_perl/%s/i686-linux-thread-multi" % get.curPERL())

    shelltools.cd("..")
    pisitools.dodoc("ChangeLog", "COPYING", "README", "TODO", "USAGE")
