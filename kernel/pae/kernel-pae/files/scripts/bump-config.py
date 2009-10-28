#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pisi

oldwd = os.getcwd()

kpspec = pisi.specfile.SpecFile('pspec.xml')
kworkdir = kpspec.source.archive.name.split('.tar.bz2')[0]
kname = kpspec.source.name
kver = kpspec.history[0].version
krel = kpspec.history[0].release
kpath = "/var/pisi/%s-%s-%s/work/%s" % (kname, kver, krel, kworkdir)

if os.path.exists(kpath):
    os.chdir(kpath)
    open(os.path.join(oldwd, "files/pardus/kernel-config.patch"), "w").write(os.popen("diff -u /dev/null .config").read())
    os.chdir(oldwd)

else:
    print "%s doesn't exist." % kpath

