#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Original work from NM
# Copyright (C) 2008 Novell, Inc.
# Copyright (C) 2008 Red Hat, Inc.
#
# Python implementation
# Copyright (C) 2009 TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import os
import sys
import stat
import errno
import fcntl
import signal
import syslog
import termios
import hashlib
import subprocess

options = """\
lock
crtscts
noipdefault
defaultroute
noauth
usehostname
usepeerdns
linkname %s
user %s
%s
"""

# Global integer for holding pppd pid
pppd_pid = 0

def sigusr1_handler(signum, frame):
    # Caught SIGUSR, send SIGTERM to pppd
    os.kill(pppd_pid, signal.SIGTERM)

def ppp_exit_code(status):

    messages = [
        "Fatal pppd error",
        "pppd options error",
        "No root priv error",
        "No ppp module error",
        "pppd received a signal",
        "Serial port lock failed",
        "Serial port open failed",
        "Connect script failed",
        "Pty program error",
        "PPP negotiation failed",
        "Peer didn't authenticatie itself",
        "Link idle: Idle Seconds reached.",
        "Connect time limit reached.",
        "Callback negotiated, call should come back.",
        "Lack of LCP echo responses",
        "A modem hung up the phone",
        "Loopback detected",
        "The init script failed",
        "Authentication error.\nWe failed to authenticate ourselves to the peer.\nMaybe bad account or password?"]

    try:
        msg = messages[status-1]
    except IndexError:
        msg = "Unknown error"

    return msg


def create_pppd_cmd_line(device, ppp_name="", pppoe=False):
    pppd = os.popen("which pppd").read().strip()

    if "no pppd" in pppd:
        # Couldn't find pppd binary, fail
        return False

    # NM *should* handle setting the default route
    cmdline = ("%s nodetach lock nodefaultroute" % pppd).split()

    if ppp_name:
        cmdline.append("user %s" % ppp_name)

    if pppoe:
        # Not really implemented, a placeholder..
        cmdline.extend(["plugin", "rp-pppoe.so"])
    else:
        cmdline.extend([device, "noipdefault"])

    # noauth by default, because we certainly don't have any information
    # with which to verify anything the peer gives us if we ask it to
    # authenticate itself, which is what 'auth' really means.
    cmdline.append("noauth")

    # Always ask for a DNS, we don't have to use them if the connection
    # overrides the returned servers.
    cmdline.append("usepeerdns")

    cmdline = " ".join(cmdline)

    return cmdline


def start_pppd(device, ppp_name="", pppoe=False):

    def preexec_fork_handler():
        os.umask(022)
        try:
            tty_fd = os.open("/dev/tty", os.O_RDWR)
            fcntl.ioctl(tty_fd, termios.TIOCNOTTY)
            os.close(tty_fd)
        except OSError:
            pass

        # Close standart IO channels
        devnull_fd = os.open(os.devnull, os.O_RDWR)
        os.dup2(devnull_fd, 0)
        os.dup2(devnull_fd, 1)
        os.dup2(devnull_fd, 2)

        # Detach from the process group
        os.setsid()

    # Make sure /dev/ppp exists
    if not stat.S_ISCHR(os.stat("/dev/ppp").st_mode):
        # No device node /dev/ppp
        os.system("/sbin/modprobe ppp_generic")

    cmd = create_pppd_cmd_line(device, ppp_name=ppp_name, pppoe=pppoe)
    syslog.syslog(syslog.LOG_DEBUG, "DEBUG: Spawning %s" % cmd)

    # Spawn pppd and return immediately with the pid
    return subprocess.Popen(cmd.split(),
                            close_fds=True,
                            preexec_fn=preexec_fork_handler,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE).pid


def notify_backend(package, status):
    pass


def trace_pppd(pid):
    syslog.syslog(syslog.LOG_DEBUG, "pppd pid is %d" % pid)

    while True:
        try:
            # Wait for pppd
            status = os.waitpid(pid, 0)[1]
        except OSError, e:
            if e.errno == errno.EINTR:
                continue

        if os.WIFEXITED(status):
            msg = ppp_exit_code(os.WEXITSTATUS(status))
            err = "ppp pid %d exited with error: %s (%d)" % (pid, msg, status)
            syslog.syslog(syslog.LOG_DEBUG, "%s, should notify the backend" % err)
        elif os.WIFSIGNALED(status):
            sig = os.WTERMSIG(status)
            syslog.syslog(syslog.LOG_DEBUG, "Terminated by signal %d" % sig)

        break

    # pppd is terminated, notify the backend


#############

if __name__ == "__main__":
    # Register SIGUSR for asynchronous state changes from backend
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGUSR1, sigusr1_handler)

    if len(sys.argv) < 4:
        print "Usage: %s <backend> <connection> <device_node>" % sys.argv[0]
        sys.exit(1)

    device = sys.argv[3]
    if not stat.S_ISCHR(os.stat(device).st_mode):
        # No character device
        sys.exit(2)

    backend = sys.argv[1]
    profile = sys.argv[2]

    syslog.openlog("comar-pppd", 0, syslog.LOG_DAEMON)
    syslog.syslog(syslog.LOG_DEBUG, "device is %s" % device)

    # Create pidfile
    uuid = hashlib.sha1(backend+profile).hexdigest()
    pidfile = "/var/run/comar-pppd-%s.pid" % uuid
    f = open(pidfile, "w")

    # Start pppd, dump our own and pppd's pid into it
    pppd_pid = start_pppd(device)

    f.write("%d,%d" % (os.getpid(), pppd_pid))
    f.close()

    # Wait for pppd to terminate
    trace_pppd(pppd_pid)

    # Cleanup pidfile upon exit
    try:
        os.unlink(pidfile)
    except:
        pass
