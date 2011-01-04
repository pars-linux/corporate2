#!/usr/bin/python

import os
import subprocess
import time

PIDFILE = "/var/run/mysqld/mysqld.pid"
SOCKFILE = "/var/run/mysqld/mysqld.sock"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R mysql:mysql /var/lib/mysql")
    os.system("/bin/chmod -R 0750 /var/lib/mysql")

    os.system("/bin/chown -R mysql:mysql /var/log/mysql")
    os.system("/bin/chmod 0750 /var/log/mysql")
    os.system("/bin/chmod -R 0660 /var/log/mysql/*")

    os.system("/bin/chown -R mysql:mysql /var/run/mysqld")
    os.system("/bin/chmod -R 0755 /var/run/mysqld")

    # On first install...
    if not os.path.exists("/var/lib/mysql/mysql"):
        # Create the database
        subprocess.call(['/usr/bin/mysql_install_db', '--datadir=/var/lib/mysql', '--user=mysql'])

        # First start.
        subprocess.call(['/usr/sbin/mysqld', '--user=mysql', '--skip-grant-tables', '--basedir=/usr', '--datadir=/var/lib/mysql', '--skip-innodb', '--max_allowed_packet=8M', '--net_buffer_length=16K', '--socket=%s' % SOCKFILE, '--pidfile=%s' % PIDFILE])


        # Sleep for a while
        time.sleep(2)

        # Stop MySQL
        if os.path.exists(PIDFILE):
            try:
                os.kill(int(open(PIDFILE, "r").read().strip()), 15)
            except:
                pass
