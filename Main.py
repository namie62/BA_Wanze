#!/usr/bin/python3
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio
import class_Led
import class_Servo
import class_Zustandsupdate
import class_Action


def allgemeines_setup():
    gpio.setmode(gpio.BOARD) # !!!!Achtung!!!! GPIO Mode kann entweder BOARD oder BCM sein. BCM heißt, dass die GPIO Nummern gleich den GPIO Bezeichnungen sind, BOARD heißt, dass die GPIO am Raspberry PI selbst abgezählt sind
    gpio.setwarnings(False) #Wenn Warnungen an kommt ständig die Meldung, dass die Channels schon verwendet werden -> False
    
if __name__=="__main__":
    try:
        allgemeines_setup()
        #led = class_Led.Led()
        #ellbogen_servo1 = class_Servo.Servo("ellbogen_servo1") #gehört eig noch in action
        zustand_update = class_Zustandsupdate.Zustandsupdate()
        action = class_Action.Action()
        
    except KeyboardInterrupt:  #finally
        gpio.cleanup()
            
            

        