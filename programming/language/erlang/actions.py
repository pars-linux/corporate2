#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir="otp_src_R%sB0%s" % (get.srcVERSION().split(".")[0], get.srcVERSION().split(".")[1])

# For finding javac, javadoc
shelltools.export("PATH", "%s:/opt/sun-jdk/bin" % (os.environ.get("PATH")))

def setup():
    # Remove bundled zlib
    shelltools.unlink("erts/emulator/zlib/*.[ch]")

    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())
    autotools.configure("--enable-shared-zlib \
                         --enable-dynamic-ssl-lib \
                         --enable-threads \
                         --enable-kernel-poll \
                         --enable-hipe \
                         --enable-smp-support \
                         --with-ssl")

def build():
    #autotools.make("-j1")

    # Building documentation needs escript from erlang package
    shelltools.export("PATH", "%s:%s/bin" % (os.environ.get("PATH"), get.curDIR()))
    autotools.make("docs")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s install-docs" % get.installDIR())

    # Cleanup package
    pisitools.remove("/usr/lib/erlang/Install")

    # Remove win32 stuff, old txt files, object files, etc.
    for f in ("lib/observer-*/priv/bin/*.bat",
              "lib/os_mon-*/ebin/nteventlog.beam",
              "lib/ssl-*/examples/certs/etc/otpCA/*.txt.old",
              "lib/webtool-*/priv/bin/start_webtool.bat"):
        pisitools.remove("/usr/lib/erlang/%s" % f)

    for d in ("lib/*/priv/obj",
              "lib/*/c_src",
              "lib/*/java_src",
              "erts-5.7.5/doc",
              "erts-5.7.5/man",
              "misc"):
        pisitools.remove("/usr/lib/erlang/%s" % d)


    # Install man pages
    #pisitools.doman("man/man1/*")
    #pisitools.doman("man/man3/*")
