#!/usr/bin/python3
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio
import class_Led
import Zielzustand
import Adafruit_PCA9685
import class_Servo_Steuerung
from motorsteuerung import Motorsteuerung


# falls gerade kein Controller vorhanden ist, kann mit diesem Main File trotzdem programmiert und ausgetestet werden als abgespeckte Version der Main.py

def allgemeines_setup():
    gpio.setmode(gpio.BOARD) # !!!!Achtung!!!! GPIO Mode kann entweder BOARD oder BCM sein. BCM heißt, dass die GPIO Nummern gleich den GPIO Bezeichnungen sind, BOARD heißt, dass die GPIO am Raspberry PI selbst abgezählt sind
    gpio.setwarnings(False) #Wenn Warnungen an kommt ständig die Meldung, dass die Channels schon verwendet werden -> False
    motorsteuerung = Motorsteuerung()
    return motorsteuerung
    
    
if __name__=="__main__":
    try:
        motorsteuerung = allgemeines_setup()
        led = class_Led.Led()
        ellbogen_servo1 = class_Servo_Steuerung.Servo_Adafruit("ellbogen_servo1", motorsteuerung)
        ellbogen_servo2 = class_Servo_Steuerung.Servo_Adafruit("ellbogen_servo2", motorsteuerung)
        schulter_servo1 = class_Servo_Steuerung.Servo_Adafruit("schulter_servo1", motorsteuerung)
        schulter_servo2 = class_Servo_Steuerung.Servo_Adafruit("schulter_servo2", motorsteuerung)
        nacken_servo = class_Servo_Steuerung.Servo_Adafruit("nacken_servo", motorsteuerung)
        helm_servo = class_Servo_Steuerung.Servo_Adafruit("helm_servo", motorsteuerung)
        
        while True:
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = (180,1) #Gradzahl
                led.stelle_farbe_ein("gruen")
                time.sleep(5)
                Zielzustand.ZIELZUSTAENDE['schulter_servo1']= (90,1) #Gradzahl
                

    except KeyboardInterrupt:  
        gpio.cleanup()