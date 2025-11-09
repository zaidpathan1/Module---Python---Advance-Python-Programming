class Device:
    def device_info(self):
        print("Device class")

class Smartphone(Device):
    def smartphone_info(self):
        print("Smartphone class")

class Camera:
    def camera_info(self):
        print("Camera class")

class SmartCamera(Smartphone, Camera):
    def smartcamera_info(self):
        print("SmartCamera class")

obj = SmartCamera()
obj.device_info()
obj.smartphone_info()
obj.camera_info()
obj.smartcamera_info()