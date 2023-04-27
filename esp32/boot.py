# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from machine import Pin
import _thread
from time import sleep
from json import dumps

import sys

btn = Pin(14, Pin.IN)
led = Pin(13, Pin.OUT)

############## get boot permissions ##############
print("permissions to boot... ", end = "")
if not btn.value():
    print("[x]")
    
    # signal it is going to shut down
    for _ in range(6):
        led.value(not led.value())
        sleep(0.1)
    
    print("cancelling boot...")
    sys.exit()
    
print("[V]")

def blink_led():
    while True:
        led.value(not led.value())
        sleep(0.5)

_thread.start_new_thread(blink_led, ())

############## start ##############
from mpu import MPU9250

mpu = MPU9250(Pin(22), Pin(21))

print("all set up, starting to send data...")

while True:
    print(dumps({"accel": mpu.accel}))
    sleep(0.1)
