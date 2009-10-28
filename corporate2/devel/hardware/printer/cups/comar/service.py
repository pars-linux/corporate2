from comar.service import *
import os

serviceType = "server"
serviceDefault = "on"
serviceDesc = _({"en": "CUPS Printer Server",
                 "tr": "CUPS Yazıcı Sunucusu"})
serviceConf = "cups"

@synchronized
def start():
    # FIXME: After avahi before hal
    startDependencies("avahi")

    # Load ppdev and lp drivers if wanted
    if config.get("LOAD_LP_MODULE") == "yes":
        os.system("modprobe -q lp")
        os.system("modprobe -q ppdev")

    startService(command="/usr/sbin/cupsd",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/cups/cupsd.pid",
                donotify=True)

def status():
    return isServiceRunning(pidfile="/var/run/cups/cupsd.pid")
