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

def led_blink_signal(led): #damit man sieht, dass Roboter bereit ist nach dem Hochfahren
    for i in range(2):
        led.stelle_farbe_ein("blau")
        sleep(0.5)
    
    led.stelle_farbe_ein("gelb")
        

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
        
    
        bewegung.nullposition(led)
        led_blink_signal(led)
                                                                 
        while True:
            if joy.Back():
                bewegung.nullposition(led)
           
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
                bewegung.nullposition(led)
                bewegung.neugier(led)
                
            if joy.B():
                bewegung.nullposition(led)
                bewegung.wut(led)

            if joy.Y():
                bewegung.nullposition(led)
                bewegung.freude(led)
               
            if joy.X():
                bewegung.nullposition(led)
                bewegung.angst(led)
                
                
#             if joy.leftBumper():
#                 led.stelle_farbe_ein("hellrosa")
#                 bewegung.kopfschuetteln()
                
                
            if joy.rightTrigger() >= 1:
                if joy.dpadLeft():
                    bewegung.linkskurve()
                if joy.dpadDown():
                    bewegung.rueckwaerts_fahren()
                if joy.dpadRight():
                    bewegung.rechtskurve() 
                if joy.dpadUp():
                    bewegung.vorwaerts_fahren()
            else: 
                bewegung.anhalten()
                
            
#             if joy.leftBumper():
#                 bewegung.hals_ausfahren()
#             if joy.rightBumper():
#                 bewegung.hals_einfahren()
                
                
            # Herunterfahren
            if joy.Start() and joy.Back():
                    gpio.cleanup()
                    shutdown.shutdown()
                
    
    except KeyboardInterrupt:
       gpio.cleanup()
                
                
            

        