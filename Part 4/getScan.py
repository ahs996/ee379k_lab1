#!usr/bin/env_python3
from socket import *

def main():
    client = socket(AF_INET, SOCK_STREAM)

    host = "www.baiwanzhan.com"
    tPort = 80 
    # target port
    client.connect((host, tPort))
    
    pkt1 = "GET /service/site/search.aspx?query=%E6%B3%95"
    pkt2 = "%E8%BD%AE HTTP/1.1\r\nHost:{}\r\n\r\n".format(host)
    client.send(pkt1.encode())
    client.send(pkt2.encode())

    result = client.recv(4096)
    http_resp = repr(result)
    resp_len = len(http_resp)

    print("response:" + http_resp)

if __name__ == "__main__":
    main()