#!/bin/bash
set +e
SSH_OPTIONS=" -i /etc/tunnel/id_rsa"
# Always assume initial connection will be successful
export AUTOSSH_GATETIME=0
# Disable echo service, relying on SSH exiting itself
export AUTOSSH_PORT=0
#to test, use (check out man ssh for explanation of options:
#autossh -vv -- $SSH_OPTIONS -o 'ControlPath none' -R 10101:localhost:22 -p 22022 autossh@grinnan.com -N > /var/user_sshlog.out 2> /var/log/user_ssh_error.out &
#once proven, use (and rem out previous command):
autossh -f -- $SSH_OPTIONS -o 'ControlPath none' -R 21312:localhost:22 -p 22022 autossh@grinnan.com -N 2> /var/log/user_ssh_error.out
