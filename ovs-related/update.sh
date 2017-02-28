#!/bin/sh

rmmod openvswitch
killall ovs-vswitchd
killall ovsdb-server
cd openvswitch-2.5.90
make uninstall
rm /usr/local/etc/openvswitch/conf.db
cd ..
./build.sh
