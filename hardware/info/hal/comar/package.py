#/usr/bin/python

import os
import shutil

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # User hal needs to be able to read authorizations
    os.system("/usr/bin/polkit-auth --user hal --grant org.freedesktop.policykit.read")

    try:
        shutil.rmtree("/var/lib/hal")
    except OSError:
        pass
