#!/bin/sh

sendip -v -p ipv4 -is 10.0.0.1 -id 10.0.0.3 -p icmp -d 0xcafecafecafe 10.0.0.1

