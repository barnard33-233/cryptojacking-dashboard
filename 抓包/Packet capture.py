from scapy.all import sniff, TCP, ARP, IP, Ether
import csv

packets = []

def packet_handler(packet):
    if packet.haslayer(ARP):
        # 处理 ARP 数据包
        arp_packet = packet.getlayer(ARP)
        timestamp = int(packet.time)
        source_ip = arp_packet.psrc
        destination_ip = arp_packet.pdst
        protocol = "ARP"
        length = len(packet)
        hw_src = arp_packet.hwsrc
        hw_dst = arp_packet.hwdst
    elif packet.haslayer(TCP):
        # 处理 TCP 数据包
        timestamp = int(packet.time)
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = "TCP"
        length = len(packet)
        hw_src = packet[Ether].src
        hw_dst = packet[Ether].dst
    else:
        # 其他类型的数据包
        return

    return timestamp, source_ip, destination_ip, protocol, length, hw_src, hw_dst


def print_packet(packet):
    result = packet_handler(packet)
    if result:
        packets.append(result)
        if len(packets) >= 10:
            save_packets_to_csv(packets)
            packets.clear()

def save_packets_to_csv(packets):
    with open("packets.csv", "w", newline="") as csvfile:
        #如果文件不存在将被创建。如果文件已存在，新的数据包将被追加到文件的末尾。如果想覆盖现有的文件，使用"w"模式替代"a"模式来打开文件。
        writer = csv.writer(csvfile)
        for packet in packets:
            packet_num = 0
            if csvfile.tell() == 0:  # 如果文件为空，则写入列名
                writer.writerow(["Time", "Source", "Destination", "Protocol", "Length", "Hw_src", "Hw_dst"])
            for packet in packets:
                writer.writerow(packet)
            for packet in packets[-10:]:
                packet_num = packet_num + 1
                print(packet_num, packet)
            print()

def main():
    global packets
    network_interface = "WLAN"
    filter_condition = "tcp or arp or port 80"
    print("正在抓包，结果已存入packets.csv中。。。")
    # 开始抓包并进行处理
    sniff(iface=network_interface, filter=filter_condition, prn=lambda packet: print_packet(packet))

if __name__ == "__main__":
    main()

