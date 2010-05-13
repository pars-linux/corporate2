#/usr/bin/python

import os
import re

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/install -d -m0755 /var/spool")
    os.system("/usr/bin/install -m0700 -o pnp -d /var/spool/cups")
    os.system("/usr/bin/install -m1700 -o pnp -d /var/spool/cups/tmp")
    os.system("/usr/bin/install -m0511 -o pnp -d /var/run/cups/certs")

    # Remove old-style certs directory
    os.system("rm -rf /etc/cups/certs")
