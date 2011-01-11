# -*- coding: utf-8 -*-
from comar.service import *
import time

serviceType = "server"
serviceDesc = _({"en": "DHCPv6 Daemon",
                 "tr": "DHCPv6 Servisi"})

serviceConf = "dhcpd6"

MSG_NM_NOT_RUNNING = _({"en": "NetworkManager service is not running",
                        "tr": "NetworkManager hizmeti çalışmıyor",
                       })

PIDFILE = "/var/run/dhcpd6.pid"
TIMEOUT = config.get("TIMEOUT", 5)

@synchronized
def start():
    startDependencies("NetworkManager")
    if run("/usr/bin/nm-online -q -t %s" % TIMEOUT) != 0:
        # NM is not running
        fail(MSG_NM_NOT_RUNNING)

    startService(command="/usr/sbin/dhcpd",
                 args="-6 -cf %s %s %s" % (config.get("DHCPD_CONF", "/etc/dhcp/dhcpd.conf"), config.get("DHCPD_ARGS", ""), config.get("INTERFACES", "")),
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
