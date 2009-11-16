#!/bin/bash

port_pulse=4713
port_espeaker=16001
pulse_server=${DISPLAY%:*}

if [ "$pulse_server" != "" ]
then
    PULSE_SERVER=tcp:$pulse_server:$port_pulse
    ESPEAKER=$pulse_server:$port_espeaker
    export PULSE_SERVER
    export ESPEAKER
fi
