# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("tmake/lib/linux-g++/tmake.conf", "PARDUS_CC", get.CC())
    pisitools.dosed("tmake/lib/linux-g++/tmake.conf", "PARDUS_CXX", get.CXX())
    pisitools.dosed("tmake/lib/linux-g++/tmake.conf", "PARDUS_CFLAGS", get.CFLAGS())
    pisitools.dosed("tmake/lib/linux-g++/tmake.conf", "PARDUS_LDFLAGS", get.LDFLAGS())

    autotools.rawConfigure("--shared \
                            --release \
                            --prefix /usr \
                            --with-doxywizard")

def build():
    autotools.make("QMAKE=%s/bin/qmake" % get.qtDIR())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LANGUAGE.HOWTO", "LICENSE", "README", "VERSION")
