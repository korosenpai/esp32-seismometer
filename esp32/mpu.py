# wrapper class of folder mpu9250 and simple.py inside it


from machine import SoftI2C, Pin
from math import sqrt, atan2, pi, sin, cos, asin, radians
from time import sleep
from json import dumps

from mpu9250.mpu9250 import MPU9250 as MPU9250DRIVERS


class MPU9250:
    def __init__(self, sda_pin, scl_pin) -> None:
        self.i2c = SoftI2C(scl = scl_pin, sda = sda_pin)

        print("scan: ", self.i2c.scan())
        self.mpu9250 = MPU9250DRIVERS(self.i2c)

        # calibration for gyro
        print("calibrating mpu6500...")
        # print_notification("offset: " + repr(self.mpu9250.mpu6500.calibrate(count = 100, delay = 50)))

        # Calibration and bias offset for magnetometer
        print("calibrating ak8963...")
        # print("offset: " + repr(self.mpu9250.ak8963.calibrate(count = 100, delay = 100)))

        
    
        # For low pass filtering
        self.magn_f_x = 0.0  # magnetometer filtered x value
        self.magn_f_y = 0.0
        self.magn_f_z = 0.0


    
    @property
    def accel(self):
        return self.mpu9250.acceleration
    
    def print_accel(self):
        x, y, z = self.accel
        print("x:", x, "y:", y, "z:", z)


    def getmagxyz(self):
        return self.mpu9250.magnetic

    
    @property
    def magn_heading(self):

        # Get soft_iron adjusted values from the magnetometer -> get less noise
        mag_x, mag_y, mag_z = self.mpu9250.magnetic
        # gyr = [ round(x * pi / 180, 2) for x in self.gyro]
        gyrRad = [ round(radians(x), 2) for x in self.mpu9250.gyro]

        self.magn_f_x = self.low_pass_filter(mag_x, self.magn_f_x)
        self.magn_f_y = self.low_pass_filter(mag_y, self.magn_f_y)
        self.magn_f_z = self.low_pass_filter(mag_z, self.magn_f_z)

        # works only on the plane
        # az =  90 - atan2(self.magn_f_y, self.magn_f_x) * 180 / pi

        # TODO tilt compensated compass
        # https://www.instructables.com/Tilt-Compensated-Compass/
        # https://www.best-microcontroller-projects.com/magnetometer-tilt-compensation.html
        
        # az = 180 * atan2(
        #     self.magn_f_x * sin(gyrRad[1]) * sin(gyrRad[0]) + self.magn_f_y * cos(gyrRad[1]) - self.magn_f_z * sin(gyrRad[1]) * cos(gyrRad[0]),
        #     self.magn_f_x * cos(gyrRad[0]) + self.magn_f_z * sin(gyrRad[0])
        # ) / pi

        Ym = self.magn_f_y * cos(gyrRad[1]) + self.magn_f_z * sin(gyrRad[1])
        Xm = self.magn_f_x * cos(gyrRad[0]) - self.magn_f_y * sin(gyrRad[1]) * sin(gyrRad[0]) + self.magn_f_z * cos(gyrRad[1]) * sin(gyrRad[0])

        az = 90 - atan2( Ym, Xm ) * 180 / pi


        # make sure the angle is always positive, and between 0 and 360 degrees
        if az < 0:
            az += 360


        # heading = self.degrees_to_heading(az)

        return az

    def low_pass_filter(self, raw_value:float, remembered_value):
        ''' Only applied 20% of the raw value to the filtered value '''
        
        # global filtered_value
        alpha = 0.8
        filtered = 0
        filtered = (alpha * remembered_value) + (1.0 - alpha) * raw_value
        return filtered
    
    def degrees_to_heading(self):
        degrees = self.magn_heading
        heading = ""
        if (degrees > 337) or (degrees >= 0 and degrees <= 22):
                heading = 'N'
        if degrees >22 and degrees <= 67:
            heading = "NE"
        if degrees >67 and degrees <= 112:
            heading = "E"
        if degrees >112 and degrees <= 157:
            heading = "SE"
        if degrees > 157 and degrees <= 202:
            heading = "S"
        if degrees > 202 and degrees <= 247:
            heading = "SW"
        if degrees > 247 and degrees <= 292:
            heading = "W"
        if degrees > 292 and degrees <= 337:
            heading = "NW"
        return heading

if __name__ == "__main__":

    mpu = MPU9250(Pin(22), Pin(21))
    
    while True:
        # mpu.print_accel()

        print(dumps({"accel": mpu.accel}))



        sleep(0.1)
