from comar.service import *

serviceType = "local"
serviceDefault = "on"
serviceDesc = _({"en": "PC/SC SmartCard Reader Service",
                 "tr": "PC/SC Akıllı Kart Okuyucu Servisi"})

PIDFILE = "/var/run/pcscd/pcscd.pid"

@synchronized
def start():
    startService(command="/usr/sbin/pcscd",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(pidfile=PIDFILE)
