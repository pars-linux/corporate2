#!/usr/bin/python

import os

# Update global mime databases, mime database format may change (0.70)
def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for p in ["/usr/kde/3.5/share/mime", "/usr/share/mime"]:
        os.system("/usr/bin/update-mime-database %s" % p)
