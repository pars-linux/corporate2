#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

# kernel-headers package provides these
kheaders = ("drm.h",
            "drm_mode.h",
            "drm_sarea.h",
            "i915_drm.h",
            "mga_drm.h",
            "nouveau_drm.h",
            "r128_drm.h",
            "radeon_drm.h",
            "savage_drm.h",
            "sis_drm.h",
            "via_drm.h")

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-udev \
                         --enable-nouveau-experimental-api \
                         --enable-radeon-experimental-api")

def build():
    autotools.make()

def install():
    autotools.install()

    for f in kheaders:
        pisitools.remove("/usr/include/drm/%s" % f)
