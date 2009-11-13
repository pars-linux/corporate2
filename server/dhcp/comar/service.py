# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "DHCP Daemon",
                 "tr": "DHCP Servisi"})
serviceConf = "dhcpd"

@synchronized
def start():
    startService(command="/usr/sbin/dhcpd",
                 args="%s %s" % (config.get("DHCPD_OPTS", ""), config.get("DHCPD_IFACE", "")),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/dhcpd",
                pidfile="/var/run/dhcpd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/dhcpd.pid")
