# -*- coding: utf-8 -*-
import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "BIND Daemon (chroot)",
                 "tr": "BIND Servisi (chroot)"})
serviceConf = "named"
chrootDir = "/var/named/chroot"

@synchronized
def start():
    startService(command="/usr/sbin/named",
                 args="-u named -n %s %s -t %s" % (config.get("CPU", "1"),
                                                         config.get("OPTIONS", ""),
                                                         chrootDir),
                 pidfile="%s/var/run/named/named.pid" % chrootDir,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="%s/var/run/named/named.pid" % chrootDir,
                donotify=True)

def status():
    return isServiceRunning("%s/var/run/named/named.pid" % chrootDir)
