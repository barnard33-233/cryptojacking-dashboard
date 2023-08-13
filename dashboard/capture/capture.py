from scapy.all import sniff
from scapy.layers.l2 import Ether, ARP
from scapy.layers.inet import IP
import pandas as pd


class Capture:
    def __init__(self, iface, local_mac, capture_duration) -> None:
        self.records = {}
        self.iface = iface
        self.local_mac = local_mac
        self.capture_duration = capture_duration
        self.start_timestamp = -1
    
    def stop_filter(self, packet) -> bool:
        return packet.time - self.start_timestamp > self.capture_duration 

    def proto_analyze(self, packet) -> str:
        # this field is not used currently.
        return 'UNKNOWN'

    def packet_hander(self, packet):
        '''
        create a record from a packet
        fields:
            Time
            Source(source ip)
            Destination dest ip
            Protocol
            Length
            Hw_src(src mac)
            Hw_dst(dst mac)
        '''
        # generic
        timestamp = int(packet.time)
        length = len(packet)
        try:
            hw_src = packet[Ether].src
            hw_dst = packet[Ether].dst
        except:
            # not a ethernet packet
            # print("no [Ether] layer") # DEBUG
            return

        # unique
        if packet.haslayer(IP):
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            protocol = self.proto_analyze(packet)
        elif packet.haslayer(ARP):
            arp_layer = packet.getlayer(ARP)
            src_ip = arp_layer.psrc
            dst_ip = arp_layer.pdst
            protocol = 'UNKNOWN'
            pass
        else:
            # print('[?] Invalid format') # DEBUG
            return
        
        # find out which is the remote mac
        if hw_dst == self.local_mac:
            remote_mac = hw_src
        elif hw_src == self.local_mac:
            remote_mac = hw_dst
        else:
            # should not reach here
            return
        
        record = [timestamp, src_ip, dst_ip, protocol, length, hw_src, hw_dst]
        # print(f"{remote_mac}:{record}") # DEBUG

        # update start_timestamp
        if self.start_timestamp == -1:
            self.start_timestamp = timestamp

        if remote_mac in self.records:
            self.records[remote_mac].append(record)
        else:
            self.records[remote_mac] = [record]
        # TODO: broadcast?

    def capture(self):
        # capture packets
        sniff(
            iface=self.iface,
            prn=lambda packet: self.packet_hander(packet),
            stop_filter=lambda packet: self.stop_filter(packet)
        )

        # convert list[list] to dataframe

        dataframes = {}
        for mac in self.records:
            data = pd.DataFrame(self.records[mac])
            data.columns = ['Time', 'Source', 'Destination', 'Protocol', 'Length', 'Hw_src', 'Hw_dst']
            dataframes[mac] = data

        return dataframes

if __name__ == '__main__':
    # test:
    iface = "wlp4s0" 
    capture_duration = 2 #s

    try:
        local_mac = open(f'/sys/class/net/{iface}/address').read().strip('\n')
    except:
        local_mac = '00:00:00:00'
    capturer = Capture(iface, local_mac, capture_duration)
    dfs = capturer.capture()
    print(dfs)
    # for mac in dfs:
    #     print(mac, dfs[mac][1][0])
