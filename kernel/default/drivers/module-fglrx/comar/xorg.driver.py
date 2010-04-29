#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess

BLACKLIST_CONF = "/etc/modprobe.d/blacklist-radeon.conf"
ZORG_ENABLED_PACKAGE = "/var/lib/zorg/enabled_package"
ZORG_KERNEL_MODULE = "/var/lib/zorg/kernel_module"

def unlink(name):
    if os.path.lexists(name):
        os.unlink(name)

def symlink(src, dst):
    unlink(dst)
    os.symlink(src, dst)

def echo(path, content):
    with open(path, "w") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())

#
# Çomar methods
#

def enable():
    symlink("xorg/fglrx/lib/libGL.so.1.2", "/usr/lib/libGL.so.1.2")
    symlink("../../fglrx/extensions/libglx.so", "/usr/lib/xorg/modules/extensions/libglx.so")

    # Create other links
    subprocess.call(["/sbin/ldconfig"])

    shutil.copy("/etc/ati/amdpcsdb.default", "/etc/ati/amdpcsdb")

    echo(BLACKLIST_CONF, "blacklist radeon")
    for kernel in os.listdir("/etc/kernel"):
        subprocess.call(["/sbin/mkinitramfs", "-t", kernel])

    echo(ZORG_ENABLED_PACKAGE, "xorg_video_fglrx")
    echo(ZORG_KERNEL_MODULE, "fglrx")

    subprocess.call(["/sbin/rmmod", "-s", "fglrx", "radeon"])
    subprocess.call(["/sbin/modprobe", "-s", "fglrx"])

def disable():
    symlink("mesa/libGL.so.1.2", "/usr/lib/libGL.so.1.2")
    symlink("../../std/extensions/libglx.so", "/usr/lib/xorg/modules/extensions/libglx.so")

    unlink(ZORG_ENABLED_PACKAGE)
    unlink(ZORG_KERNEL_MODULE)

    subprocess.call(["/sbin/rmmod", "-s", "fglrx"])

def getInfo():
    info = {
            "alias":        "fglrx",
            "xorg-module":  "fglrx"
            }
    return info

def getDeviceOptions(busId, options):
    return options
