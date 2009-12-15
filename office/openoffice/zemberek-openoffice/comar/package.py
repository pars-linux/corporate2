#!/usr/bin/python

import os
import glob

unopkg = "/opt/OpenOffice.org/bin/unopkg"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.environ["JAVA_HOME"] = "/opt/sun-jre"
    extPath = glob.glob("/usr/share/zemberek/zemberek*.oxt")[0]
    os.system("%s add --shared --force %s" % (unopkg, extPath))

def preRemove():
    os.environ["JAVA_HOME"] = "/opt/sun-jre"
    extPath = glob.glob("/usr/share/zemberek/zemberek*.oxt")[0]
    os.system("%s remove --shared %s" % (unopkg, os.path.basename(extPath)))
