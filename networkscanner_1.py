import scapy.all as scapy

def win(ip):
    scapy.arping(ip)

win("192.168.1.1/24")   #group 
win("192.168.1.1")  #single scan 