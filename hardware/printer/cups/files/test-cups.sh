#!/bin/bash

export LC_ALL=C

# Remove all queues
python -c "import cups;c=cups.Connection();map(c.deletePrinter, c.getPrinters().keys())"

# Stop CUPS
service cups stop

# Completely remove CUPS
pisi rm cups --ignore-dep -vd
rm -rf /etc/cups

pisi bi pspec.xml -vd
pisi it cups-*.pisi --reinstall -vd
pisi it ghostscript --reinstall --ignore-dep -vd
service cups start
