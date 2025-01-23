from scapy.all import sniff


# smaple code you can impove on it 
def packet_callback(packet):
    print(packet.summary())

sniff(prn=packet_callback, count=10)
