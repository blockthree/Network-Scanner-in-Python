import scapy.all as scapy


def scan(ip):
    arp_reqquest = scapy.ARP(pdst=ip)
    source_def = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
   # scapy.ls(scapy.Ether())
    #print(source_def.summary())
    final = source_def/arp_reqquest
    print(final.show())
    


scan("192.168.94.172")   