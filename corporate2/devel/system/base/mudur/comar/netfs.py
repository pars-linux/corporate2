#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *
import os

from pardus.fstabutils import Fstab

serviceType = "local"
serviceDefault = "conditional"
serviceDesc = _({"en": "Remote Filesystem Mounter",
                 "tr": "Uzak Dosyasistemi Bağlayıcı"})

DATAFILE = "/var/run/netfs.status"

MSG_NM_NOT_RUNNING = _({"en": "NetworkManager service is not running",
                        "tr": "NetworkManager hizmeti çalışmıyor",
                       })

@synchronized
def start():
    # Mount all remote filesystems
    if run("/usr/bin/nm-online -x") != 0:
        # NM is not running
        fail(MSG_NM_NOT_RUNNING)

    fstab = Fstab()
    for entry in fstab:
        if entry.is_remote_mount()



@synchronized
def stop():
    # Unmount all remote filesystems

@synchronized
def ready():
    status = is_on()
    remote_fs_exist = False

    fstab = Fstab()
    for entry in fstab:
        if entry.is_remote_mount():
            remote_fs_exist = True
            break

    # Will only run if there are any remote mounts in
    # fstab file.
    if status == "on" or (status == "conditional" and \
            remote_fs_exist):
        start()

def status():
    fstab = Fstab()
    for entry in fstab:
        if entry.is_remote_mount() and entry.is_mounted():
            return True
