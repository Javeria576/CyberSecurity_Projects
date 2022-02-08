import socket
from queue import Queue
import threading

queue = Queue()

open_ports = []

target = '192.168.1.1'

def portscan(port):

    try:
        scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scan.connect((target, port))
        return True
    except:
        return False

def fill_port(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is opened".format(port))
            open_ports.append(port)

port_list = range(1, 100)
fill_port(port_list)

threadList = []

for t in range(10):
    thread = threading.Thread(target = worker)
    threadList.append(thread)


for thread in threadList:
    thread.start()

for thread in threadList:
    thread.join()

print("Open ports are: {}".format(open_ports))

