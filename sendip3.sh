#!/bin/sh

for k in $(seq 2000 2100)
do
	echo $k
	sendip -p ipv4 -is 10.0.0.18 -p udp -us $k -ud $k -d "UDP Test" -v 10.0.0.90
	sleep 0.1
done
