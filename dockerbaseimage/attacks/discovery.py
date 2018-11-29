from scapy.all import *
from scapy.layers.inet6 import *
import random

valid_host_address='0123456789abcdef'

for i in range(14):
        target_ip = "2a02:16:33::" + valid_host_address[i]
        p=IPv6(dst=target_ip)/ICMPv6EchoRequest()
        send(p,verbose=False)
        print "Packets sent: " + str(i)
