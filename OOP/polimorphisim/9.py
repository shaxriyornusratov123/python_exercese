class Wifi:
    def connect(self):
        print("connecting on wifi")

class Ethernet:
    def connect(self):
        print("connecting on the ethernet")

def start_connection(device):
    device.connect()

w1=Wifi()
e=Ethernet()

start_connection(w1)
start_connection(e)