# -*- coding: utf-8 -*-
from comar.service import *

serviceType="server"
serviceDesc = _({"en": "TPM Emulator",
                 "tr": "TPM Öykünücüsü"})

def load_module():
    run("/sbin/modprobe tpmd_dev")

@synchronized
def start():
    load_module()
    startService(command="/usr/sbin/tpmd",
                 args="save",
                 chuid="tss",
                 detach=True,
                 donotify=True)


@synchronized
def stop():
    stopService(command="/usr/sbin/tpmd",
                user="tss",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/sbin/tpmd")
