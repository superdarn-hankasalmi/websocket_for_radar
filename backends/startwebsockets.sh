#!/bin/bash
cd websockify/websockify
start_port=9000
web_address=143.210.44.13
for i in {0..1}
#do
    #screen -d -m -S $((start_port + 100 + i)) websockify -v --cert=/home/cassie/backends/certs/finlandCA.pem --key=/home/cassie/backends/certs/finlandCA.key $((start_port + 100 + i)) $web_address:$((start_port + i)) >>/dev/null &

#done

do
    screen -d -m -S $((start_port + 100 + i)) websockify -v $((start_port + 100 + i)) $web_address:$((start_port + i)) >>/dev/null &

done
