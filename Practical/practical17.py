class Device:
    def device_info(self):
        print("This is a device")

class Smartphone(Device):
    def smartphone_info(self):
        print("This is a smartphone")

class Laptop(Device):
    def laptop_info(self):
        print("This is a laptop")

phone = Smartphone()
laptop = Laptop()

phone.device_info()
phone.smartphone_info()

laptop.device_info()
laptop.laptop_info()