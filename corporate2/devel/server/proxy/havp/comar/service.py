# -*- coding: utf-8 -*-
import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "HTTP Anti-Virus Proxy",
                 "tr": "HTTP Antivirüs Vekil Sunucusu"})

PIDFILE = "/var/run/havp/havp.pid"

MSG_NO_MAND_MOUNT = _({"en": "You need to mount filesystem with '-o mand'.",
                       "tr": "Dosya sisteminin '-o mand' parametresiyle bağlanmış olması gereklidir.",
                      })

@synchronized
def start():
    try:
        startService(command="/usr/sbin/havp",
                     donotify=True)
    except:
        fail(MSG_NO_MAND_MOUNT)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(pidfile=PIDFILE)
