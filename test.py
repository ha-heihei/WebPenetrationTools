import sys
from scapy.all import *
import time

from scapy.layers.inet import ICMP, IP, TCP
from scapy.layers.l2 import Ether

while (1) :
   packet= Ether(src=RandMAC(), dst=RandMAC())/IP(src=RandIP(), dst=RandIP())/ ICMP()
   time.sleep(0.5)
   sendp(packet)
   print(packet.summary())


# import sys, random
# while 1:
#      pdst="%i.%i.%i.%i" %(random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
#      psrc="1.1.1.1"
#      print(send(IP(src=psrc,dst=pdst)/ICMP ()))
#
# import sys, random
# while 1:
#  pdst="%i.%i.%i.%i" %(random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
#  psrc="1.1.1.1"
#  #send(IP(src=psrc,dst=pdst)/ICMP ())
#  print(send(IP(src=psrc, dst=pdst)/TCP(dport=80, flags="S")))