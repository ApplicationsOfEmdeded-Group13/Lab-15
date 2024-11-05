#   Pico pin GP13   -> AIN2
#   Pico pin GP12   -> AIN1
#   any Pico GND    -> GND
import ir_rx
import math, time
import machine

from machine import Pin
from ir_rx.nec import NEC_8 # Use the NEC 8-bit class
from ir_rx.print_error import print_error # for debugging

# load the MicroPython pulse-width-modulation module for driving hardware
from machine import PWM

time.sleep(1) # Wait for USB to become ready

led1 = Pin(2, Pin.OUT)
led2 = Pin(3, Pin.OUT)
led3 = Pin(4, Pin.OUT)

pwm_rate = 10
direction = True
ain1_ph = Pin(12, Pin.OUT)
bin1_ph = Pin(10, Pin.OUT)

ain2_en = PWM(13, freq = pwm_rate, duty_u16 = 0)
bin2_en = PWM(11, freq = pwm_rate, duty_u16 = 0)

pwm = min(max(int(2**16 * abs(1)), 0), 65535)

ain2_en.duty_u16(0)
ain2_en.duty_u16(0)

def toggleLEDs():
    led1.toggle()
    led2.toggle()
    led3.toggle()

def controlDirection(data):
    if data == 1:
        ain1_ph.low()
        bin1_ph.low()
        ain2_en.duty_u16(pwm)
        bin2_en.duty_u16(pwm)
    elif data == 0x02:
        ain1_ph.high()
        bin1_ph.high()
        ain2_en.duty_u16(pwm)
        bin2_en.duty_u16(pwm)
    elif data == 0x03:
        ain1_ph.low()
        bin1_ph.high()
        ain2_en.duty_u16(pwm)
        bin2_en.duty_u16(pwm)
    elif data == 0x04:
        ain1_ph.high()
        bin1_ph.low()
        ain2_en.duty_u16(pwm)
        bin2_en.duty_u16(pwm)
    elif data == 5:
        ain1_ph.low()
        bin1_ph.low()
        ain2_en.duty_u16(pwm)
        bin2_en.duty_u16(pwm)
        time.sleep(.5)
        ain2_en.duty_u16(0)
        bin2_en.duty_u16(0)



# Callback function to execute when an IR code is received
# Changes motor direction every time the receiver gets a signal
def ir_callback(data, addr, _):
    toggleLEDs()
    #print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")
    print(f"Received NEC command! Data: {data}, Addr: {addr}")
    controlDirection(data)

# Setup the IR receiver
ir_pin = Pin(17, Pin.IN, Pin.PULL_UP) # Adjust the pin number based on your wiring

ir_receiver = NEC_8(ir_pin, callback=ir_callback)

# Optional: Use the print_error function for debugging
ir_receiver.error_function(print_error)

# Main loop to keep the script running
while True:
    pass
