#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from comar.service import *

serviceDefault = "off"
serviceType = "server"
serviceDesc = _({"en": "Apache Tomcat Web Server 6",
                 "tr": "Apache Tomcat Web Sunucusu 6"
                 })

BASEDIR = "/opt/tomcat6"
PIDFILE = "/var/run/tomcat6.pid"

os.environ["LC_ALL"] = "C"
os.environ["CATALINA_PID"] = PIDFILE
os.environ["JAVA_HOME"] = "/opt/sun-jdk"

@synchronized
def start():
    startService(command="%s/bin/startup.sh" % BASEDIR,
                 donotify=True)

@synchronized
def stop():
    stopService(command = "%s/bin/shutdown.sh" % BASEDIR,
                # Without empty args, COMAR doesn't run the command above.
                args = "",
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
