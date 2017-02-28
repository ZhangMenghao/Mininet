#!/bin/sh
for k in $(seq 1 2000)
do
	echo $k
	sendip -p ipv4 -is 10.0.0.1 -p udp -us $k -ud $k -d "UDP Test" -v 10.0.0.5
	sleep 0.05
done
