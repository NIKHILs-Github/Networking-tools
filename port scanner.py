import socket

# Function to scan a specific port
def scan_port(target, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout of 1 second
        
        # Try to connect to the target IP address and port
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")
        
        sock.close()  # Close the socket
    except socket.error as err:
        print(f"Error scanning port {port}: {err}")

# Function to scan a range of ports
def scan_ports(target, start_port, end_port):
    print(f"Scanning ports on {target} from {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        scan_port(target, port)

# Example usage
target_ip = input("Enter the target IP address: ")
start_port = int(input("Enter the start port number: "))
end_port = int(input("Enter the end port number: "))

scan_ports(target_ip, start_port, end_port)
