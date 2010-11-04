serviceType = "server"
serviceDesc = _({"en": "Ahenk Agent",
                 "tr": "Ahenk Ajan"})
serviceConf = "ahenk_agent"

from comar.service import *

@synchronized
def start():
    import os
    os.environ["LC_ALL"] = "C"
    os.environ["LANG"] = "C"
    startService(command="/usr/bin/ahenk_agent",
                 args="%s -d" % config.get("OPTIONS", ""),
                 pidfile="/var/run/ahenk-agent.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/bin/ahenk_agent",
                args="-k",
                donotify=True)

def status():
    return isServiceRunning("/var/run/ahenk-agent.pid")
