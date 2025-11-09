class Device:
    def device_info(self):
        print("Device information")

class Smartphone(Device):
    def smartphone_info(self):
        print("Smartphone information")

class AndroidPhone(Smartphone):
    def android_info(self):
        print("Android phone information")

my_phone = AndroidPhone()
my_phone.device_info()
my_phone.smartphone_info()
my_phone.android_info()