import socket
import logging
import threading
from datetime import datetime

# --- CONFIGURATION ---
# We use port 2222 to avoid conflict with real services.
# '0.0.0.0' means "listen to everyone on the network".
BIND_IP = '0.0.0.0'
BIND_PORT = 2222
LOG_FILE = 'honeypot_attacks.log'

# Setup Logging (Evidence Recorder)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def handle_client(client_socket, client_addr):
    print(f"[!] ALERT: Intrusion attempt from {client_addr[0]}")
    
    try:
        # 1. Send Fake Banner (Trick them into thinking it's an Ubuntu Server)
        client_socket.send(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5\r\n")
        
        # 2. Capture their input (The Username/Password attempt)
        # We give them 5 seconds to type something
        client_socket.settimeout(5)
        data = client_socket.recv(1024)
        
        # 3. Log the Attack
        if data:
            evidence = f"IP: {client_addr[0]} | Tried Payload: {data.strip()}"
            logging.info(evidence)
            print(f"    -> CAPTURED: {evidence}")
        
        # 4. Kick them out
        client_socket.close()
        
    except Exception as e:
        # If they connect but don't type anything, just close.
        client_socket.close()

def start_honeypot():
    # Create the trap (Socket)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((BIND_IP, BIND_PORT))
    server.listen(5)
    
    print("--------------------------------------------------")
    print(f"[*] HONEYPOT ACTIVE v1.0")
    print(f"[*] Trap is Set on Port: {BIND_PORT}")
    print(f"[*] Recording attacks to: {LOG_FILE}")
    print("--------------------------------------------------")

    while True:
        client, addr = server.accept()
        # Handle each hacker in a separate thread so the server doesn't freeze
        client_handler = threading.Thread(target=handle_client, args=(client, addr))
        client_handler.start()

if __name__ == "__main__":
    start_honeypot()