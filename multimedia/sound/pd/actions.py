#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="%s-%s%s/src" % (get.srcNAME(), get.srcVERSION()[:-2], get.srcVERSION()[-2:].replace(".", "-"))

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-jack \
                         --enable-alsa \
                         --enable-fftw \
                         --enable-portaudio \
                         --enable-portmidi")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("../LICENSE.txt", "../README.txt", "*.txt")
