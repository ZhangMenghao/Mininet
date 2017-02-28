#!/bin/sh

for k in $(seq 2000 2100)
do
	echo $k
	sendip -p ipv4 -is 10.0.0.152 -p udp -us 100 -ud 100 -d "UDP Test" -v 10.0.0.1
	sleep 1
done
