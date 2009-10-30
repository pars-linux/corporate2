# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -DNDEBUG" % get.CFLAGS())

    autotools.autoreconf("-vif")
    autotools.configure("--enable-pic \
                         --disable-xcb \
                         --enable-glx-tls \
                         --disable-gl-osmesa \
                         --disable-egl \
                         --disable-glw \
                         --disable-glut \
                         --disable-gallium \
                         --with-driver=dri \
                         --without-demos \
                         --with-dri-driverdir=/usr/lib/xorg/modules/dri \
                         --with-dri-drivers=i810,i915,i965,mach64,r128,r200,r300,r600,radeon,sis,tdfx,trident,ffb,swrast")

def build():
    autotools.make("-j1")

    # Build glxinfo/gears
    autotools.make("-C progs/xdemos glxinfo glxgears")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dobin("progs/xdemos/glxinfo")
    pisitools.dobin("progs/xdemos/glxgears")

    # Don't install unused headers
    for header in ("[a-fh-wyz]*.h", "gg*.h", "glf*.h", "*glut*.h"):
        pisitools.remove("/usr/include/GL/%s" % header)

    # Moving libGL for dynamic switching
    pisitools.domove("/usr/lib/libGL.so.1.2", "/usr/lib/mesa")

    pisitools.dodoc("docs/COPYING", "docs/enums.txt")
    pisitools.dohtml("docs/*")
