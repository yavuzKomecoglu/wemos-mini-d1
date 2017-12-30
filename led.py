from machine import Pin
import time

led = Pin(2, Pin.OUT)

for i in range(10):
    led(0)
    time.sleep(0.5)
    led(1)
    time.sleep(0.5)
