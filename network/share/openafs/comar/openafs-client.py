# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "OpenAFS Daemon",
                 "tr": "OpenAFS Hizmeti"})
serviceConf = "openafs-client"

CACHEINFO       = "/etc/openafs/cacheinfo"

ERR_DRIVER_LOAD = _({"en": "Failed loading the afs kernel module",
                     "tr": "afs çekirdek sürücüsü yüklenemedi",
                     })

ERR_MP_UNMOUNT = _({"en": "Failed unmounting %s",
                    "tr": "%s bağlama noktası ayrılamadı",
                    })

ERR_DRIVER_UNLOAD = _({"en": "Unloading afs kernel module failed",
                       "tr": "afs çekirdek sürücüsü kaldırılamadı",
                      })

def choose_afsd_options():
    # Determine the choosen cachesize
    cachesize = 0
    options = ""
    if os.path.exists(CACHEINFO):
        try:
            cachesize = open(CACHEINFO, "r").read().strip().split(":")[-1]
        except IndexError:
            pass

    if config.get("OPTIONS") == "AUTOMATIC":
        if cachesize < 131072:
            options = config.get("SMALL")
        elif cachesize < 524288:
            options = config.get("MEDIUM")
        elif cachesize < 1048576:
            options = config.get("LARGE")
        elif cachesize < 2097152:
            options = config.get("XLARGE")
        else:
            options = config.get("XXLARGE")

    # Construct afsd options
    if config.get("ENABLE_AFSDB", "yes") == "yes":
        options += " -afsdb"
    if config.get("ENABLE_DYNROOT", "yes") == "yes":
        options += " -dynroot"

    return options

def cleanstart():
    # Start openafs-server first
    startDependencies("openafs_server")

    # Get the mountpoint
    MOUNTPOINT = config.get("MOUNTDIR", "/afs")

    # Make sure the mointpoint exists
    if not os.path.exists(MOUNTPOINT):
        os.makedirs(MOUNTPOINT)

    if os.system("modprobe -q libafs") != 0:
        fail(ERR_DRIVER_LOAD)

    options = choose_afsd_options()

    startService(command="/usr/sbin/afsd",
                 args="%s -mountdir %s" % (options, MOUNTPOINT),
                 donotify=True)

@synchronized
def start():
    # Check if the openafs kernel module is loaded -> attempt unload
    if os.path.exists("/proc/fs/openafs"):
        if os.system("modprobe -r libafs") != 0:
            fail(ERR_DRIVER_UNLOAD)
        else:
            # Unloaded
            cleanstart()

    else:
        cleanstart()

@synchronized
def stop():
    # Three stage: unmount / stop / unload module

    # Get the mountpoint
    MOUNTPOINT = config.get("MOUNTDIR", "/afs")

    if os.system("umount %s" % MOUNTPOINT) != 0:
        fail(ERR_MP_UNMOUNT % MOUNTPOINT)
    else:
        stopService(command="/usr/sbin/afsd",
                    args="-shutdown",
                    donotify=True)

    if os.path.exists("/proc/fs/openafs"):
        if os.system("modprobe -r libafs") != 0:
            fail(ERR_DRIVER_UNLOAD)

    # Clean up: remove the mountpoint if it's an empty directory
    if os.path.exists(MOUNTPOINT) and len(os.listdir(MOUNTPOINT)) == 0:
        try:
            os.removedirs(MOUNTPOINT)
        except:
            fail(ERR_MP_PRUNE)

def status():
    return isServiceRunning(command="/usr/sbin/afsd")
