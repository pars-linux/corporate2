#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # I haven't enabled non-C bindings, cause they aren't very useful
    # at the moment. In case if you need them later:
    # C++ binding: remove --without-boost and depend on boost
    # Python binding: add --enable-python-binding and depend on swig
    # Also I haven't decided that if they would be worth separating
    # into their own binary packages.
    autotools.configure("--without-boost \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Compiled examples are not useful, they also pollute /usr/bin namespace
    pisitools.remove("/usr/bin/bitbang*")
    pisitools.remove("/usr/bin/find*")
    pisitools.remove("/usr/bin/simple")
    # Their source can be useful though
    pisitools.dodoc("examples/*.c", destDir="%s/examples" % get.srcNAME())

    pisitools.dodoc("AUTHORS", "COPYING.LIB", "ChangeLog", "LICENSE", "README")
