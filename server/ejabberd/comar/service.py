from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "Ejabberd Jabber Server",
                 "tr": "Ejabberd Jabber Sunucusu"})

@synchronized
def start():
    startService(command="/usr/sbin/ejabberdctl",
            args="start",
            donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/ejabberdctl",
        args="stop",
        donotify=False)

    time.sleep(3)
    stopService(command="/usr/bin/pkill",
        args="-u ejabberd -f epmd",
        donotify=False)

def status():
    return run("/usr/sbin/ejabberdctl status") == 0
