#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import texlivemodules


WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().split('_')[-1])

CoreSource="texlive-%s-source" % get.srcVERSION().split('_')[-1]

def setup():
    shelltools.move("texmf", "%s/texmf" % CoreSource)
    shelltools.move("texmf-dist", "%s/texmf-dist" % CoreSource)

    libtools.libtoolize("--copy --force")

    shelltools.cd("%s/%s/%s" % (get.workDIR(), WorkDir, CoreSource))

    autotools.configure(" --bindir=/usr/bin \
                          --datadir=/usr/share \
                          --prefix=/usr \
                          --with-system-freetype2 \
                          --with-freetype2-include=/usr/include \
                          --with-system-zlib \
                          --with-system-pnglib \
                          --with-system-xpdf \
                          --with-system-teckit \
                          --without-texinfo \
                          --with-xdvipdfmx \
                          --with-teckit-includes=/usr/include/teckit \
                          --disable-detex \
                          --disable-dvi2tty \
                          --disable-dvipng \
                          --disable-dvipdfmx \
                          --disable-luatex \
                          --disable-ps2eps \
                          --disable-psutils \
                          --disable-t1utils \
                          --enable-xetex \
                          --disable-xdvik \
                          --disable-xindy \
                          --disable-dialog \
                          --disable-multiplatform \
                          --with-epsfwin \
                          --with-mftalkwin \
                          --with-regiswin \
                          --with-tektronixwin \
                          --with-unitermwin \
                          --with-ps=gs \
                          --enable-ipc \
                          --disable-lcdf-typetools \
                          --disable-pdfopen \
                          --disable-ttf2pk \
                          --disable-tex4htk \
                          --disable-cjkutils \
                          --disable-vlna \
                          --disable-largefile \
                          --enable-shared \
                          --disable-native-texlive-build")

def build():
    shelltools.cd(CoreSource)
    autotools.make()

def install():

    shelltools.cd(CoreSource)
    autotools.install("bindir=%s/usr/bin texmf=%s/usr/share/texmf run_texlinks=true run_mktexlsr=true" % (get.installDIR() , get.installDIR()))

    # Installing texmf, texmf-dist, tlpkg, texmf-var

    texlivemodules.installTexmfFiles()

    shelltools.cd(get.installDIR())
    shelltools.system("cp -pR usr/texmf usr/share/")
    shelltools.system("cp -pR usr/texmf-dist usr/share/")

    shelltools.system("rm -rf usr/texmf")
    shelltools.system("rm -rf usr/texmf-dist")

    shelltools.cd("%s/%s/%s" % (get.workDIR(), WorkDir, CoreSource))
    # Install documents
    docs = ["ChangeLog", "README", "BUGS", "NEWS", "README.14m", "PROJECTS"]
    dirs = ["kpathsea", "dviljk", "dvipsk", "makeindexk", "ps2pkm", "web2c"]

    pisitools.dodoc("texk/ChangeLog", "texk/README")
    for d in docs:
        for dir in dirs:
            if shelltools.can_access_file("%s/texk/%s/%s" % (get.curDIR(), dir, d)):
                pisitools.insinto("usr/share/doc/%s/texk/%s" % (get.srcNAME(), dir) , "texk/%s/%s" % (dir, d))

    # Remove these directories
    pisitools.removeDir("/usr/share/texmf/doc")

    for d in ["web2c", "updmap.d", "fmtutil.d", "texmf.d", "language.dat.d", "language.def.d"]:
        pisitools.dodir("/etc/texmf/%s" % d)

    pisitools.domove("/usr/share/texmf/web2c/texmf.cnf", "/etc/texmf/texmf.d/")
    pisitools.domove("/usr/share/texmf/web2c/fmtutil.cnf", "/etc/texmf/fmtutil.d/")
    pisitools.domove("/usr/share/texmf/web2c/updmap.cfg","/etc/texmf/updmap.d/", "00updmap.cfg")

    # Remove unnecessary files
    pisitools.remove("/usr/bin/man")

    shelltools.cd("%s/usr/share/texmf/" % get.installDIR())
    texlivemodules.handleConfigFiles()

    pisitools.dodir("/usr/share/texmf-site")

    # Symlinks for regenerated files by texmf-update
    for sym in ["updmap.cfg", "texmf.cnf", "fmtutil.cnf"]:
        pisitools.dosym("/etc/texmf/web2c/%s" % sym, "/usr/share/web2c/%s" % sym)
        pisitools.dosym("/etc/texmf/web2c/%s" % sym, "/usr/share/texmf/web2c/%s" % sym)
    pisitools.dosym("/etc/texmf/dvips/config/config.ps", "/usr/share/dvips/config/config.ps")

    pisitools.dosym("tex", "/usr/bin/virtex")
    pisitools.dosym("pdftex", "/usr/bin/pdfvirtex")

    # Rename mpost to leave room for mplib
    pisitools.domove("/usr/bin/mpost", "/usr/bin/", "mpost-%s" % get.srcNAME())
    pisitools.dosym("mpost-%s" % get.srcNAME(), "/usr/bin/mpost")

    # Keep it as that's where the formats will go
    pisitools.dodir("/var/lib/texmf")

