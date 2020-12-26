#!/usr/bin/python3
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio
import class_Led
import class_Servo
import Zielzustand
#import xbox
#from __future__ import division
import Adafruit_PCA9685
import adafruit_test

def allgemeines_setup():
    gpio.setmode(gpio.BOARD) # !!!!Achtung!!!! GPIO Mode kann entweder BOARD oder BCM sein. BCM heißt, dass die GPIO Nummern gleich den GPIO Bezeichnungen sind, BOARD heißt, dass die GPIO am Raspberry PI selbst abgezählt sind
    gpio.setwarnings(False) #Wenn Warnungen an kommt ständig die Meldung, dass die Channels schon verwendet werden -> False
    pwm = Adafruit_PCA9685.PCA9685(address=0x41)
    return pwm
    
if __name__=="__main__":
    try:
        #joy = xbox.Joystick()
        pwm = allgemeines_setup()
        #led = class_Led.Led()
        ellbogenmotor1 = adafruit_test.Servo_Adafruit("ellbogen_servo1", pwm)
        #ellbogen_servo1 = class_Servo.Servo("nacken_servo")
        
        while True:
            #led.stelle_farbe_ein("gruen")
            ellbogenmotor1.action()


    except KeyboardInterrupt:  #finally
        gpio.cleanup()