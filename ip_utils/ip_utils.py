import ipaddress

def return_ip_address(address):
    return ipaddress.ip_address(address)

ip = return_ip_address("192.168.0.1")
print("ip of 192.168.0.1",ip,type(ip))
print("ip of 192.168.0.1",ip.__repr__)
ip = return_ip_address(1)
print("ip of integer 1",ip,type(ip))
ip_int = int(return_ip_address("192.168.0.1"))
print("integer of ip of 192.168.0.1",ip_int,type(ip_int))
b_int = bin(ip_int)
print("binary of ip of 192.168.0.1",b_int,type(b_int))
ip = return_ip_address(0b11000000101010000000000000000001)
print("ip of binary number 0b11000000101010000000000000000001",ip,type(ip))
ip_str = str(return_ip_address("192.168.0.1"))
print("string of ip of 192.168.0.1",ip_str,type(ip_str))

print("########################################################################################################################")
network = ipaddress.ip_network('192.168.0.0/24')
print("network ={} and address={} netmask={} prefixlen={}".format(network, network.network_address, network.netmask, network._prefixlen))

try:
    network = ipaddress.ip_network('192.168.0.1/24')
    print("network ={} and address={} netmask={} prefixlen={}".format(network, network.network_address, network.netmask, network._prefixlen))
except Exception as e:
    print("Exception with host bits set={}. This can be avoided by setting strict=False".format(e))
    network = ipaddress.ip_network('192.168.0.1/23', strict=False)
    print("With host bits set: network ={} and address={} netmask={} prefixlen={}".format(network, network.network_address, network.netmask, network._prefixlen))

