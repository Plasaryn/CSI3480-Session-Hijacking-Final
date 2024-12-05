from scapy.all import sniff, IP, TCP, Raw

def process_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP) and packet.haslayer(Raw):  # Check for IP, TCP, and Raw layers
        raw_data = packet[Raw].load.decode(errors="ignore")  # Decode the payload
        if "session_id" in raw_data: 
            source_ip = packet[IP].src
            dest_ip = packet[IP].dst
            source_port = packet[TCP].sport
            dest_port = packet[TCP].dport
            
            session_id = raw_data.split("session_id:")[1].split()[0] if "session_id:" in raw_data else "Unknown"
            
            print("\n=== Packet with session_id Found ===")
            print(f"Source IP: {source_ip}")
            print(f"Destination IP: {dest_ip}")
            print(f"Source Port: {source_port}")
            print(f"Destination Port: {dest_port}")
            # print(f"Session ID: {session_id}")
            print(f"Payload:\n{raw_data}")
            print("====================================\n")

# Start sniffing packets
sniff(filter="tcp", prn=process_packet, store=False)
