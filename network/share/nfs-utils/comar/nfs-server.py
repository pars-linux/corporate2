# -*- coding: utf-8 -*-
from comar.service import *
from pardus import fstabutils
import signal
import os

serviceType = "server"
serviceDesc = _({"en": "NFS Server",
                 "tr": "NFS Sunucusu"})

serviceConf = "nfs"

ERR_INSMOD = _({"en": "Failed probing module %s",
               "tr": "%s modülü yüklenemedi",
             })

PROCNFSD_MOUNTPOINT = "/proc/fs/nfsd"
RQUOTAD_PATH = "/usr/sbin/rpc.rquotad"

IDMAPD_PIDFILE = "/var/run/rpc.idmapd.pid"
MOUNTD_PIDFILE = "/var/run/rpc.mountd.pid"
SVCGSSD_PIDFILE = "/var/run/rpc.svcgssd.pid"
RQUOTAD_PIDFILE = "/var/run/rpc.rquotad.pid"

# Parse the fstab file and determine whether we need quotad or not by searching
# mount option quota in any mount entry.
# If none, nfs conf.d file decides if it's needed.
def need_quotad():
    fstab = fstabutils.Fstab()
    for entry in fstab.get_entries():
        if "quota" in entry.get_fs_mntopts():
            return True

@synchronized
def start():
    startDependencies("nfs_common")

    if run("/sbin/modprobe -q nfsd"):
        fail(ERR_INSMOD % "nfsd")

    # Check if PROCNFSD_MOUNTPOINT is mounted
    if run("/bin/mountpoint -q %s" % PROCNFSD_MOUNTPOINT):
        run("/bin/mount -t nfsd nfsd %s" % PROCNFSD_MOUNTPOINT)

    run("/usr/sbin/exportfs -r")

    startService(command="/usr/sbin/rpc.nfsd",
                 args="%s %s" % (config.get("RPCNFSD_OPTIONS"), config.get("RPCNFSDCOUNT")),
                 donotify=True)

    if config.get("NEED_SVCGSSD") == "yes":
        startService(command="/usr/sbin/rpc.svcgssd",
                     args="-f %s" % config.get("RPCSVCGSSD_OPTIONS"),
                     donotify=True,
                     detach=True,
                     makepid=True,
                     pidfile=SVCGSSD_PIDFILE)

    # Start rpc.rquotad daemon here if its available
    if (config.get("NEED_QUOTAD") == "yes" or need_quotad()) and os.path.exists(RQUOTAD_PATH):
        startService(command=RQUOTAD_PATH,
                     args="-F %s" % config.get("RPCRQUOTAD_OPTIONS"),
                     donotify=True,
                     detach=True,
                     makepid=True,
                     pidfile=RQUOTAD_PIDFILE)

    # Reload rpc.idmapd
    if os.path.exists(IDMAPD_PIDFILE):
        os.kill(int(file(IDMAPD_PIDFILE).read().strip()), signal.SIGHUP)

    startService(command="/usr/sbin/rpc.mountd",
                 args="-F %s" % (config.get("RPCMOUNTD_OPTIONS")),
                 donotify=True,
                 detach=True,
                 makepid=True,
                 pidfile=MOUNTD_PIDFILE)

@synchronized
def stop():
    stopService(pidfile=MOUNTD_PIDFILE,
                donotify=True)

    stopService(pidfile=SVCGSSD_PIDFILE,
                donotify=True)

    stopService(pidfile=RQUOTAD_PIDFILE,
                donotify=True)

    if os.path.exists(RQUOTAD_PIDFILE):
        os.unlink(RQUOTAD_PIDFILE)

    stopService(command="/usr/sbin/rpc.nfsd",
                args="0",
                donotify=True)

    # Unexport all exported directories
    run("/usr/sbin/exportfs -au")

    if not run("/bin/mountpoint -q %s" % PROCNFSD_MOUNTPOINT):
        run("/usr/sbin/exportfs -f %s" % PROCNFSD_MOUNTPOINT)

def reload():
    # Re-export all exported directories
    run("/usr/sbin/exportfs -r")

def status():
    # ugly way of learning if the daemon is up and running.
    result = not run("/sbin/pidof nfsd")
    if config.get("NEED_SVCGSSD") == "yes":
        result = result and isServiceRunning(SVCGSSD_PIDFILE)
    if (config.get("NEED_QUOTAD") == "yes" or need_quotad()) and os.path.exists(RQUOTAD_PATH):
        result = result and isServiceRunning(RQUOTAD_PIDFILE)
    return result
