#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from subprocess import *

ooo_base_path = "/opt/OpenOffice.org/lib/ooo-3.2/";
ooo_program_path = ooo_base_path + "program/"
program=ooo_program_path+"s"+sys.argv[0].split('/')[-1][2:] # This transforms oowriter into swriter, oobase into sbase etc.
process=None

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
