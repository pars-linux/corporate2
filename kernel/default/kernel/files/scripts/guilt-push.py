#!/usr/bin/python
# -*- coding: utf-8 -*-

import pisi
import sys
import os

SVNDIR = os.getcwd()
GITDIR = "/root/git/kernel"
GITBRANCH = "pardus-2009"


def import_all_patches(patches):
    for p in patches:
        print "Importing %s" % p.filename
        os.system("guilt-import %s/files/%s" % (SVNDIR, p.filename))

if __name__ == "__main__":
    # Get currently applied patches
    spec = pisi.specfile.SpecFile('pspec.xml')
    patches = spec.source.patches
    patches.sort(reverse=True)
    kver = spec.history[0].version

    # Filter out stable patch if requested
    if True:
        stable_patch = "patch-%s.bz2" % kver
        for p in patches:
            if stable_patch in p.filename:
                print "Dropping %s as requested" % stable_patch
                patches.remove(p)
                break

    os.chdir(GITDIR)

    # Init guilt if necessary
    if not os.path.exists(".git/patches/%s" % GITBRANCH):
        os.system("guilt-init")

    # Import all patches to guilt
    os.system("git checkout %s" % GITBRANCH)
    import_all_patches(patches)
