class Device:
    def device_info(self):
        print("This is a device.")

class Smartphone(Device):  
    def smartphone_info(self):
        print("This is a smartphone.")


phone = Smartphone()
phone.device_info()     
phone.smartphone_info()  