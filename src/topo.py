from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

class MininetTopo(Topo):
    def build(self):
        # Add hosts to a topology
        self.addHost("h1")
        self.addHost("h3")
        # Add switchs to a topology
        self.addSwitch("s1")
        self.addSwitch("s2")
        # Add bidirectional links to a topology, and set bandwidth(Mbps)
        self.addLink("h1", "s1", bw=2)
        self.addLink("s1", "s2", bw=2)
        self.addLink("s2", "h3", bw=2)
 
if __name__ == '__main__':
    setLogLevel('info')
    # Create a topology
    topo = MininetTopo() 
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(
        topo = topo,
        controller = OVSController,
        link = TCLink)
    # Start a network
    net.start()
    # Use tcpdump to record packet in background
    print("start to record trace in h3 and h4")
    h3 = net.get("h3")
    h3.cmd("tcpdump -w ./output/h3_output.pcap &")

    CLI(net)
    net.stop()