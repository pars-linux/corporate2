from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Zarafa Quota Monitor",
                 "tr": "Zarafa Kota Görüntüleyici"})
serviceDefault = "off"

PIDFILE = "/var/run/zarafa-monitor.pid"
MONITORCONFIG = "/etc/zarafa/monitor.cfg"

@synchronized
def start():
    import os
    os.environ["LC_ALL"] = "C"
    os.environ["LANG"] = "C"

    startService(command="/usr/bin/zarafa-monitor",
                 args="-c %s" % MONITORCONFIG,
                 makepid=True,
                 detach=True,
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
