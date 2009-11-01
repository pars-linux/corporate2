#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2006,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.insinto("%s/share/apps/kdm/themes/pardus/" % get.kdeDIR(), "./*")
