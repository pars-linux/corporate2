#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/var/lib/dhcp/dhcpd.leases"):
        os.system("/bin/touch /var/lib/dhcp/dhcpd.leases")
