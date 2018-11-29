from scapy.all import *
from scapy.layers.inet6 import *
import random

def randstring(length=10):
    valid_letters='0123456789abcdef'
    return ''.join((random.choice(valid_letters) for i in xrange(length)))

for i in range(20,30):
		source_ip = "2a01:d0:ffff:141::" + randstring(4) + ":" + randstring(4)
        p=IPv6(dst="2a00:d880:5:ae::e9ab", src=source_ip)/TCP(sport=RandShort(), dport=i, flags="S")
        send(p,verbose=False)
        print "Packets sent: " + str(i)

