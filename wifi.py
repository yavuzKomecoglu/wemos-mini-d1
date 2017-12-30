import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('SSID NAME', 'SSID PASSWORD')
    while not wlan.isconnected():
        pass
print('network config:', wlan.ifconfig())


#Access Point Config
#ap = network.WLAN(network.AP_IF)
#ap.active(True)
#ap.config(essid="wemos", authmode=network.AUTH_WPA_WPA2_PSK, password="wemo123")

