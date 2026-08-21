import re

def check_ip(ip):
    ipv4 = r'^(\d{1,3}\.){3}\d{1,3}$'
    ipv6 = r'^([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}$'

    if re.match(ipv4, ip):
        return True
    elif re.match(ipv6, ip):
        return True
    else:
        return False

ip = input("Enter IP address: ")

if check_ip(ip):
    print("Valid IP Address")
else:
    print("Invalid IP Address")