# -*- coding: utf-8 -*-
import os
import subprocess
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Squid Proxy Daemon",
                 "tr": "Squid Vekil Servisi"})
serviceConf = "squid"

def check_cache():
    if not os.path.exists("/var/cache/squid/00"):
            subprocess.call(["/usr/sbin/squid"], ["-z"])

@synchronized
def start():
    check_cache()
    startService(command="/usr/sbin/squid",
                 args="%s" % config.get("SQUID_OPTS"),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/squid",
                args="-k shutdown",
                donotify=True)

def reload():
    stopService(command="/usr/sbin/squid",
                args="-k reconfigure")

def status():
    return isServiceRunning("/var/run/squid.pid")
