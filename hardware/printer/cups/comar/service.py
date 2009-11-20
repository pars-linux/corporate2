from comar.service import *
import os

serviceType = "server"
serviceDefault = "on"
serviceDesc = _({"en": "CUPS Printer Server",
                 "tr": "CUPS Yazıcı Sunucusu"})
serviceConf = "cups"

@synchronized
def start():
    # FIXME: After avahi before hal
    startDependencies("avahi")

    # Load ppdev and lp drivers if wanted
    if config.get("LOAD_LP_MODULE") == "yes":
        os.system("modprobe -q lp")
        os.system("modprobe -q ppdev")

    startService(command="/usr/sbin/cupsd",
                 donotify=True)

    # Tell udevd to replay printer events
    # FIXME: This will be enabled after switching to the new system-config-printer
    """
    # One for low-level usb
    os.system("udevadm trigger --subsystem-match=usb \
                               --attr-match=bInterfaceClass=07 \
                               --attr-match=bInterfaceSubClass=01")
    # One for usblp backend
    os.system("udevadm trigger --subsystem-match=usb \
                               --property-match=DEVNAME=\"/dev/usb/lp*\"")
    """

@synchronized
def stop():
    stopService(pidfile="/var/run/cups/cupsd.pid",
                donotify=True)

def status():
    return isServiceRunning(pidfile="/var/run/cups/cupsd.pid")
