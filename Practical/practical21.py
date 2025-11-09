class Device:
    def info(self):
        print("This is a general device.")

class Smartphone(Device):
    def info(self):  
        print("This is a smartphone device.")

# Creating objects
device = Device()
phone = Smartphone()

device.info()  
phone.info()