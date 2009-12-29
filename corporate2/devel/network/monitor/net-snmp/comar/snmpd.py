# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "SNMP Daemon",
                 "tr": "SNMP Servisi"})
serviceConf = "snmpd"

@synchronized
def start():
    startService(command="/usr/sbin/snmpd",
                args="-p /var/run/snmpd.pid %s"  % config.get("SNMPD_FLAGS", ""),
                pidfile="/var/run/snmpd.pid",
                donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/snmpd.pid", donotify=True)

def status():
    return isServiceRunning("/var/run/snmpd.pid")
