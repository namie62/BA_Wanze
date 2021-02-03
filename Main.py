#!/usr/bin/python3
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio
import class_Led
import Zielzustand
import xbox
from class_Motorsteuerung import Motorsteuerung
import Adafruit_PCA9685
import class_Servo_Steuerung
import class_Fahrgestell
import class_Bewegungsablaeufe


def allgemeines_setup():
    gpio.setmode(gpio.BOARD) # !!!!Achtung!!!! GPIO Mode kann entwedenr BOARD oder BCM sein. BCM heißt, dass die GPIO Nummern gleich den GPIO Bezeichnungen sind, BOARD heißt, dass die GPIO am Raspberry PI selbst abgezählt sind
    gpio.setwarnings(False) #Wenn Warnungen an kommt ständig die Meldung, dass die Channels schon verwendet werden -> False
   # motorsteuerung = Motorsteuerung()
    return 0#motorsteuerung


if __name__=="__main__":
    try:
        joy = xbox.Joystick()
        motorsteuerung = allgemeines_setup()
        led = class_Led.Led()
       # bewegung = class_Bewegungsablaeufe.Bewegungsablaeufe()
       # class_Servo_Steuerung.Servo_Adafruit("ellbogen_servo_links", motorsteuerung)
        
        #class_Servo_Steuerung.Servo_Adafruit("ellbogen_servo_rechts", motorsteuerung)
        #class_Servo_Steuerung.Servo_Adafruit("schulter_servo_links", motorsteuerung)
        #class_Servo_Steuerung.Servo_Adafruit("schulter_servo_rechts", motorsteuerung)
        #class_Servo_Steuerung.Servo_Adafruit("nacken_servo", motorsteuerung)
        #class_Servo_Steuerung.Servo_Adafruit("helm_servo", motorsteuerung)
        class_Fahrgestell.Fahrgestell()
 
        
        while not joy.Back():

            
            if joy.leftY() > 0:
                bewegung.joystick_linker_arm_nach_oben()
                
            if joy.leftY() < 0:
                bewegung.joystick_linker_arm_nach_unten()
            
            if joy.leftX() > 0:
                bewegung.joystick_linker_ellbogen_nach_oben()
                
            if joy.leftX() < 0:
                bewegung.joystick_linker_ellbogen_nach_unten()
                
            if joy.rightY() > 0:
                bewegung.joystick_rechter_arm_nach_oben()
            
            if joy.rightY() < 0:
                bewegung.joystick_rechter_arm_nach_unten()
                
            if joy.rightX() > 0:
                bewegung.joystick_rechter_ellbogen_nach_oben()
            
            if joy.rightX() < 0:
                bewegung.joystick_rechter_ellbogen_nach_unten()

            if joy.A():
                led.stelle_farbe_ein("gruen")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (0,1,0) # Überschreibt bei Knopfdruck die Zielzustände mit (Prozentzahl/Gradzahl (aber lieber Prozent; kann in Konstanten der Servomodus eingestellt werden), Schrittanzahl)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (0,1,0) #(Prozentzahl/Gradzahl, Schrittanzahl, Toggle für Joytick?)
                Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (0,1,0) 
                Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts'] = (0,1,0) 
                Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (0,1,0)
                Zielzustand.ZIELZUSTAENDE['helm_servo'] = (0,1,0)
                
            if joy.B():
                led.stelle_farbe_ein("rot")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (50,5,0)  
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (50,1,0)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (10,1,0)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts'] = (10,1,0)  
                Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (10,1,0)  
                Zielzustand.ZIELZUSTAENDE['helm_servo'] = (10,1,0)  
                
            if joy.Y():
                led.stelle_farbe_ein("orange")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (20,1,0)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (20,1,0)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (20,1,0) 
                Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts']= (20,1,0)  
                Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (20,1,0)  
                Zielzustand.ZIELZUSTAENDE['helm_servo'] = (20,1,0)  
                 
            if joy.X():
                led.stelle_farbe_ein("blau")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (11,1,0)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (30,1,0)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (30,1,0)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts'] = (30,1,0)  
                Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (30,1,0)
                Zielzustand.ZIELZUSTAENDE['helm_servo'] = (30,1,0)  

            if joy.leftBumper():
                led.stelle_farbe_ein("giftgruen")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (50,1,0)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (50,1,0) 
                Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (50,1,0)  
                Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts'] = (50,1,0)  
                Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (50,1,0)  
                Zielzustand.ZIELZUSTAENDE['helm_servo'] = (50,1,0)  


            if joy.rightBumper() == 1:
                #print(joy.leftBumper())
                if joy.dpadLeft():
                    Zielzustand.ZIELZUSTAENDE['fahrgestell'] = (4)
                    led.stelle_farbe_ein("flieder")
                    
                if joy.dpadDown():
                    Zielzustand.ZIELZUSTAENDE['fahrgestell'] = (2)
                    led.stelle_farbe_ein("türkis")
                    
                if joy.dpadRight():
                    Zielzustand.ZIELZUSTAENDE['fahrgestell'] = (3)
                    led.stelle_farbe_ein("orange")    
                    
                if joy.dpadUp():
                    Zielzustand.ZIELZUSTAENDE['fahrgestell'] = (1)
                    led.stelle_farbe_ein("lila")
            else: 
                Zielzustand.ZIELZUSTAENDE['fahrgestell'] = (0)
    
    except KeyboardInterrupt:  
       gpio.cleanup()
                
                
            

        