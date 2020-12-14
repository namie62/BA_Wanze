#!/usr/bin/python3
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio
import class_Led
import class_Servo
import class_Zustandsupdate
import Zielzustand
import xbox


def allgemeines_setup():
    gpio.setmode(gpio.BOARD) # !!!!Achtung!!!! GPIO Mode kann entweder BOARD oder BCM sein. BCM heißt, dass die GPIO Nummern gleich den GPIO Bezeichnungen sind, BOARD heißt, dass die GPIO am Raspberry PI selbst abgezählt sind
    gpio.setwarnings(False) #Wenn Warnungen an kommt ständig die Meldung, dass die Channels schon verwendet werden -> False
    
    
    
if __name__=="__main__":
    try:
        joy = xbox.Joystick()
        allgemeines_setup()
        led = class_Led.Led()
        ellbogen_servo1 = class_Servo.Servo("ellbogen_servo1")
        
        while not joy.Back():
            if joy.A():
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = 0  #Gradzahl
                led.stelle_farbe_ein("gruen")
            if joy.B():
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = 30
                led.stelle_farbe_ein("rot")
            if joy.X():
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = 90
                led.stelle_farbe_ein("blau")
            if joy.Y():
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = 180
                led.stelle_farbe_ein("orange")
        gpio.cleanup()
        
    except KeyboardInterrupt:  #finally
        gpio.cleanup()
                
            

        