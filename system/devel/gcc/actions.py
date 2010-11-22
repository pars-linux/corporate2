#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# let's not break arch
# cflags = "-march=%s -O2 -g -pipe -fomit-frame-pointer" % get.ARCH().replace("x86_64", "x86-64")
cflags = "-O2 -g -pipe -fomit-frame-pointer"
opt_multilib = "--enable-multilib" if get.ARCH() == "x86_64" else ""

def exportFlags():
    shelltools.export("CFLAGS", cflags)
    shelltools.export("CXXFLAGS", cflags)
    # shelltools.export("LDFLAGS", "")

    # FIXME: this may not be necessary for biarch
    shelltools.export("CC", "gcc")
    shelltools.export("CXX", "g++")
    shelltools.export("LC_ALL", "en_US.UTF-8")

def setup():
    exportFlags()
    # Maintainer mode off, do not force recreation of generated files
    # shelltools.system("contrib/gcc_update --touch")

    #for i in ["libgfortran"]:
    #    shelltools.cd(i)
    #    autotools.autoreconf("-vfi")
    #    shelltools.cd("..")

    shelltools.makedirs("build")
    shelltools.cd("build")

    shelltools.system('../configure \
                       --prefix=/usr \
                       --bindir=/usr/bin \
                       --libdir=/usr/lib \
                       --libexecdir=/usr/lib \
                       --includedir=/usr/include \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --with-gxx-include-dir=/usr/include/c++ \
                       --build=%s \
                       --disable-libgcj \
                       --disable-nls \
                       --disable-mudflap \
                       --disable-libmudflap \
                       --disable-libunwind-exceptions \
                       --enable-checking=release \
                       --enable-clocale=gnu \
                       --enable-__cxa_atexit \
                       --enable-languages=c,c++,fortran,objc \
                       --enable-libstdcxx-allocator=new \
                       --disable-libstdcxx-pch \
                       --enable-shared \
                       --enable-ssp \
                       --disable-libssp \
                       --enable-threads=posix \
                       --without-included-gettext \
                       %s \
                       --with-tune=generic \
                       --with-system-zlib \
                       --disable-werror \
                       --with-pkgversion="Pardus Linux" \
                       --with-bugurl=http://bugs.pardus.org.tr' % (get.HOST(), opt_multilib))
                       # FIXME: this is supposed to be detected automatically
                       #--enable-long-long \
                       # --without-system-libunwind \ # leave it to compiler
                       # --with-tune=generic \


def build():
    exportFlags()

    shelltools.cd("build")
    autotools.make('BOOT_CFLAGS="%s" profiledbootstrap' % cflags)

def install():
    shelltools.cd("build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for header in ["limits.h","syslimits.h"]:
        pisitools.insinto("/usr/lib/gcc/%s/%s/include" % (get.HOST(), get.srcVERSION()) , "gcc/include-fixed/%s" % header)

    # Not needed
    pisitools.removeDir("/usr/lib/gcc/*/*/include-fixed")
    pisitools.removeDir("/usr/lib/gcc/*/*/install-tools")

    # This one comes with binutils
    pisitools.remove("/usr/lib*/libiberty.a")

    # cc symlink
    pisitools.dosym("/usr/bin/gcc" , "/usr/bin/cc")

    # /lib/cpp symlink for legacy X11 stuff
    pisitools.dosym("/usr/bin/cpp", "/lib/cpp")

