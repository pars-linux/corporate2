#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess

def unlink(name):
    if os.path.lexists(name):
        os.unlink(name)

def symlink(src, dst):
    unlink(dst)
    os.symlink(src, dst)

#
# Çomar methods
#

def enable():
    symlink("xorg/fglrx/lib/libGL.so.1.2", "/usr/lib/libGL.so.1.2")
    symlink("../../fglrx/extensions/libdri.so", "/usr/lib/xorg/modules/extensions/libdri.so")
    symlink("../../fglrx/extensions/libglx.so", "/usr/lib/xorg/modules/extensions/libglx.so")

    # Create other links
    subprocess.call(["/sbin/ldconfig"])

    shutil.copy("/etc/ati/amdpcsdb.default", "/etc/ati/amdpcsdb")

    file("/var/lib/zorg/enabled_package", "w").write("xorg_video_fglrx")
    file("/var/lib/zorg/kernel_module", "w").write("fglrx")

    subprocess.call(["/sbin/rmmod", "-s", "fglrx", "radeon"])
    subprocess.call(["/sbin/modprobe", "-s", "fglrx"])

def disable():
    symlink("mesa/libGL.so.1.2", "/usr/lib/libGL.so.1.2")
    symlink("../../std/extensions/libdri.so", "/usr/lib/xorg/modules/extensions/libdri.so")
    symlink("../../std/extensions/libglx.so", "/usr/lib/xorg/modules/extensions/libglx.so")

    unlink("/var/lib/zorg/enabled_package")
    unlink("/var/lib/zorg/kernel_module")

    subprocess.call(["/sbin/rmmod", "-s", "fglrx"])

def getInfo():
    info = {
            "alias":        "fglrx",
            "xorg-module":  "fglrx"
            }
    return info

def getDeviceOptions(busId, options):
    return options
