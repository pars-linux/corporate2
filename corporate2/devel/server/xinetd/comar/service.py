# -*- coding: utf-8 -*-
from comar.service import *
import signal

serviceType = "server"
serviceDesc = _({"en": "eXtended InterNET Services Daemon",
                 "tr": "Genişletilmiş İnternet Hizmetleri Servisi (xinetd)"
                 })
serviceDefault = "off"

PIDFILE = "/var/run/xinetd.pid"

@synchronized
def start():
    startService(command="/usr/sbin/xinetd",
                 args="-pidfile %s -stayalive %s" % (PIDFILE, config.get("EXTRAOPTIONS")),
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def reload():
    stopService(command="/usr/sbin/xinetd",
                signal=signal.SIGHUP)

def status():
    return isServiceRunning(PIDFILE)
