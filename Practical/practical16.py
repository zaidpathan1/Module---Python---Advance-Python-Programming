class Camera:
    def camera_info(self):
        print("This is a camera feature")

class GPS:
    def gps_info(self):
        print("This is a GPS feature")

class Smartphone(Camera, GPS):
    def phone_info(self):
        print("This is a smartphone")

my_phone = Smartphone()
my_phone.camera_info()
my_phone.gps_info()
my_phone.phone_info()