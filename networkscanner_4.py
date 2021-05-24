import scapy.all as scapy


def scan(ip):
    arp_reqquest = scapy.ARP(pdst=ip)
    source_def = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
   # scapy.ls(scapy.Ether())
    #print(source_def.summary())
    final_requset = source_def/arp_reqquest
    (answered,unanswered)= scapy.srp(final_requset,timeout= 1)
    print(answered.summary())

scan("192.168.94.56/24")   