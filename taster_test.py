from time import sleep
import RPi.GPIO as gpio
from Konstanten import TASTER

print(TASTER)

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

taster = 40
gpio.setup(taster, gpio.IN)
time = 0.01



while(True):
    if gpio.input(taster) == True:
        i=1
        print(i)
        while gpio.input(taster)== True:
            sleep(time)
    
    else:
        i = 0
        print(i)
        while gpio.input(taster) == False:
            sleep(time)
    
    sleep(time)
    
print('test')