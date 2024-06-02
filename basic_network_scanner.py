import socket
import ipaddress
import threading
import keyboard

# Flag to control the scanning process
stop_scanning = False

def scan_port(ip, port):
    global stop_scanning
    if stop_scanning:
        return
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Lower timeout for faster scans
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open on {ip}")
        sock.close()
    except socket.error as e:
        print(f"Could not connect to {ip}:{port} due to {e}")

def scan_ip(ip, ports):
    for port in ports:
        scan_port(ip, port)
        if stop_scanning:
            break

def scan_network(network, ports):
    global stop_scanning
    threads = []
    try:
        for ip in ipaddress.IPv4Network(network):
            if stop_scanning:
                break
            thread = threading.Thread(target=scan_ip, args=(str(ip), ports))
            thread.daemon = True  # Set as daemon thread
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    except Exception as e:
        print(f"An error occurred: {e}")

def stop_scan_on_key_press():
    global stop_scanning
    print("Press 'x' to stop the scan.")
    keyboard.wait('x')
    stop_scanning = True
    print("Scan will stop after the current task completes.")

if __name__ == "__main__":
    network = input("Enter the network to scan (e.g., 192.168.1.0/24): ")
    ports = list(range(1, 1025))  # Modify port range as needed

    # Start a thread to monitor key press
    key_press_thread = threading.Thread(target=stop_scan_on_key_press)
    key_press_thread.daemon = True
    key_press_thread.start()

    scan_network(network, ports)
    print("Scan completed or stopped.")
