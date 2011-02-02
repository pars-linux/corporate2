#!/bin/sh
#
# Customized agents startup file

if [ -x /usr/bin/gpg-agent -a -z "$GPG_AGENT_INFO" ]; then
  eval "$(/usr/bin/gpg-agent --daemon)"
fi

if [ -x /usr/bin/ssh-agent -a -z "$SSH_AGENT_PID" ]; then
  eval "$(/usr/bin/ssh-agent -s)"
fi
