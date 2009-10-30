#!/usr/bin/python
# -*- coding: utf-8 -*-

# PulseAudio COMAR backend
import os
import subprocess

class PAConfig(object):
    def __init__(self):
        self.daemon_conf = "/etc/pulse/daemon.conf"
        if os.path.exists(self.daemon_conf):
            self.original_conf = open(self.daemon_conf, "r").readlines()

        d = self.get_effective_options()
        print d

    def get_effective_options(self):
        if self.original_conf:
            d = {}
            for line in [l for l in self.original_conf if not l.lstrip().startswith("#") and \
                                                          not l.lstrip().startswith(";")]:
                if "=" in line:
                    d[line.split("=")[0].strip()] = line.split("=")[1].strip()

            return d



def __get_resampling_methods():
    """ Returns the list of sampling methods supported by PulseAudio. """
    return os.popen("/usr/bin/pulseaudio --dump-resample-methods").read().strip().split("\n")

paconfig = PAConfig()
