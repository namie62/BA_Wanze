#!/usr/bin/python3
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio
import class_Led
import class_Servo
import Zielzustand
import xbox
#from __future__ import division
import Adafruit_PCA9685
import adafruit_test

def allgemeines_setup():
    gpio.setmode(gpio.BOARD) # !!!!Achtung!!!! GPIO Mode kann entweder BOARD oder BCM sein. BCM heißt, dass die GPIO Nummern gleich den GPIO Bezeichnungen sind, BOARD heißt, dass die GPIO am Raspberry PI selbst abgezählt sind
    gpio.setwarnings(False) #Wenn Warnungen an kommt ständig die Meldung, dass die Channels schon verwendet werden -> False
    pwm = Adafruit_PCA9685.PCA9685(address=0x41)
    return pwm
    
    
if __name__=="__main__":
    #try:
        joy = xbox.Joystick()
        pwm = allgemeines_setup()
        led = class_Led.Led()
        ellbogen_servo1 = adafruit_test.Servo_Adafruit("ellbogen_servo1", pwm)
        ellbogen_servo2 = adafruit_test.Servo_Adafruit("ellbogen_servo2", pwm)
        schulter_servo1 = adafruit_test.Servo_Adafruit("schulter_servo1", pwm)
        #schulter_servo2 = adafruit_test.Servo_Adafruit("schulter_servo2", pwm)
        #nacken_servo = adafruit_test.Servo_Adafruit("nacken_servo", pwm)
        #helm_servo = adafruit_test.Servo_Adafruit("helm_servo", pwm)
        
        while not joy.Back():
            if joy.A():
                led.stelle_farbe_ein("gruen")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'][0] = 180  #Gradzahl
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'][1] = 1
                
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'][0] = 180  #Gradzahl
                Zielzustand.ZIELZUSTAENDE['schulter_servo1'][0] = 180  #Gradzahl
                Zielzustand.ZIELZUSTAENDE['schulter_servo2'][0] = 180  #Gradzahl
                Zielzustand.ZIELZUSTAENDE['nacken_servo'][0] = 180  #Gradzahl                                                                                                                                                                                                          ervo'][0] = 180  #Gradzahl
                #Zielzustand.ZIELZUSTAENDE['helm_servo'][0] = 180  #Gradzahl
            if joy.B():
                led.stelle_farbe_ein("rot")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'][0] = 30  #Gradzahl
 
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'][0] = 30  #Gradzahl
                Zielzustand.ZIELZUSTAENDE['schulter_servo1'][0] = 30  #Gradzahl
                Zielzustand.ZIELZUSTAENDE['schulter_servo2'][0] = 30  #Gradzahl
                Zielzustand.ZIELZUSTAENDE['nacken_servo'][0] = 30  #Gradzahl
#                 Zielzustand.ZIELZUSTAENDE['helm_servo'][0] = 30  #Gradzahl
#                 
            if joy.X():
                led.stelle_farbe_ein("blau")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'][0] = 90
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'][1] = 9
                 
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'][0] = 90  #Gradzahl
                Zielzustand.ZIELZUSTAENDE['schulter_servo1'][0] = 90  #Gradzahl
                Zielzustand.ZIELZUSTAENDE['schulter_servo2'][0] = 90  #Gradzahl
                Zielzustand.ZIELZUSTAENDE['nacken_servo'][0] = 90  #Gradzahl
#                 Zielzustand.ZIELZUSTAENDE['helm_servo'][0] = 90  #Gradzahl
                
            if joy.Y():
                led.stelle_farbe_ein("orange")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'][0] = 10
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'][1] = 3
                 
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'][0] = 10  #Gradzahl
                Zielzustand.ZIELZUSTAENDE['schulter_servo1'][0] = 10  #Gradzahl
                Zielzustand.ZIELZUSTAENDE['schulter_servo2'][0] = 10  #Gradzahl
                Zielzustand.ZIELZUSTAENDE['nacken_servo'][0] = 10  #Gradzahl
#                 Zielzustand.ZIELZUSTAENDE['helm_servo'][0] = 10  #Gradzahl
                
        gpio.cleanup()
        
   # except KeyboardInterrupt:  #finally
    #   gpio.cleanup()
                
            

        