from comar.service import *
import os

serviceType = "server"
serviceDefault = "off"
serviceDesc = _({"en": "CUPS Printer Server",
                 "tr": "CUPS Yazıcı Sunucusu"})
serviceConf = "cups"

PIDFILE = "/var/run/cupsd.pid"

@synchronized
def start():
    startService(command="/usr/sbin/cupsd",
                 donotify=True)

@synchronized
def reload():
    if os.path.exists(PIDFILE):
        # 1 is SIGHUP
        os.kill(int(open(PIDFILE, "r").read().strip()), 1)

@synchronized
def stop():
    stopService(pidfile=PIDFILE, donotify=True)

def status():
    return isServiceRunning(pidfile=PIDFILE)
