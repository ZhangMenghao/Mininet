"""custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
	rightHost2 = self.addHost ( 'h3' )
	leftHost2 = self.addHost( 'h4' )
        Switch4 = self.addSwitch( 's4' )
	Switch5 = self.addSwitch( 's5' )
	Switch6 = self.addSwitch( 's6' )
	Switch7 = self.addSwitch( 's7' )
	Switch8 = self.addSwitch( 's8' )
        # Add links
        self.addLink( leftHost, Switch4 )
	self.addLink( leftHost2, Switch6 )
	self.addLink( Switch4, Switch5 )
	self.addLink( Switch5, Switch8 )
	self.addLink( Switch4, Switch6 )
        self.addLink( Switch6, Switch7 )
	self.addLink( Switch7, Switch8 )
        self.addLink( Switch8, rightHost )
	self.addLink( Switch8, rightHost2 )


topos = { 'mytopo': ( lambda: MyTopo() ) }

