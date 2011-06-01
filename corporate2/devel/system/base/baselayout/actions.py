# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    # NOTE: This is only for the start-stop-daemon
    autotools.make('-C src CC="%s" LD="%s %s" CFLAGS="%s"' % (get.CC(), get.CC(), get.LDFLAGS(), get.CFLAGS()))

def install():
    pisitools.insinto("/", "root/*")

    def chmod(path, mode):
        shelltools.chmod("%s%s" % (get.installDIR(), path), mode)

    # Install baselayout utilities
    autotools.rawInstall('-C src DESTDIR="%s"' % get.installDIR())

    chmod("/tmp", 01777)
    chmod("/var/lock", 0755)
    chmod("/var/tmp", 01777)
    chmod("/usr/share/baselayout/shadow", 0600)

    # For Corporate2's KDE3
    pisitools.dosym("/etc/xdg/autostart", "/usr/share/autostart")

    if get.ARCH() == "x86_64":
        # Directories for 32bit libraries
        pisitools.dodir("/lib32")
        pisitools.dodir("/usr/lib32")

        # Hack for binary blobs built on multi-lib systems
        pisitools.dosym("lib", "/lib64")
