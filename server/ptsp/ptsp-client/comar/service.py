# -*- coding: utf-8 -*-
from comar.service import *
import os
import ConfigParser

serviceType = "script"
serviceDesc = "ptsp_client"
serviceDefault = "on"
configFile = "/etc/pts-client.conf"

MSG_ERR_FILENOTEXIST = _({"en": "File %s does not exist.",
                          "tr": "%s dosyası mevcut değil.",
                          })
MSG_ERR_PLAUNOTSTRT = _({"en": "PulseAudio is not starting.",
                         "tr": "PulseAudio başlamıyor.",
                         })
MSG_ERR_NOTTHIN = _({"en": "Not thin setup.",
                     "tr": "İnce kurulum değil.",
                     })

def configure():
    if run("/usr/bin/zorg --probe") != 0:
        fail("Not starting as zorg returned an error")

def has_thin():
    return "thin" in open("/proc/cmdline", "r").read()

def get_xserver():
    if not os.path.exists(configFile):
        fail(MSG_ERR_FILENOTEXIST % configFile)

    cp = ConfigParser.ConfigParser()
    cp.read(configFile)

    try:
        return cp.get("Server", "xserver")
    except ConfigParser.NoOptionError:
        fail("XSERVER not defined in %s" % configFile)

def start_pulse():
    if run("/usr/bin/pulseaudio --system -D") != 0:
        fail(MSG_ERR_PLAUNOTSTRT)

def start():
    if not has_thin():
        fail(MSG_ERR_NOTTHIN)

    startDependencies("acpid")
    startDependencies("hal")
    configure()
    loadEnvironment()
    os.environ["XAUTHLOCALHOSTNAME"]=os.uname()[1]
    os.environ["HOME"]="/root"
    os.environ["USER"]="root"
    start_pulse()

    while True:
        run("X -query %s vt7 -br" % get_xserver())

def stop():
    if not has_thin():
        fail(MSG_ERR_NOTTHIN)

    if 0 == run("/usr/bin/killall X"):
        notify("System.Service.changed", "stopped")
