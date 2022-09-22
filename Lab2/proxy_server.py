#!/usr/bin/env python3
import socket
import time
import sys

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)

    except socket.gaierror:
        print("Failed to resolve hostname, exiting.")
        sys.exit()

    return remote_ip

def main():
    proxy_host = 'www.google.com'
    proxy_port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Initializing Proxy Server...")
    
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(1)
        
        #continuously listen for connections
        while True:
            conn, addr = proxy_start.accept()
            print("Connected by", addr)

            #connection now made, make new Socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_socket:
                print("Connecting to Google...")

                remote_ip = get_remote_ip(proxy_host)

                proxy_socket.connect((remote_ip, proxy_port))

                #receive data, then send it to the google server
                full_data = conn.recv(BUFFER_SIZE)
                proxy_socket.sendall(full_data)
                proxy_socket.shutdown(socket.SHUT_WR)

                data = proxy_socket.recv(BUFFER_SIZE)
                conn.send(data)

            conn.close()

if __name__ == "__main__":
    main()
