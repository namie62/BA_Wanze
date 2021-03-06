import time
import RPi.GPIO as gpio
import Konstanten

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
pin_nummern = Konstanten.MOTOREN_und_LED_CHANNELS.get("fahrgestell")
pin1_rechts = pin_nummern[0]
pin2_rechts = pin_nummern[1]
pin1_links = pin_nummern[2]
pin2_links = pin_nummern[3]


for i in range(len(Konstanten.MOTOREN_und_LED_CHANNELS.get("fahrgestell"))):
    gpio.setup(Konstanten.MOTOREN_und_LED_CHANNELS.get("fahrgestell")[i], gpio.OUT)
    
jo = gpio.PWM(21, 100)
jo.start(100)



gpio.output(22, gpio.LOW)
#gpio.output(23, gpio.LOW)
#gpio.output(24, gpio.LOW)
time.sleep(30)

gpio.cleanup()
