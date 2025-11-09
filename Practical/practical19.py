class Device:
    def __init__(self, name):
        self.name = name
        print(f"Device initialized: {self.name}")

class Smartphone(Device):
    def __init__(self, name, brand):
        super().__init__(name)  
        self.brand = brand
        print(f"Smartphone initialized: {self.brand}")

phone = Smartphone("iPhone 14", "Apple")