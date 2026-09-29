import time
import sys
import random
from scapy.all import IP, TCP, UDP, send

# ==============================================================================
# TRAFFIC GENERATOR FOR IDS TESTING
# ==============================================================================

def print_header():
    print("\n" + "="*50)
    print("   NETWORK TRAFFIC GENERATOR (IDS TESTER)")
    print("="*50)

def get_target_ip():
    target = input("\n[?] Enter Victim IP Address: ")
    return target

def trigger_high_traffic(target_ip):
    # Threshold is > 200. We send 250 to be safe.
    print(f"\n[+] Generating HIGH TRAFFIC (Warning Tier)...")
    print(f"    -> Target: {target_ip}")
    print(f"    -> Sending 250 Packets to Port 80...")
    
    # Craft a simple HTTP-like packet
    pkt = IP(dst=target_ip)/TCP(dport=80, flags="S")
    
    # Send loop
    count = 0
    for i in range(250):
        send(pkt, verbose=0)
        count += 1
        if count % 50 == 0:
            print(f"    Sent {count} packets...")
            
    print(f"\n[SUCCESS] Sent 250 packets. This should trigger 'HIGH TRAFFIC' (Yellow).")

def trigger_dos_attack(target_ip):
    # Threshold is > 500. We send 600.
    print(f"\n[+] Generating DoS ATTACK (Critical Tier)...")
    print(f"    -> Target: {target_ip}")
    print(f"    -> Sending 600 Packets to Port 80...")
    
    pkt = IP(dst=target_ip)/TCP(dport=80, flags="S")
    
    count = 0
    # Faster sending for DoS simulation
    for i in range(600):
        send(pkt, verbose=0)
        count += 1
        if count % 100 == 0:
            print(f"    Sent {count} packets...")
            
    print(f"\n[SUCCESS] Sent 600 packets. This should trigger 'DoS ATTACK' (Red).")

def trigger_port_scan(target_ip):
    # Threshold is > 15 unique ports. We scan 25.
    print(f"\n[+] Generating PORT SCAN...")
    print(f"    -> Target: {target_ip}")
    print(f"    -> Scanning 25 random ports (range 2000-2025)...")
    
    count = 0
    for port in range(2000, 2026):
        pkt = IP(dst=target_ip)/TCP(dport=port, flags="S")
        send(pkt, verbose=0)
        print(f"    -> Probe sent to port {port}")
        time.sleep(0.05) # Small delay to ensure they arrive in order
        
    print(f"\n[SUCCESS] Scanned 26 unique ports. This should trigger 'PORT SCAN' (Magenta).")

def trigger_restricted_ports(target_ip):
    print(f"\n[+] Accessing RESTRICTED PORTS...")
    print(f"    -> Target: {target_ip}")
    
    ports = [21, 23, 445, 3389]
    
    for port in ports:
        print(f"    -> Connecting to Restricted Port: {port}")
        pkt = IP(dst=target_ip)/TCP(dport=port, flags="S")
        send(pkt, verbose=0)
        time.sleep(0.1)
        
    print(f"\n[SUCCESS] Accessed restricted ports. This should trigger 'RESTRICTED PORT' (Red).")

def trigger_ml_anomaly(target_ip):
    print(f"\n[+] Generating BEHAVIORAL ANOMALY...")
    print(f"    -> Target: {target_ip}")
    print(f"    -> Sending packet with unusual Size and Port...")
    
    # Rare port + Large payload usually triggers Isolation Forest
    # 4444 is often used by Metasploit, usually flagged
    # Payload is random junk data to increase size
    payload = "X" * 1200 
    pkt = IP(dst=target_ip)/UDP(dport=6666)/payload
    
    for i in range(5):
        send(pkt, verbose=0)
        print(f"    -> Sent anomalous packet {i+1}")
    
    print(f"\n[SUCCESS] Sent unusual packets. This usually triggers 'TRAFFIC ANOMALY'.")

# ==============================================================================
# MAIN MENU
# ==============================================================================

if __name__ == "__main__":
    print_header()
    target = get_target_ip()
    
    while True:
        print("\n" + "-"*30)
        print("SELECT ATTACK SCENARIO")
        print("-" * 30)
        print("1. Test 'HIGH TRAFFIC' (Warning > 200 pkts)")
        print("2. Test 'DoS ATTACK'   (Critical > 500 pkts)")
        print("3. Test 'PORT SCAN'    (> 15 unique ports)")
        print("4. Test 'RESTRICTED PORTS' (21, 23, 445)")
        print("5. Test 'ML ANOMALY'   (Weird packet size)")
        print("6. Exit")
        
        choice = input("\nEnter Choice (1-6): ")
        
        if choice == '1':
            trigger_high_traffic(target)
        elif choice == '2':
            trigger_dos_attack(target)
        elif choice == '3':
            trigger_port_scan(target)
        elif choice == '4':
            trigger_restricted_ports(target)
        elif choice == '5':
            trigger_ml_anomaly(target)
        elif choice == '6':
            print("\n[Exiting] Stay safe!")
            sys.exit()
        else:
            print("[!] Invalid choice")
