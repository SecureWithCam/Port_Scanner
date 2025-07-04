import socket  # This brings in Python's networking tools

# Step 1: Ask the user for the target (IP address or domain)
target = input("Enter the target (example: scanme.nmap.org): ")

# Step 2: Choose which ports to scan (these are common ports)
ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]

print(f"\nScanning {target}...\n")

# Step 3: Loop through each port and check if it's open
for port in ports:
    # Create a socket object (like opening a network door)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # Don't wait forever—1 second timeout

    # Try to connect to the target on this port
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    s.close()  # Close the connection

print("\nScan complete")
