#!/usr/bin/python3
#-*- coding: utf-8 -*-
import RPi.GPIO as gpio
import class_Led
import Zielzustand
import xbox
from class_Motorsteuerung import Motorsteuerung
import class_Servo_Steuerung
import class_Fahrgestell
import class_Bewegungsablaeufe
import class_Schrittmotor
import shutdown
from time import sleep

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
        #class_Schrittmotor.Schrittmotor()
        bewegung = class_Bewegungsablaeufe.Bewegungsablaeufe()
        class_Servo_Steuerung.Servo_Adafruit("ellbogen_servo_links", motorsteuerung)
        
        class_Servo_Steuerung.Servo_Adafruit("ellbogen_servo_rechts", motorsteuerung)
        class_Servo_Steuerung.Servo_Adafruit("schulter_servo_links", motorsteuerung)
        class_Servo_Steuerung.Servo_Adafruit("schulter_servo_rechts", motorsteuerung)
        class_Servo_Steuerung.Servo_Adafruit("nacken_servo", motorsteuerung)
        class_Servo_Steuerung.Servo_Adafruit("helm_servo", motorsteuerung)
        class_Fahrgestell.Fahrgestell()
                                                                 
        while True:
            if joy.leftTrigger():
                led.stop()
                bewegung.nullposition()
           
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
                bewegung.angst()
                
            if joy.B():
                led.stelle_farbe_ein("rot")
                bewegung.froehlich()

            if joy.Y():
                led.stelle_farbe_ein("orange")
                bewegung.schuechtern()
               
                 
            if joy.X():
                led.stelle_farbe_ein("blau")
                bewegung.winken()
                

            if joy.leftBumper():
                led.stelle_farbe_ein("hellrosa")
                bewegung.kopfschuetteln()
                
                 
            if joy.rightTrigger() >= 1:
                #print(joy.leftBumper())
                if joy.dpadLeft():
                    Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("linkskurve_vorwaerts")
                    led.stelle_farbe_ein("flieder")
                    
                if joy.dpadDown():
                    Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("rueckwaerts")
                    led.stelle_farbe_ein("türkis")
                    
                if joy.dpadRight():
                    Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("rechtskurve_vorwaerts")
                    led.stelle_farbe_ein("orange")    
                    
                if joy.dpadUp():
                    Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("vorwaerts")
                    led.stelle_farbe_ein("lila")
            else: 
                Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("stopp")
                
            if joy.rightBumper():
                if joy.dpadUp():
                    Zielzustand.ZIELZUSTAENDE['schrittmotor'] = ("ausfahren")
                if joy.dpadDown():
                    Zielzustand.ZIELZUSTAENDE['schrittmotor'] = ("einfahren")
            else:
                Zielzustand.ZIELZUSTAENDE['schrittmotor'] = ("stopp")
    
            if joy.Start():
                if joy.Back():
                    gpio.cleanup()
                    shutdown.shutdown()
                
    
    except KeyboardInterrupt:
        
       gpio.cleanup()
                
                
            

        