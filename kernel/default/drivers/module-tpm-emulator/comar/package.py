#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown tss:tss /var/lib/tpm")
    os.system("/bin/chmod 1777 /var/lib/tpm")
