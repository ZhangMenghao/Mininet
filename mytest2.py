#!/usr/bin/python
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import Intf
from mininet.log import setLogLevel, info

def myNetwork():

    net = Mininet( topo=None,
                   build=False)

    info( '*** Adding controller\n' )
    net.addController(name='c0',controller=RemoteController, ip='166.111.132.55', port=6653)

    info( '*** Add switches\n')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')

    info( '*** Add hosts\n')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2', ip='0.0.0.0')
    h3 = net.addHost('h3', ip='0.0.0.0')

    info( '*** Add links\n')
    net.addLink(h1, s3)
    net.addLink(h2, s4)
    net.addLink(h3, s5)
    net.addLink(s3, s4)
    net.addLink(s4, s5)

    info( '*** Starting network\n')
    net.start()
    os.system(">/var/lib/dhcp/dhcpd.leases")
    #os.system(">/var/lib/dhcp/dhcpd6.leases")
    os.system(">/var/lib/dhcp/dhclient.leases")
    #os.system(">/var/lib/dhcp/dhclient6.leases")
    h1.cmdPrint('killall dhcpd')
    h1.cmdPrint('dhcpd')
    #h1.cmdPrint('ip -6 addr add 3ffe:501:ffff:102::1/64 dev h1-eth0')
    #h1.cmdPrint('dhcpd -6 -cf /etc/dhcp/dhcpdv6.conf')
    #h2.cmdPrint('dhclient '+h2.defaultIntf().name)
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
