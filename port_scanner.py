import socket  # Import Python's built-in networking module

# Prompt the user to enter a target IP address or domain name
target = input("Enter the target (example: scanme.nmap.org): ")

# Define a list of common ports to scan
ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]

print(f"\nScanning {target}...\n")

# Loop through each port and attempt to connect
for port in ports:
    # Create a socket object for TCP connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)   # Set timeout to 1 second to avoid delays

    # Attempt to connect to the target on the current port
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    # Close the socket connection
    s.close()

print("\nScan complete")
