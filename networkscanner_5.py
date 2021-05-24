from re import VERBOSE
import scapy.all as scapy
from scapy.data import PPI_TYPES


def scan(ip):
    arp_reqquest = scapy.ARP(pdst=ip)
    source_def = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
   # scapy.ls(scapy.Ether())
    #print(source_def.summary())
    final_requset = source_def/arp_reqquest
    (answered,unanswered)= scapy.srp(final_requset,timeout= 1,verbose=False)
    print("ip \t\t\t\t\t macaddress")
    for h in answered:
        print(h[1].psrc+"\t\t\t\t"+h[1].hwsrc)
       
        print("______________________________________________")

scan("192.168.94.56/24")  