#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

version = get.srcVERSION()
WorkDir = "gcc-%s" % version

# Global Path Variables
BINPATH = "/usr/%s/gcc-bin/%s" % (get.HOST(), version)
LIBPATH = "/usr/lib/gcc-lib/%s/%s" % (get.HOST(), version)
DATAPATH = "/usr/share/gcc-data/%s/%s" % (get.HOST(), version)
STDCXX_INCDIR = "/usr/lib/gcc-lib/%s/%s/include/g++-v3" % (get.HOST(), version)

cflags = get.CFLAGS().replace("mtune", "mcpu").replace("-fstack-protector", "").replace("-D_FORTIFY_SOURCE=2", "").replace("-mcpu=generic", "-mcpu=%s" % get.ARCH().replace("_", "-"))
cxxflags =  get.CXXFLAGS().replace("mtune", "mcpu").replace("-fstack-protector", "").replace("-D_FORTIFY_SOURCE=2", "").replace("-mcpu=generic", "-mcpu=%s" % get.ARCH().replace("_", "-"))

multilib = (get.ARCH() == "x86_64")
opt_multilib = "--enable-multilib" if multilib else ""

ldconfig = {
            "system": ["/etc/ld.so.conf.d/99-libstdc++.conf", "/usr/lib/libstdc++-v3"],
            "multilib": ["/etc/ld.so.conf.d/99-libstdc++-32bit.conf", "/usr/lib32/libstdc++-v3"]
           }

def setup():
    shelltools.export("CFLAGS", cflags)
    shelltools.export("CXXFLAGS", cxxflags)

    # Misdesign in libstdc++ (Redhat)
    shelltools.copy("libstdc++-v3/config/cpu/i486/atomicity.h", "libstdc++-v3/config/cpu/i386/atomicity.h")

    shelltools.system("./contrib/gcc_update --touch &> /dev/null")

    conf = "--enable-nls \
            --without-included-gettext \
            %s \
            --prefix=/usr \
            --bindir=%s \
            --includedir=%s/include \
            --datadir=%s \
            --mandir=%s/man \
            --infodir=%s/info \
            --enable-shared \
            --host=%s \
            --target=%s \
            --with-system-zlib \
            --enable-languages=c++ \
            --enable-threads=posix \
            --enable-long-long \
            --disable-checking \
            --enable-cstdio=stdio \
            --enable-__cxa_atexit \
            --enable-version-specific-runtime-libs \
            --with-gxx-include-dir=%s \
            --with-local-prefix=/usr/local" % (opt_multilib, BINPATH, LIBPATH, DATAPATH, DATAPATH, DATAPATH, get.HOST(), get.HOST(), STDCXX_INCDIR)

    # Build in a separate build tree
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("../configure %s" % conf)

    shelltools.touch("gcc/c-gperf.h")

def build():
    shelltools.cd("build")
    autotools.make('all-target-libstdc++-v3 \
                    LIBPATH="%s" \
                    BOOT_CFLAGS="%s" STAGE1_CFLAGS="-O"' % (LIBPATH, cflags))

def install():
    shelltools.cd("build")

    # Do the 'make install' from the build directory
    autotools.rawInstall('prefix=/usr \
                          bindir="%s" \
                          includedir="%s/include" \
                          datadir="%s" \
                          mandir="%s/man" \
                          infodir="%s/info" \
                          DESTDIR="%s" \
                          LIBPATH="%s"' % (BINPATH, LIBPATH, DATAPATH, DATAPATH, DATAPATH, get.installDIR(), LIBPATH),
                          "install-target-libstdc++-v3")

    confdirbase = ldconfig["system"][0].rsplit("/", 1)[0]
    pisitools.dodir(confdirbase)

    # we'll move this into a directory we can put at the end of ld.so.conf
    # other than the normal versioned directory, so that it doesnt conflict
    # with gcc 3.3.3
    pisitools.domove("/%s/lib*.so.*" % LIBPATH, "/usr/lib/libstdc++-v3/")
    shelltools.echo("%s/%s" % (get.installDIR(), ldconfig["system"][0]), ldconfig["system"][1])

    if multilib:
        pisitools.domove("/%s/32/lib*.so.*" % LIBPATH, "/usr/lib32/libstdc++-v3/")
        shelltools.echo("%s/%s" % (get.installDIR(), ldconfig["multilib"][0]), ldconfig["multilib"][1])


    for i in ["/usr/lib/gcc-lib", "/usr/share/gcc-data"]:
        if shelltools.isDirectory("%s/%s" % (get.installDIR(), i)):
            pisitools.removeDir(i)

