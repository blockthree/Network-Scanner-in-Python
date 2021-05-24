from typing import final
import scapy.all as scapy

def scan(ip):
    arp_re = scapy.ARP(pdst=ip)
    source_def= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    final = source_def/arp_re
    (ans,unans) = scapy.srp(final,timeout=1,verbose=False)
    
    reult= []
    for de in ans:
        result_dic = {"ip":de[1].psrc,"mac":de[1].hwsrc}
        reult.append(result_dic)
       # print(de[1].psrc+"\t\t\\t"+de[1].hwsrc)
       #scapy.ls(scapy.Ether())
        print("______________________________________________________")
    return reult

def printdic(reult):
    print("ip\t\t\t\t\tmac address")
    for fa in reult:
        print(fa["ip"]+"\t\t\t\t"+fa["mac"])
 
reult = scan("192.168.94.56/24")  
printdic(reult) 