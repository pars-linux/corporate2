#!/usr/bin/python

import os.path
import subprocess

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    KVER = open("/etc/kernel/kernel").read().strip()

    # Create initramfs image
    subprocess.call(["/sbin/mkinitramfs", "--type", "kernel"])

    # Update GRUB entry
    if os.path.exists("/boot/grub/grub.conf"):
        call("grub", "Boot.Loader", "updateKernelEntry", (KVER, ""))

    # Temporary workaround for pisi bug
    pakhandler = "/var/db/comar3/scripts/System.PackageHandler/kernel.py"
    pakhandler_app = "/var/db/comar3/apps/kernel/System.PackageHandler"

    for f in (pakhandler, pakhandler):
        if os.path.exists(f):
            try:
                os.unlink(f)
            except IOError:
                pass

def preRemove():
    pass
