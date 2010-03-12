#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    pisitools.dobin("src/slocate")
    shelltools.chmod("%s/usr/bin/slocate" % get.installDIR(), 02700)
    shelltools.chown("%s/usr/bin/slocate" % get.installDIR(), "root", "locate")

    pisitools.dobin("debian/cron.daily", "/etc/cron.daily")
    pisitools.rename("/etc/cron.daily/cron.daily", "slocate")

    pisitools.dodir("/var/lib/slocate")
    shelltools.chown("%s/var/lib/slocate" % get.installDIR(), "root", "locate")
    shelltools.chmod("%s/var/lib/slocate" % get.installDIR(), 0750)
    #shelltools.touch("%s/var/lib/slocate/slocate.db" % get.installDIR())

    pisitools.dosym("slocate", "/usr/bin/locate")
    pisitools.dosym("slocate", "/usr/bin/updatedb")

    pisitools.dodoc("WISHLIST", "README", "Changelog", "notes")
    pisitools.doman("doc/*.1")
