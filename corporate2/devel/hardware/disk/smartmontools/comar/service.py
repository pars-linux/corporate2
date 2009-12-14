from comar.service import *

serviceType="server"
serviceDesc = _({"en": "S.M.A.R.T. monitoring daemon",
                 "tr": "S.M.A.R.T. izleme servisi"})

serviceConf = "smartd.conf"

@synchronized
def start():
    startService(command="/usr/sbin/smartd",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/smartd",
                donotify=True)

def reload():
    # FIXME: That's bad.
    run("/usr/bin/killall -HUP smartd")

def status():
    return isServiceRunning(command="/usr/sbin/smartd")
