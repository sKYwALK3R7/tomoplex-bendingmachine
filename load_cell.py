import time
import sys
from  hx711 import HX711

class LoadCell():
    def __init__(self):
        print("Hello")
        self.hx = HX711(5, 6)
        print("Hello2")
        self.hx.set_reading_format("MSB", "MSB")
        print("Hello3")
        self.hx.set_reference_unit(1)
        print("Hello4")
        self.hx.reset()
        print("Hello5")
        self.denominator = -4502.847332
        self.forceMax = 0
        self.offset = -99999999

    def calibrate(self):
        print("Beginning")
        self.hx.reset()
        self.hx.reset()
        sum = 0
        for _ in range (50):
            print(_)
            sum += self.hx.read_long()
            self.hx.power_down()
            self.hx.power_up()
            time.sleep(0.1)
        self.offset = sum/50
        # time.sleep(2)

    def getForce(self):
        force = (self.hx.read_long() - self.offset)/ self.denominator
        self.hx.power_down()
        self.hx.power_up()
        time.sleep(0.1)
        if force > self.forceMax: self.forceMax = force
        return force
    
    def getMaxForce(self):
        return self.forceMax
    
    def cleanAndExit():
        sys.exit()
