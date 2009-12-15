#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "TurboFlot-%s" % get.srcVERSION()


def install():
    pythonmodules.install()

    # It copies same files both under /usr and /usr/lib/python2.6/site-packages/turboflot/static .
    pisitools.remove("/usr/*.js")
    pisitools.remove("/usr/turboflot.css")
