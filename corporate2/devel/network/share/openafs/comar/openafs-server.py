# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "OpenAFS BOS server",
                 "tr": "OpenAFS BOS sunucusu"})
serviceConf = "openafs-server"

PID_FILE = "/var/run/bosserver.pid"

@synchronized
def start():
    startService(command="/usr/sbin/bosserver",
                 args="-nofork %s" % (config.get("BOSSERVER_OPTIONS", "")),
                 pidfile=PID_FILE,
                 makepid=True,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    # This kindly kills all server processes
    run("/usr/bin/bos shutdown localhost -localauth -wait")

    stopService(pidfile=PID_FILE,
                donotify=True)

    if os.path.exists(PID_FILE):
        os.unlink(PID_FILE)

def status():
    return isServiceRunning(pidfile=PID_FILE)
