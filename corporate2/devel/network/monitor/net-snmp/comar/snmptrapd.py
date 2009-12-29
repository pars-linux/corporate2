# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "SNMPTrap Daemon",
                 "tr": "SNMPTrap Servisi"})
serviceConf = "snmptrapd"

@synchronized
def start():
    startService(command="/usr/sbin/snmptrapd",
                args="-p /var/run/snmptrapd.pid %s"  % config.get("SNMPTRAPD_FLAGS", ""),
                pidfile="/var/run/snmptrapd.pid",
                donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/snmptrapd.pid", donotify=True)

def status():
    return isServiceRunning("/var/run/snmptrapd.pid")
