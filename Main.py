#!/usr/bin/python3
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio
import class_Led
import class_Servo
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
        ellbogen_servo1 = class_Servo.Servo("nacken_servo")
        
        while not joy.Back():
            if joy.A():
                Zielzustand.ZIELZUSTAENDE['nacken_servo'][0] = 180  #Gradzahl
                Zielzustand.ZIELZUSTAENDE['nacken_servo'][1] = 1
                led.stelle_farbe_ein("gruen")
            if joy.B():
                Zielzustand.ZIELZUSTAENDE['nacken_servo'][0] = 30
                Zielzustand.ZIELZUSTAENDE['nacken_servo'][1] = 3
                led.stelle_farbe_ein("rot")
            if joy.X():
                Zielzustand.ZIELZUSTAENDE['nacken_servo'][0] = 90
                Zielzustand.ZIELZUSTAENDE['nacken_servo'][1] = 9
                led.stelle_farbe_ein("blau")
            if joy.Y():
                Zielzustand.ZIELZUSTAENDE['nacken_servo'][0] = 180
                Zielzustand.ZIELZUSTAENDE['nacken_servo'][1] = 18
                led.stelle_farbe_ein("orange")
        gpio.cleanup()
        
    except KeyboardInterrupt:  #finally
        gpio.cleanup()
                
            

        