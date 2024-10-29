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

# Toggles all 3 LEDs
def toggleLEDs():
    led1.toggle()
    led2.toggle()
    led3.toggle()

#Function called whenever interrupt signla is received, so LEDs
#toggle with every transmission

# Callback function to execute when an IR code is received
# Changes motor direction every time the receiver gets a signal
def ir_callback(data, addr, _):
    toggleLEDs()
    print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")

# Setup the IR receiver
ir_pin = Pin(17, Pin.IN, Pin.PULL_UP) # Adjust the pin number based on your wiring

ir_receiver = NEC_8(ir_pin, callback=ir_callback)

# Optional: Use the print_error function for debugging
ir_receiver.error_function(print_error)

# Main loop to keep the script running
while True:
    pass # Execution is interrupt-driven, so just keep the script alive
