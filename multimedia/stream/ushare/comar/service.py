from comar.service import *
import signal

serviceType = "local"
serviceDesc = _({"en": "uShare UPnP A/V Media Server",
                 "tr": "uShare UPnP Ses/Görüntü Ortam Sunucu"})
serviceDefault = "off"

pidfile = "/var/run/ushare.pid"
command = "/usr/bin/ushare"

@synchronized
def start():
    startService(command=command,
                 args="--cfg=/etc/ushare.conf -d",
                 pidfile=pidfile,
                 detach=True,
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=pidfile,
                donotify=True)

def reload():
    stopService(command=command,
                signal=signal.SIGHUP)

def status():
    return isServiceRunning(pidfile)
