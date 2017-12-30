import network
import utime
from ntptime import settime
import json
import urequests
from machine import I2C, Pin
import ssd1306

def get_weather():
    r = urequests.get("http://api.openweathermap.org/data/2.5/weather?q=Istanbul&appid=3cf2dc844aebdb560fe02b5d12716a41&lang=tr&units=metric").json()
    temp = str(int(float(r['main']['temp'])))
    return temp

def connect_wifi(): 
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('SSID NAME', 'SSID PASSWORD')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())





days= {0:"Pzt", 1:"Sal", 2:"Çar", 3:"Per", 4:"Cum", 5:"Cmt", 6:"Paz"}
months = {1:"Oca", 2:"Şub", 3:"Mar", 4:"Nis", 5:"May", 6:"Haz", 7:"Tem", 8:"Ağu", 9:"Eyl", 10:"Eki", 11:"Kas", 12:"Ara"}

settime()

#oled display init
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(64, 48, i2c)


#wifi
connect_wifi()

#
i = 0
while True:
    i+=1
    temp = ""
    if(temp!=""):
        if(i%(30*60)==0):
            temp = get_weather()
    else:
        temp = get_weather()
        
    
    (year, month, mday, hour, minute, second, weekday, yearday) = utime.localtime()        

    display.fill(0)

    #display.text("Hava",5,5)
    display.text("{} C".format(temp),20,0)

    #display.text("{} {} {}".format(mday, months[month],days[weekday]),0,10)

    display.text("{} {}".format(mday, months[month]),5,20)
    display.text("{}".format(days[weekday]),20,30)

    display.text("{}:{}:{}".format(hour+3,minute,second),0,40)

    #display.text("{}:{}:".format(hour+3,minute,second),5,30)
    #display.text("{}".format(second),5,40)
    display.show()

    #utime.sleep(1)
