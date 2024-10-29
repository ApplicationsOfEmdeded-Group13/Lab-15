#Program keeps motors running while changing their direction every half second

import machine, time
from machine import Pin
from machine import PWM

pwm_rate = 10
direction = True
ain1_ph = Pin(12, Pin.OUT) # Initialize GP14 as an OUTPUT
bin1_ph = Pin(10, Pin.OUT)

ain2_en = PWM("GP13", freq = pwm_rate, duty_u16 = 0)
bin2_en = PWM("GP11", freq = pwm_rate, duty_u16 = 0)

pwm = min(max(int(2**16 * abs(1)), 0), 65535)


while True:
    ain1_ph.low()
    bin1_ph.low()
    ain2_en.duty_u16(pwm)
    bin2_en.duty_u16(pwm)
    time.sleep(.5)
    ain1_ph.high()
    bin1_ph.high()
    ain2_en.duty_u16(pwm)
    bin2_en.duty_u16(pwm)
    time.sleep
