import scapy.all as scapy

def scan(ip):
    f = scapy.ARP(pdst=ip)
    print(f.summary())
    #scapy.ls(scapy.ARP())

scan("192.168.94.172")    
