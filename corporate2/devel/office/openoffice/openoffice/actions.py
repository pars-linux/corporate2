#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os
import re

#Those are global variables that will be assigned later in the setup method
UpstreamVersion = None
BaseVersion = None
#FIXME: This method fails if you use --install like methods, make this a seperate function

WorkDir = "ooo-build-%s" % get.srcVERSION()

# NoStrip variable will also be extended in setup method because, we need some version sstrings from configure.in file which will be used in NoStrip directories.
NoStrip = []

def getJobCount():
    # If jobs field in pisi.conf is greater than 1, use 'this value - 1' as number of cpus. There is also a max-jobs configure opt. but it's buggy now
    return max(int(get.makeJOBS().strip().replace("-j", "")) - 1, 1)

def setup():
    global UpstreamVersion
    UpstreamVersion = re.search("^DEFAULT_TAG=(.*)$", open("configure.in").read(), re.M).group(1)

    global BaseVersion
    BaseVersion = re.search("^OOO_MAJOR=(.*)$", open("configure.in").read(), re.M).group(1)

    NoStrip.extend(["/opt/OpenOffice.org/lib/ooo-%s/basis%s/share" % (BaseVersion, BaseVersion), "/opt/OpenOffice.org/lib/ooo-%s/share" % BaseVersion])

    shelltools.export("QT4DIR", get.qtDIR())
    shelltools.export("QT4INC", "%s/include" % get.qtDIR())
    shelltools.export("QT4LIB", "%s/lib" % get.qtDIR())
    shelltools.export("KDE4DIR", get.kdeDIR())

    #libdir is needed to set exec_prefix stuff of patches/dev300/system-python-ure-bootstrap.diff
    shelltools.system('./configure \
                       --prefix=/opt/OpenOffice.org \
                       --libdir=/opt/OpenOffice.org/lib \
                       --sysconfdir=/etc \
                       --with-lang="de en-US es fr hu it nl pt-BR sv tr" \
                       --disable-post-install-scripts \
                       --disable-gtk \
                       --disable-kde4 \
                       --enable-kde \
                       --disable-cairo \
                       --disable-mono \
                       --with-distro=Corporate2 \
                       --with-drink=turkish_coffee \
                       --with-gcc-speedup=ccache \
                       --with-ant-home=/usr/share/ant \
                       --with-binsuffix=no \
                       --with-system-mdbtools \
                       --with-openclipart=/usr/share/clipart/openclipart \
                       --with-num-cpus=%s' % getJobCount())

def build():
    shelltools.export("HOME", get.workDIR())

    #FIXME: parallel build seems not to work well :/
    autotools.make("-j1")

def install():
    shelltools.export("HOME", get.workDIR())

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #Remove upstream desktop files, use ours. It's very hard to translate and make changes in those desktop files
    pisitools.remove("/usr/share/applications/*.desktop")

    #dosym main executables
    for bin in map(os.path.basename, shelltools.ls("%s/opt/OpenOffice.org/bin/*" % get.installDIR())):
        pisitools.dosym("/opt/OpenOffice.org/bin/ooo-wrapper.py", "/usr/bin/%s" % bin)

    # Icons
    pisitools.insinto("/usr/share/pixmaps","desktop/48x48/*.png")

    # Icon symlinks
    pisitools.dosym("/usr/share/pixmaps/ooo-impress.png","/usr/share/pixmaps/presentation.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-writer.png","/usr/share/pixmaps/wordprocessing.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-calc.png","/usr/share/pixmaps/spreadsheet.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-base.png","/usr/share/pixmaps/database.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-draw.png","/usr/share/pixmaps/drawing.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-math.png","/usr/share/pixmaps/formula.png")

    #Put pyuno to python directory and add OpenOffice.org python modules directory to sys.path in uno.py
    unoPath = "/opt/OpenOffice.org/lib/ooo-%s/basis%s/program/uno.py" % (BaseVersion, BaseVersion)
    unopy = open(get.installDIR() + unoPath).read()
    pisitools.dodir("/usr/lib/%s/site-packages/" % get.curPYTHON())
    newunopy = open("%s/usr/lib/%s/site-packages/uno.py" % (get.installDIR(), get.curPYTHON()), "w")
    newunopy.write("import sys\nsys.path.append('/opt/OpenOffice.org/lib/ooo-%s/basis%s/program')\n%s" % (BaseVersion, BaseVersion, unopy))
    newunopy.close()
    pisitools.remove(unoPath)
    pisitools.domove("/opt/OpenOffice.org/lib/ooo-%s/basis%s/program/unohelper.py" % (BaseVersion, BaseVersion), "/usr/lib/%s/site-packages" % get.curPYTHON())

    solverDirList = shelltools.ls("build/%s/solver" % UpstreamVersion)
    if len(solverDirList) != 1:
        raise Exception("Could not find solver directory!")
    solverDir = solverDirList[0]

    #install pdfimport, report-builder, wiki-publisher and presenter screen as extensions
    pisitools.insinto("/opt/OpenOffice.org/lib/ooo-%s/share/extension/install/" % BaseVersion, "build/%s/solver/%s/unxlng*.pro/bin/report-builder.oxt" % (UpstreamVersion, solverDir))
    pisitools.insinto("/opt/OpenOffice.org/lib/ooo-%s/share/extension/install/" % BaseVersion, "build/%s/solver/%s/unxlng*.pro/bin/swext/wiki-publisher.oxt" % (UpstreamVersion, solverDir))
    pisitools.insinto("/opt/OpenOffice.org/lib/ooo-%s/share/extension/install/" % BaseVersion, "build/%s/solver/%s/unxlng*.pro/bin/minimizer/presentation-minimizer.oxt" % (UpstreamVersion, solverDir))
    pisitools.insinto("/opt/OpenOffice.org/lib/ooo-%s/share/extension/install/" % BaseVersion, "build/%s/solver/%s/unxlng*.pro/bin/presenter/presenter-screen.oxt" % (UpstreamVersion, solverDir))
    pisitools.insinto("/opt/OpenOffice.org/lib/ooo-%s/share/extension/install/" % BaseVersion, "build/%s/solver/%s/unxlng*.pro/bin/pdfimport/pdfimport.oxt" % (UpstreamVersion, solverDir))

    #install man files
    pisitools.domove("/opt/OpenOffice.org/share/man/man1/*", "/usr/share/man/man1")
    pisitools.removeDir("/opt/OpenOffice.org/share/man")

    pisitools.dodoc("AUTHORS","ChangeLog","COPYING","NEWS","README")

    #Workaround for #11530, bnc#502641
    pisitools.dosed("%s/opt/OpenOffice.org/lib/ooo-%s/basis%s/share/registry/data/org/openoffice/Office/Calc.xcu" % (get.installDIR(), BaseVersion, BaseVersion), "</oor:component-data>", " <node oor:name=\"Formula\">\n  <node oor:name=\"Syntax\">\n   <prop oor:name=\"Grammar\" oor:type=\"xs:int\">\n    <value>0</value>\n   </prop>\n  </node>\n </node>\n</oor:component-data>")
