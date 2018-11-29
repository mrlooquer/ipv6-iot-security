from scapy.all import *
from scapy.layers.inet6 import *
import random

def randstring(length=10):
    valid_letters='0123456789abcdef'
    return ''.join((random.choice(valid_letters) for i in xrange(length)))

for i in range(20,30):
    source_ip = "2a02:16:33::" + randstring(4) + ":" + randstring(4)+ ":" + randstring(4) + ":" + randstring(4)
    destination_ip = "2a02:16:33::"  + randstring(4) + ":" + randstring(4) + ":" + randstring(4) + ":" + randstring(4)
    p=IPv6(dst=destination_ip, src=source_ip)/ICMPv6EchoRequest()
    send(p,iface="eth0",verbose=False)
    print "Packets sent: " + str(i)
