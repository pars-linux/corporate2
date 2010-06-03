#!/usr/bin/python

import os

unopkg = "/opt/OpenOffice.org/bin/unopkg"
extPath = "/opt/OpenOffice.org/lib/ooo-3.2/share/extension/install"
extName = "presentation-minimizer"
extID = "com.sun.star.PresentationMinimizer-linux_x86"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.environ["JAVA_HOME"] = "/opt/sun-jre"
    ret = os.system("%s add --shared --force %s/%s.oxt" % (unopkg, extPath, extName))

    if ret != 0:
        raise Exception("Could not install OO.org extension: %s" % extName)

def preRemove():
    os.environ["JAVA_HOME"] = "/opt/sun-jre"
    ret = os.system("%s remove --shared %s" % (unopkg, extID))

    if ret != 0:
        raise Exception("Could not remove OO.org extension: %s" % extName)
