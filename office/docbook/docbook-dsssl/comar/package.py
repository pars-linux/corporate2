#!/usr/bin/python

import os
import glob

def manage_catalogs(action, filename, ver):
    catalog_dir = "/usr/share/sgml/docbook/dsssl-stylesheets-%s/catalog" % ver
    cmd = "/usr/bin/install-catalog --%s %s %s" % (action, filename, catalog_dir)
    print "**** %s" % cmd
    os.system(cmd)

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for centralized in glob.glob("/etc/sgml/*-docbook-*.cat"):
        manage_catalogs("add", centralized, toVersion)

def preRemove():
    #FIXME: version is static because preRemove doesn't pass that info
    ver = "1.79"
    for centralized in glob.glob("/etc/sgml/*-docbook-*.cat"):
        manage_catalogs("remove", centralized, ver)
