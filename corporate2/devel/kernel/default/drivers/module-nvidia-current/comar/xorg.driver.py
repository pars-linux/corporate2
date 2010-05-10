# -*- coding: utf-8 -*-

import os
import subprocess

from zorg.config import getDeviceInfo

version = "195.36.24"
driver = "nvidia-current"
base = "/usr/lib/xorg/%s" % driver

BLACKLIST_CONF = "/etc/modprobe.d/blacklist-nouveau.conf"
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

links = (
    # X driver
    ("%s/drivers/nvidia_drv.so" % base, "/usr/lib/xorg/modules/drivers/nvidia_drv.so"),

    # glx extension
    ("%s/extensions/libglx.so.%s" % (base, version), "/usr/lib/xorg/modules/extensions/libglx.so"),

    # nvidia-tls library
    ("libnvidia-tls.so.1", "/usr/lib/libnvidia-tls.so"),
    ("libnvidia-tls.so.%s" % version, "/usr/lib/libnvidia-tls.so.1"),
    ("%s/lib/tls/libnvidia-tls.so.%s" % (base, version), "/usr/lib/libnvidia-tls.so.%s" % version),

    # GL library
    ("%s/lib/libGL.so.%s" % (base, version), "/usr/lib/libGL.so.1.2"),

    ("libGLcore.so.1", "/usr/lib/libGLcore.so"),
    ("libGLcore.so.%s" % version, "/usr/lib/libGLcore.so.1"),
    ("%s/lib/libGLcore.so.%s" % (base, version), "/usr/lib/libGLcore.so.%s" % version),

    # XvMC library
    ("%s/lib/libXvMCNVIDIA.so.%s" % (base, version), "/usr/lib/libXvMCNVIDIA.so.%s" % version),
    ("libXvMCNVIDIA.so.%s" % version, "/usr/lib/libXvMCNVIDIA.so"),

    # VDPAU driver
    ("%s/lib/vdpau/libvdpau_nvidia.so.%s" % (base, version), "/usr/lib/vdpau/libvdpau_nvidia.so.1"),

    # nvidia-cfg library
    ("libnvidia-cfg.so.1", "/usr/lib/libnvidia-cfg.so"),
    ("libnvidia-cfg.so.%s" % version, "/usr/lib/libnvidia-cfg.so.1"),
    ("%s/lib/libnvidia-cfg.so.%s" % (base, version), "/usr/lib/libnvidia-cfg.so.%s" % version),

    # Cuda library
    ("libcuda.so.1", "/usr/lib/libcuda.so"),
    ("libcuda.so.%s" % version, "/usr/lib/libcuda.so.1"),
    ("%s/lib/libcuda.so.%s" % (base, version), "/usr/lib/libcuda.so.%s" % version),
)

#
# Çomar methods
#

def enable():
    unlink("/usr/lib/libvdpau_nvidia.so")
    for src, dst in links:
        symlink(src, dst)

    # Create other links
    subprocess.call(["/sbin/ldconfig"])

    echo(BLACKLIST_CONF, "blacklist nouveau")
    for kernel in os.listdir("/etc/kernel"):
        subprocess.call(["/sbin/mkinitramfs", "-t", kernel])

    echo(ZORG_ENABLED_PACKAGE, "xorg_video_%s" % driver.replace("-", "_"))
    echo(ZORG_KERNEL_MODULE, driver)

    subprocess.call(["/sbin/rmmod", "-s", "nvidia"])
    subprocess.call(["/sbin/modprobe", "-s", "nvidia"])

def disable():
    unlink("/usr/lib/libvdpau_nvidia.so")
    for src, dst in links:
        unlink(dst)

    symlink("../../std/extensions/libglx.so", "/usr/lib/xorg/modules/extensions/libglx.so")
    symlink("mesa/libGL.so.1.2", "/usr/lib/libGL.so.1.2")

    unlink(BLACKLIST_CONF)
    for kernel in os.listdir("/etc/kernel"):
        subprocess.call(["/sbin/mkinitramfs", "-t", kernel])

    unlink(ZORG_ENABLED_PACKAGE)
    unlink(ZORG_KERNEL_MODULE)

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
