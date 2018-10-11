#!/usr/bin/env python

import dpkt
import sys
import socket
from dpkt.compat import compat_ord

counter=0
ipcounter=0
tcpcounter=0
udpcounter=0

filename='temp.pcap'

for ts, pkt in dpkt.pcap.Reader(open(filename,'r')):
  counter += 1
  eth = dpkt.ethernet.Ethernet(pkt)
  ip = eth.data
  tcp = ip.data
  ipcounter += 1

  try:
    if tcp.dport == 5060 and len(tcp.data) > 0:
      sourceIP = ip.src
      destinationIP = ip.dst
#      print(eth.data)
      print('Source: ' + str(tcp.sport) + ' Destination: ' + str(tcp.dport))
      print('Source IP: ',  sourceIP)
      print('Destination IP: ', destinationIP)
#      print('IP: %s -> %s (len=%d ttl=%d DF=%d MF=%d offset=%d)\n' % (inet_to_str(ip.src), inet_to_str(ip.dst), ip.len, ip.ttl, do_not_fragment, more_fragments, fragment_offset))
#      print(tcp.data)
  except:
    pass

#  ip = eth.data
#  ipcounter += 1
#
#  if ip.p == dpkt.ip.IP_PROTO_TCP: 
#    tcpcounter += 1
#
#  if ip.p == dpkt.ip.IP_PROTO_UDP:
#    udpcounter += 1

print("Total number of packets in the pcap file: ", counter)
print("Total number of ip packets: ", ipcounter)
print("Total number of tcp packets: ", tcpcounter)
print("Total number of udp packets: ", udpcounter)
