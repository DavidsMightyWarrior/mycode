#!/usr/bin/env python3

from scapy.all import *
#from btbb import *
packets = rdpcap('temp.pcap')


#packets.summary()
#packets.show()

#for packet in packets:
#  if packet.haslayer(UDP):
#    if isinstance(packet.an, UDP):
#      print(packet.an.rrname)

#for i in range(len(packets)):
#  t = packets[i].fields['subtype']
#  print(t)

#srcIP=[]
#for pkt in packets:
#  if IP in pkt:
#    try:
#      srcIP.append(pkt[IP].src)
#    except:
#      pass
