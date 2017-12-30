import network
import urequests
from machine import I2C, Pin
import ssd1306
import time


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('SSID NAME', 'SSID PASSWORD')
    while not wlan.isconnected():
        pass
print('network config:', wlan.ifconfig())

i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(64, 48, i2c)
display.fill(0)

while True:
    print(time.localtime()[5])
    if(time.localtime()[5] % 5 ==0):
        #coinmarket
        response = urequests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/')
        data_btc = response.json()
        btc_price = data_btc[0]["price_usd"]
        print(btc_price)

        #paribu
        response2 = urequests.get('https://www.paribu.com/ticker')
        data_btc_paribu = response2.json()
        btc_price_tl = data_btc_paribu['BTC_TL']["last"]
        print(btc_price_tl)
                



        display.fill(0)
        display.text("1 BTC",10,0)
        display.text("$"+btc_price,0,15)
        display.text(str(btc_price_tl)+" TL",0,30)
        display.show()



