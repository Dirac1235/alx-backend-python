# Define the static routes
static_routes = {
    "0.0.0.0/0": "192.168.1.1",  # Default route
    "10.1.101.0/24": "192.168.2.2",
    "10.1.0.0/16": "192.168.3.3"
}

# Define the destination IP addresses
destination_ips = [
    "192.168.1.1",
    "192.168.2.2",
    "192.168.3.3",
    "10.1.1.10",
    "10.1.101.14",
    "10.1.101.33",
    "10.2.1.3",
    "10.1.4.6",
    "172.23.18.55",
    "10.5.8.4",
    "10.1.101.123"
]

# Function to determine the appropriate path
def get_path(ip):
  for network, next_hop in static_routes.items():
    if ip_in_network(ip, network):
      return next_hop
  return "Not routable (Unreachable)"  # No matching route found

# Function to check if an IP address belongs to a network
def ip_in_network(ip, network):
  ip_addr = int(ip.split('.')[0]) * 2**24 + int(ip.split('.')[1]) * 2**16 + int(ip.split('.')[2]) * 2**8 + int(ip.split('.')[3])
  network_addr, mask = network.split('/')
  network_addr = int(network_addr.split('.')[0]) * 2**24 + int(network_addr.split('.')[1]) * 2**16 + int(network_addr.split('.')[2]) * 2**8 + int(network_addr.split('.')[3])
  mask = int(mask)
  return (ip_addr & (2**32 - 1 << (32 - mask))) == network_addr

# Print the results
print("Destination ip addresses\t Appropriate path")
for ip in destination_ips:
  path = get_path(ip)
  print(f"{ip}\t\t {path}")
