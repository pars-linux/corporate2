# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "InfraRed Controller Manager",
                 "tr": "Kızılötesi Denetleyici Yöneticisi"})

@synchronized
def start():
    reply = startService(command="/usr/sbin/lircd",
                         args=config.get("LIRCD_OPTS", ""),
                         pidfile="/var/run/lircd.pid",
                         donotify=True)
    if reply == 0 and config.get("USE_LIRCMD", "no") == "yes":
        startService(command="/usr/sbin/lircmd")

@synchronized
def stop():
    reply = stopService(pidfile="/var/run/lircd.pid",
                        donotify=True)
    if config.get("USE_LIRCMD", "no") == "yes":
        stopService(command="/usr/sbin/lircmd")

def status():
    return isServiceRunning("/var/run/lircd.pid")
