#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "bash_completion"

def install():
    pisitools.insinto("/etc", "bash_completion")

    pisitools.insinto("/usr/share/bash-completion", "contrib/*")

    pisitools.dodoc("Changelog", "README")
