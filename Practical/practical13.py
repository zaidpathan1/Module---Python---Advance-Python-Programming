class Device:
    def __init__(self, name, device_type, price):
        self.name = name          
        self.device_type = device_type
        self.price = price

device1 = Device("iPhone 14", "Smartphone", 1200)

print("Device Details:")
print(f"Name       : {device1.name}")
print(f"Type       : {device1.device_type}")
print(f"Price      : ${device1.price}")