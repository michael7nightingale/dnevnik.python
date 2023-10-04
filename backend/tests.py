import ipaddress


ip = "192.168.32.96"
mask = "28"
q = 0
for ip_addr in ipaddress.ip_network(f"{ip}/{mask}"):
    ip_binary = bin(int(ip_addr))[2:]
    if ip_binary.count("1") % 2 == 1:
        q += 1

print(q)
