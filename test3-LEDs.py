from machine import Pin
import time

time.sleep(1)

led1 = Pin(2, Pin.OUT)
led2 = Pin(3, Pin.OUT)
led3 = Pin(4, Pin.OUT)

while True:
    led1.high()
    led2.high()
    led3.high()
    time.sleep(.5)
    led1.low()
    led2.low()
    led3.low()
    time.sleep(.5)
