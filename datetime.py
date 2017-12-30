import machine
import utime
from ntptime import settime

days= {0:"Pzt", 1:"Sal", 2:"Çar", 3:"Per", 4:"Cum", 5:"Cmt", 6:"Paz"}
months = {1:"Oca", 2:"Şub", 3:"Mar", 4:"Nis", 5:"May", 6:"Haz", 7:"Tem", 8:"Ağu", 9:"Eyl", 10:"Eki", 11:"Kas", 12:"Ara"}

settime()

(year, month, mday, hour, minute, second, weekday, yearday) = utime.localtime()


print("Bugün {} {} {}".format(mday, months[month], days[weekday]))
print("Saat {}:{}:{}".format(hour+3,minute,second))




