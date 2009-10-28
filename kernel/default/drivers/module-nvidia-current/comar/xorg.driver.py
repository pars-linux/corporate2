#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess

from zorg.config import getDeviceInfo

version = "185.18.36"
driver = "nvidia-current"
base = "/usr/lib/xorg/%s" % driver

def unlink(name):
    if os.path.lexists(name):
        os.unlink(name)

def symlink(src, dst):
    unlink(dst)
    os.symlink(src, dst)

links = (
        # X driver
        ("%s/drivers/nvidia_drv.so" % base, "/usr/lib/xorg/modules/drivers/nvidia_drv.so"),

        # XvMC library
        ("%s/lib/libXvMCNVIDIA.so.%s" % (base, version), "/usr/lib/libXvMCNVIDIA.so.%s" % version),
        ("libXvMCNVIDIA.so.%s" % version, "/usr/lib/libXvMCNVIDIA.so"),

        # glx extension
        ("%s/extensions/libglx.so.%s" % (base, version), "/usr/lib/xorg/modules/extensions/libglx.so"),

        # GL library
        ("%s/lib/libGL.so.%s" % (base, version), "/usr/lib/libGL.so.1.2"),

        ("libGLcore.so.1", "/usr/lib/libGLcore.so"),
        ("libGLcore.so.%s" % version, "/usr/lib/libGLcore.so.1"),
        ("%s/lib/libGLcore.so.%s" % (base, version), "/usr/lib/libGLcore.so.%s" % version),

        # Cuda library
        ("libcuda.so.1", "/usr/lib/libcuda.so"),
        ("libcuda.so.%s" % version, "/usr/lib/libcuda.so.1"),
        ("%s/lib/libcuda.so.%s" % (base, version), "/usr/lib/libcuda.so.%s" % version),

        # VDPAU library
        ("libvdpau_nvidia.so.%s" % version, "/usr/lib/libvdpau_nvidia.so"),
        ("%s/lib/libvdpau_nvidia.so.%s" % (base, version), "/usr/lib/libvdpau_nvidia.so.%s" % version),

        # nvidia-cfg library
        ("libnvidia-cfg.so.1", "/usr/lib/libnvidia-cfg.so"),
        ("libnvidia-cfg.so.%s" % version, "/usr/lib/libnvidia-cfg.so.1"),
        ("%s/lib/libnvidia-cfg.so.%s" % (base, version), "/usr/lib/libnvidia-cfg.so.%s" % version),

        # nvidia-tls library
        ("libnvidia-tls.so.1", "/usr/lib/libnvidia-tls.so"),
        ("libnvidia-tls.so.%s" % version, "/usr/lib/libnvidia-tls.so.1"),
        ("%s/lib/tls/libnvidia-tls.so.%s" % (base, version), "/usr/lib/libnvidia-tls.so.%s" % version),
        )

#
# Çomar methods
#

def enable():
    for src, dst in links:
        symlink(src, dst)

    # Create other links
    subprocess.call(["/sbin/ldconfig"])

    file("/var/lib/zorg/enabled_package", "w").write("xorg_video_%s" % driver.replace("-", "_"))
    file("/var/lib/zorg/kernel_module", "w").write(driver)

    subprocess.call(["/sbin/rmmod", "-s", "nvidia"])
    subprocess.call(["/sbin/modprobe", "-s", "nvidia"])

def disable():
    for src, dst in links:
        unlink(dst)

    symlink("../../std/extensions/libglx.so", "/usr/lib/xorg/modules/extensions/libglx.so")
    symlink("mesa/libGL.so.1.2", "/usr/lib/libGL.so.1.2")

    unlink("/var/lib/zorg/enabled_package")
    unlink("/var/lib/zorg/kernel_module")

    subprocess.call(["/sbin/rmmod", "-s", "nvidia"])

def getInfo():
    info = {
            "alias":        driver,
            "xorg-module":  "nvidia"
            }
    return info

def getDeviceOptions(busId, options):
    dev = getDeviceInfo(busId)
    if not dev:
        return options

    ignoredDisplays = []
    enabledDisplays = []
    horizSync = []
    vertRefresh = []
    metaModes = []
    rotation = ""
    orientation = ""
    order = ""

    for name, output in dev.outputs.items():
        if output.ignored:
            ignoredDisplays.append(name)
            continue

        if output.enabled:
            enabledDisplays.append(name)
        else:
            continue

        if name in dev.monitors:
            mon = dev.monitors[name]
            horizSync.append("%s: %s" % (name, mon.hsync))
            vertRefresh.append("%s: %s" % (name, mon.vref))

        if output.mode:
            if output.refresh_rate:
                metaModes.append("%s: %s_%s" % (name, output.mode, output.refresh_rate))

            metaModes.append("%s: %s" % (name, output.mode))
        else:
            metaModes.append("%s: nvidia-auto-select" % name)

        if output.rotation and not rotation:
            rotation = output.rotation

        if output.right_of:
            orientation = "%s RightOf %s" % (name, output.right_of)
            order = "%s, %s" % (output.right_of, name)
        elif output.below:
            orientation = "%s Below %s" % (name, output.below)
            order = "%s, %s" % (output.below, name)

    if ignoredDisplays:
        options["IgnoreDisplayDevices"] = ", ".join(ignoredDisplays)

    if horizSync:
        options["HorizSync"] = "; ".join(horizSync)
        options["VertRefresh"] = "; ".join(vertRefresh)

    if metaModes:
        options["MetaModes"] = ", ".join(metaModes)

    if rotation:
        options["Rotate"] = rotation

    if orientation:
        options["TwinView"] = "True"
        options["TwinViewOrientation"] = orientation
        options["TwinViewXineramaInfoOrder"] = order
    elif len(enabledDisplays) > 1:
        options["TwinView"] = "True"
        options["TwinViewOrientation"] = "%s Clone %s" % tuple(enabledDisplays[:2])

    return options
