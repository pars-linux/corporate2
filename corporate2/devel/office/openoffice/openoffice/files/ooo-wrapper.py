#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from subprocess import *

ooo_bin_path= "/opt/OpenOffice.org/bin/";
program=ooo_bin_path + os.path.basename(sys.argv[0])

#skip wrapper for those
blacklist = ['ooconfig', 'ootool', 'unopkg']

#TODO: Now we couldn't use command line parameters of soffice, this is because of kio-to-local
#For example 'ooimpress -h' doesn't work now :(

files = sys.argv[1:]
if files and not os.path.basename(program) in blacklist:
    for file in files:
        process = Popen(['kio-to-local', program, file])
else:
    process = Popen([program])

os.waitpid(process.pid,0)
