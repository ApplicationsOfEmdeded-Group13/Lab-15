from machine import Pin
from machine import PWM

forward_pin = Pin(18, Pin.IN, Pin.PULL_UP)
right_pin = Pin(19, Pin.IN, Pin.PULL_UP)
left_pin = Pin(20, Pin.IN, Pin.PULL_UP)
back_pin = Pin(21, Pin.IN, Pin.PULL_UP)

pwm_rate = 10
direction = True
ain1_ph = Pin(12, Pin.OUT)
bin1_ph = Pin(10, Pin.OUT)

ain2_en = PWM(13, freq = pwm_rate, duty_u16 = 0)
bin2_en = PWM(11, freq = pwm_rate, duty_u16 = 0)

pwm = min(max(int(2**16 * abs(1)), 0), 65535)

ain2_en.duty_u16(0)
ain2_en.duty_u16(0)

def rfInterrupt(pin):
    if pin == forward_pin:
        ain1_ph.high()
        bin1_ph.low()
        ain2_en.duty_u16(pwm)
        bin2_en.duty_u16(pwm)
    if pin == right_pin:
        ain1_ph.low()
        bin1_ph.low()
        ain2_en.duty_u16(pwm)
        bin2_en.duty_u16(pwm)
    if pin == left_pin:
        ain1_ph.high()
        bin1_ph.high()
        ain2_en.duty_u16(pwm)
        bin2_en.duty_u16(pwm)
    if pin == back_pin:
        ain1_ph.low()
        bin1_ph.high()
        ain2_en.duty_u16(pwm)
        bin2_en.duty_u16(pwm)

forward_pin.irq(trigger=Pin.IRQ_FALLING, handler=rfInterrupt)
right_pin.irq(trigger=Pin.IRQ_FALLING, handler=rfInterrupt)
left_pin.irq(trigger=Pin.IRQ_FALLING, handler=rfInterrupt)
back_pin.irq(trigger=Pin.IRQ_FALLING, handler=rfInterrupt)

while True:
    pass
