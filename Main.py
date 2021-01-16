#!/usr/bin/python3
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio
import class_Led
import Zielzustand
import xbox
from motorsteuerung import Motorsteuerung
import Adafruit_PCA9685
import class_Servo_Steuerung


def allgemeines_setup():
    gpio.setmode(gpio.BOARD) # !!!!Achtung!!!! GPIO Mode kann entwedenr BOARD oder BCM sein. BCM heißt, dass die GPIO Nummern gleich den GPIO Bezeichnungen sind, BOARD heißt, dass die GPIO am Raspberry PI selbst abgezählt sind
    gpio.setwarnings(False) #Wenn Warnungen an kommt ständig die Meldung, dass die Channels schon verwendet werden -> False
    motorsteuerung = Motorsteuerung()
    return motorsteuerung
    
    
if __name__=="__main__":
    try:
        joy = xbox.Joystick()
        motorsteuerung = allgemeines_setup()
        led = class_Led.Led()
        ellbogen_servo1 = class_Servo_Steuerung.Servo_Adafruit("ellbogen_servo1", motorsteuerung)
        ellbogen_servo2 = class_Servo_Steuerung.Servo_Adafruit("ellbogen_servo2", motorsteuerung)
        schulter_servo1 = class_Servo_Steuerung.Servo_Adafruit("schulter_servo1", motorsteuerung)
        schulter_servo2 = class_Servo_Steuerung.Servo_Adafruit("schulter_servo2", motorsteuerung)
        nacken_servo = class_Servo_Steuerung.Servo_Adafruit("nacken_servo", motorsteuerung)
        helm_servo = class_Servo_Steuerung.Servo_Adafruit("helm_servo", motorsteuerung)
        
        while not joy.Back():
            
            if joy.A():
                led.stelle_farbe_ein("gruen")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = (0,1) # Überschreibt bei Knopfdruck die Zielzustände mit (Gradzahl, Schrittanzahl)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'] = (0,1)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo1'] = (0,1) 
                Zielzustand.ZIELZUSTAENDE['schulter_servo2'] = (0,1) 
                Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (0,1)
                Zielzustand.ZIELZUSTAENDE['helm_servo'] = (0,1)
                
            if joy.B():
                led.stelle_farbe_ein("rot")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = (10,1)  
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'] = (110,1)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo1'] = (10,1)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo2'] = (10,1)  
                Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (10,1)  
                Zielzustand.ZIELZUSTAENDE['helm_servo'] = (10,1)  
                
            if joy.Y():
                led.stelle_farbe_ein("orange")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = (20,1)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'] = (20,1)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo1'] = (20,1) 
                Zielzustand.ZIELZUSTAENDE['schulter_servo2']= (20,1)  
                Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (20,1)  
                Zielzustand.ZIELZUSTAENDE['helm_servo'] = (20,1)  
                 
            if joy.X():
                led.stelle_farbe_ein("blau")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = (30,1)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'] = (30,1)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo1'] = (30,1)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo2'] = (30,1)  
                Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (30,1)
                Zielzustand.ZIELZUSTAENDE['helm_servo'] = (30,1)  

            if joy.rightBumper():
                led.stelle_farbe_ein("giftgruen")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = (50,1)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'] = (50,1) 
                Zielzustand.ZIELZUSTAENDE['schulter_servo1'] = (50,1)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo2'] = (50,1)  
                Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (50,1)  
                Zielzustand.ZIELZUSTAENDE['helm_servo'] = (50,1)  

            if joy.leftBumper():
                led.stelle_farbe_ein("weiß")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = (60,1)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'] = (60,1)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo1'] = (60,1)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo2'] = (60,1)  
                Zielzustand.ZIELZUSTAENDE['nacken_servo']= (60,1)  
                Zielzustand.ZIELZUSTAENDE['helm_servo'] = (60,1)  

            if joy.dpadLeft():
                led.stelle_farbe_ein("flieder")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = (80,1)  
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'] = (80,1)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo1'] = (80,1)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo2'] = (80,1)  
                Zielzustand.ZIELZUSTAENDE['nacken_servo']= (80,1)  
                Zielzustand.ZIELZUSTAENDE['helm_servo'] = (80,1)  

            if joy.dpadDown():
                led.stelle_farbe_ein("türkis")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = (90,1)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'] = (90,1)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo1'] = (90,1)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo2'] = (90,1)  
                Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (90,1)
                Zielzustand.ZIELZUSTAENDE['helm_servo'] = (90,1)

            if joy.dpadRight():
                led.stelle_farbe_ein("orange")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = (100,1)   
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'] =  (100,1)    
                Zielzustand.ZIELZUSTAENDE['schulter_servo1'] =  (100,1)    
                Zielzustand.ZIELZUSTAENDE['schulter_servo2']=  (100,1)    
                Zielzustand.ZIELZUSTAENDE['nacken_servo'] =  (100,1)    
                Zielzustand.ZIELZUSTAENDE['helm_servo'] =  (100,1)    

            if joy.dpadUp():
                led.stelle_farbe_ein("lila")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = (110,1)              
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'] = (110,1)   
                Zielzustand.ZIELZUSTAENDE['schulter_servo1'] = (110,1)   
                Zielzustand.ZIELZUSTAENDE['schulter_servo2'] = (110,1)   
                Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (110,1)   
                Zielzustand.ZIELZUSTAENDE['helm_servo'] = (110,1)   
                
    except KeyboardInterrupt:  
       gpio.cleanup()
                
            

        