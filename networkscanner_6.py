from typing import final
import scapy.all as scapy

def scan(ip):
    arp_re = scapy.ARP(pdst=ip)
    source_def= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    final = source_def/arp_re
    (ans,unans) = scapy.srp(final,timeout=1,verbose=False)
    print("ip\t\t\t\t\tmac address")
    reult= []
    for de in ans:
        result_dic = {"ip":de[1].psrc,"mac":de[1].hwsrc}
        reult.append(result_dic)
        print(de[1].psrc+"\t\t\\t"+de[1].hwsrc)

        print("______________________________________________________")


    #scapy.ls(scapy.Ether())
    print(reult)

scan("192.168.94.56/24")    