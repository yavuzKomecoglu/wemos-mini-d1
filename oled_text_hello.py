import ssd1306
from machine import I2C, Pin

i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(64, 48, i2c)

display.fill(0)
display.text('Merhaba',5,5)
display.text('Yavuz',5,15)
display.show()

#display.invert(True)
