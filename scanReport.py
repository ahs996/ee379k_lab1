#!/usr/bin/env python3

def main():
    ipFile = open("listCIDR.txt", "r", newLine=None)
    data = []
    for line in ipFile:
        read_line = line.rsplit().split("CIDR:")
        data.append(read_line)
    print (data)