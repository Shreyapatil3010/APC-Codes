
server_ip = ("192.168.1.1",)

allowed_ips = ["192.168.1.2", "192.168.1.3"]

def update_allowed_ips(ip):
    if ip not in allowed_ips:
        allowed_ips.append(ip)
        print("IP added successfully")
    else:
        print("IP already exists")

def display_config():
    print("Server IP:", server_ip[0])
    print("Allowed IPs:", allowed_ips)

update_allowed_ips("192.168.1.4")

print("\nUpdated Configuration:")
display_config()

print("\nServer IP cannot be changed because it is stored in a tuple.")
