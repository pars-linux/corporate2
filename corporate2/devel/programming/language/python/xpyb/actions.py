#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("src/Makefile.in", "^(py_compile = ).*", r"\1/bin/true")

    autotools.configure("--enable-xinput")

def build():
    autotools.make()

def install():
    autotools.install()
