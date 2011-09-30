# -*- coding: utf-8 -*-
import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "A Mail Virus Scanner",
                 "tr": "E-posta Virus Tarayıcısı"})

PIDFILE = "/var/run/amavisd/amavisd.pid"

@synchronized
def start():
    startService(command="/usr/sbin/amavisd",
                 args="-c /etc/amavis/amavisd.conf",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(pidfile=PIDFILE)
