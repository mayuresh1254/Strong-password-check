import socket
import threading

# Function to scan a specific port
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    except socket.error:
        print(f"[-] Couldn't connect to server {ip}")
        return

# Function to start scan on a range of ports
def run_scanner(target_ip, port_range):
    print(f"[*] Starting scan on {target_ip}")
    for port in range(*port_range):
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        thread.start()

if __name__ == "__main__":
    target = input("Enter target IP address: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))
    
    run_scanner(target, (start_port, end_port + 1))
