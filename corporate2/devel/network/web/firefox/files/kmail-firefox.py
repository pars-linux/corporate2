#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import cgi
import subprocess

def usage():
    print "Usage: kmail-firefox mailto:email@adress[?subject=sbj&cc=another@address&bcc=another@address&body=body]"

if len(sys.argv) != 2:
    usage()
    sys.exit(1)

param = sys.argv[1]

if not param.startswith("mailto:"):
    usage()
    sys.exit(1)

command = ["kmail"]
kmailParams = {"subject": "-s", "cc": "-c", "bcc": "-b", "body": "--body"}

#strip mailto: part
param = param[len("mailto:"):]
if param.find("?") == -1:
    command.append(param)
else:
    to, hede, url = param.partition("?")
    command.append(to)
    mailDict = cgi.parse_qs(url)
    if len(mailDict.keys()) > 5:
        usage()
        sys.exit(1)

    for key in mailDict.keys():
        try:
            command.extend([kmailParams[key.lower()], mailDict[key][0]])
        except KeyError:
            #ignore wrong keys
            pass

process = subprocess.call(command)
