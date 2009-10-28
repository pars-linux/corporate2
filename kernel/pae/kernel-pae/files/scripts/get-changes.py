#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

curdir = os.getcwd()
basename = os.path.basename(curdir)
flavour = curdir.partition("kernel/")[-1].split("/")[0]
if "module" in basename:
    default = "../../../default/drivers/%s" % basename.replace("-%s" % flavour, "")

else:
    default = "../../default/kernel"

print default

os.system("svn up")
rev = os.popen("svn info | grep 'Last Changed Rev: '").read().split("Last Changed Rev:")[1].strip()
os.system("svn up %s" % default)
os.system("svn merge -r %d:HEAD %s ." % (int(rev)+1, default))
