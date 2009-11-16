#!/usr/bin/python

import os

def createNode(mode, uid, gid, minor, major, path):
    os.system("/bin/mknod --mode=%d %s c %d %d" % (mode, path, minor, major))
    os.system("/bin/chown %s:%s %s" % (uid, gid, path))

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    createNode(600, "root", "tty", 5, 1, "/opt/ptsp/lib/udev/devices/console")
    createNode(600, "root", "root" ,1, 11, "/opt/ptsp/lib/udev/devices/kmsg")
    createNode(666, "root", "root" ,1, 3, "/opt/ptsp/lib/udev/devices/null")
    createNode(666, "root", "root" ,1, 5, "/opt/ptsp/lib/udev/devices/zero")
    createNode(666, "root", "tty"  ,5, 2, "/opt/ptsp/lib/udev/devices/ptmx")
    createNode(666, "root", "tty"  ,5, 0, "/opt/ptsp/lib/udev/devices/tty")
    createNode(620, "root", "tty"  ,4, 1, "/opt/ptsp/lib/udev/devices/tty1")
    createNode(600, "root", "root" ,10, 130, "/opt/ptsp/lib/udev/devices/watchdog")
    createNode(660, "root", "dialout" ,108, 0, "/opt/ptsp/lib/udev/devices/ppp")
    createNode(600, "root", "root" ,10, 200, "/opt/ptsp/lib/udev/devices/net/tun")
    createNode(600, "root", "root" ,36, 0, "/opt/ptsp/lib/udev/devices/route")
    createNode(600, "root", "root" ,10, 200, "/opt/ptsp/lib/udev/devices/skip")
    #create permission
    os.system("/bin/chown root:dbus /opt/ptsp/usr/libexec/dbus-daemon-launch-helper")
    os.system("/bin/chmod 4750 /opt/ptsp/usr/libexec/dbus-daemon-launch-helper")

    # set hald permissions
    os.system("/bin/chown hal:hal /opt/ptsp/var/cache/hald")

    for root, dirs, files in os.walk("/opt/ptsp/var/db/comar3"):
        for name in files:
            if name.endswith(".pyc"):
                os.unlink(os.path.join(root, name))

    if os.path.exists("/opt/ptsp/lib/udev/devices/rtc"):
        os.unlink("/opt/ptsp/lib/udev/devices/rtc")

    try:
        os.symlink("/proc/self/fd", "/opt/ptsp/lib/udev/devices/fd")
    except OSError:
        pass

    try:
        os.symlink("/proc/self/fd/0", "/opt/ptsp/lib/udev/devices/stdin")
    except OSError:
        pass

    try:
        os.symlink("/proc/self/fd/1", "/opt/ptsp/lib/udev/devices/stdout")
    except OSError:
        pass

    try:
        os.symlink("/proc/self/fd/2", "/opt/ptsp/lib/udev/devices/stderr")
    except OSError:
        pass

    try:
        os.symlink("/proc/kcore", "/opt/ptsp/lib/udev/devices/core")
    except OSError:
        pass

