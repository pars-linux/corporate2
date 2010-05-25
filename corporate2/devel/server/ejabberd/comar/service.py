from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Ejabberd Jabber Server",
                 "tr": "Ejabberd Jabber Sunucusu"})

@synchronized
def start():

    startService(command="/usr/sbin/ejabberdctl",
            args="start",
            chuid="ejabberd",
            donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/ejabberdctl",
        args="stop",
        chuid="ejabberd",
        donotify=False)
    time.sleep(3)
    stopService(command="/usr/bin/pkill",
        args="-u ejabberd -f epmd",
        donotify=False)

def status():
    ret = run("/usr/bin/sudo -u ejabberd /usr/sbin/ejabberdctl status")
    if ret != 0:
        return False
    return True
