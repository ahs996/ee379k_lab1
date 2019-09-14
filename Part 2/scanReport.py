#! usr/bin/env python
import socket
import struct
import sys
import ipaddress


class CIDR():
    def __init__(self, ip_dot):
        self.ip_dot = ip_dot
        self.net_prefix = 32
        self.min_ip = 2 ** 32
        self.max_ip = int()
        self.subnets = list()
        self.ips_within = list()
        self.counter = 0
        for ip in ip_dot:
            range_of_ips = ipaddress.IPv4Network(ip)
            self.min_ip = min(self.min_ip, ip2long(str(range_of_ips[0])))
            self.max_ip = max(self.max_ip, ip2long(str(range_of_ips[-1])))
    def check_subnet(self, network):
        if self.min_ip <= network.min_ip and self.max_ip >= network.max_ip:
            self.subnets.append(network)        # network is a subnet of self
            self.counter += 1
    def check_ip_in_range(self, ip):
        longform = ip2long(ip)
        if longform in range(self.min_ip, self.max_ip):
            self.ips_within.append(ip)
    def __str__(self):
        s = "CIDR: " + str(self.ip_dot) + '\n'
        ip_range = [socket.inet_ntoa(struct.pack('!L', self.min_ip)), socket.inet_ntoa(struct.pack('!L', self.max_ip))]
        s += "IPv4 Range: " + str(ip_range) + '\n'
        nets = [str(self.ip_dot) for subnet in self.subnets]
        s += "Subnets: " + str(nets) + '\n'
        s += "IPs in network: " + str(self.ips_within) + ": " + str(self.counter) + '\n'
        return s
def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("ERROR: a filepath was not entered")
    script_name = sys.argv[0]
    cidr_name = sys.argv[1]
    ipv4_name = sys.argv[2]

    with open(cidr_name) as f: 
        lines = [line.rstrip('\n').replace(",", "").split() for line in f]
    
    # print(CIDR(lines[0][1:len(lines[0])]).ip_dot)
    cidr_list = list()
    for line in lines:
        if line[0] == 'CIDR:':
            cidr_list.append(CIDR(line[1:len(line)]))
    print("cidrs found:", len(cidr_list))
    # print(cidr_list[0])
    print(cidr_list[0].min_ip- cidr_list[0].max_ip, cidr_list[0].net_prefix)
    print(cidr_list[5].min_ip, cidr_list[5].max_ip, cidr_list[0].net_prefix)

    for i in range(0, len(cidr_list)):
        for j in range(0, len(cidr_list)):
            if i != j:
                cidr_list[i].check_subnet(cidr_list[j])
    # print(len(cidr_list[0].subnets))
    # for i in range(0, len(cidr_list)):
    #     print(len(cidr_list[0].subnets))
    
    with open(ipv4_name) as f:
        lines = [line.rstrip('\n') for line in f]
    # print(lines)
    for i in range(0, len(cidr_list)):
        for j in range(0, len(lines)):
            cidr_list[i].check_ip_in_range(lines[j])
    curMaxSub = 0
    curMaxSubI = 0
    curMaxIP = 0
    curMaxIPI = 0
    for i in range(0, len(cidr_list)):
        if len(cidr_list[i].ips_within) > curMaxIP:
            curMaxIP = len(cidr_list[i].ips_within)
            curMaxIPI = i
        if len(cidr_list[i].subnets) > curMaxSub:
            curMaxSub = len(cidr_list[i].subnets)
            curMaxSubI = i
    print(curMaxSub, curMaxSubI, curMaxIP, curMaxIPI)    
    print(cidr_list[0])
    
    with open("net_group.txt", 'w+') as f1:
        for c in cidr_list:
            print(c, file=f1)
