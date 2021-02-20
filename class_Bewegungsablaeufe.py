#-*- coding: utf-8 -*-
import Zielzustand
from threading import Thread
from time import sleep


# hier kommen die Methoden rein, welche die Standardbewegungsabläufe enthalten

class Bewegungsablaeufe():
    
    def joystick_linker_arm_nach_oben(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (100,1,1)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (100,1,1)
        
    def joystick_rechter_arm_nach_oben(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (100,1,1)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts'] = (100,1,1)

    def joystick_linker_arm_nach_unten(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (0,1,2)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (0,1,2)
        
    def joystick_rechter_arm_nach_unten(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (0,1,2)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts'] = (0,1,2)

    def joystick_rechter_ellbogen_nach_oben(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (100,1,1)

    def joystick_linker_ellbogen_nach_oben(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (100,1,1)
    
    def joystick_linker_ellbogen_nach_unten(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (0,1,2)
        
    def joystick_rechter_ellbogen_nach_unten(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (0,1,2)
    
    def kopf_nach_rechts_neigen(self):
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (60,1,0)
    
    def kopf_nach_links_neigen(self):
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (30,1,0)
    
    def hals_ausfahren(self):
        Zielzustand.ZIELZUSTAENDE['schrittmotor'] = ("ausfahren")
    
    def hals_einfahren(self):
        Zielzustand.ZIELZUSTAENDE['schrittmotor'] = ("einfahren")
        
    def hals_stoppen(self):
        Zielzustand.ZIELZUSTAENDE['schrittmotor'] = ("stopp")
        
    def vorwaerts_fahren(self):
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("vorwaerts")
        
    def rueckwaerts_fahren(self):
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("rueckwaerts")
        
    def linkskurve(self):
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("linkskurve_vorwaerts")

    def rechtskurve(self):
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("rechtskurve_vorwaerts")
    
    def anhalten(self):
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("stopp")

    def neugier(self, led):
        t = 0.2
        led.stelle_farbe_ein("gruendimmung1")
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("vorwaerts")
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (100,1,0)
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (30,1,0)  
        Zielzustand.ZIELZUSTAENDE['schrittmotor'] = ("ausfahren")
        sleep(t)
        led.stelle_farbe_ein("gruendimmung1")
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (90,1,0)
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("stopp")
        sleep(t)
        led.stelle_farbe_ein("gruendimmung2")
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (80,1,0)
        sleep(t)
        led.stelle_farbe_ein("gruendimmung3")
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (70,1,0)
        sleep(t)
        led.stelle_farbe_ein("gruendimmung4")
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (60,1,0)
        sleep(t)
        led.stelle_farbe_ein("gruendimmung5")
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (50,1,0)
        sleep(t)
        led.stelle_farbe_ein("gruendimmung6")
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (40,1,0)
        sleep(t)
        led.stelle_farbe_ein("gruendimmung7")
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (30,1,0)
        sleep(t)
        led.stelle_farbe_ein("gruendimmung8")
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (20,1,0)
        sleep(t)
        led.stelle_farbe_ein("gruendimmung8")
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (10,1,0)
        sleep(t)
        led.stelle_farbe_ein("gruendimmung8")
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (60,1,0)
        sleep(t)
        led.stelle_farbe_ein("gruendimmung9")
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (0,1,0)
        sleep(t)
        led.stelle_farbe_ein("gruendimmung10")
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (60,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (10,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts']= (5,1,0)
        sleep(t)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (20,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts']= (10,1,0)
        sleep(t)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (30,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts']= (15,1,0)
        sleep(t)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (40,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts']= (20,1,0)
        
        
        
        

    def wut(self, led):
        t = 0.2
        led.stelle_farbe_ein("rot")
        Zielzustand.ZIELZUSTAENDE['schrittmotor'] = ("ausfahren")
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (10,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (10,1,0)
        sleep(t)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (20,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (20,1,0)
        sleep(t)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (30,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (30,1,0)
        sleep(t)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (40,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (40,1,0)
        led.stelle_farbe_ein("aus")
        sleep(t)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (50,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (50,1,0)
        sleep(t)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (60,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (60,1,0)
        sleep(t)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (70,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (70,1,0)
        led.stelle_farbe_ein("rot")
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (80,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (80,1,0)
        sleep(t)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (90,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (90,1,0)
        sleep(t)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (100,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (100,1,0)
        
        for i in range(2):
            led.stelle_farbe_ein("aus")
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (80,1,0)
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (80,1,0)
            sleep(t)
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (100,1,0)
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (100,1,0)
            led.stelle_farbe_ein("rot")
            sleep(t)
            
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (0,1,0)
        
        for i in range(2):
            led.stelle_farbe_ein("aus")
            Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("rechtskurve_vorwaerts")
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (80,1,0)
            Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (80,1,0)
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (60,1,0)
            Zielzustand.ZIELZUSTAENDE['helm_servo'] = (100,1,0)
            Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (30,1,0) 
            sleep(0.4)
            led.stelle_farbe_ein("rot")
            Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("linkskurve_vorwaerts")
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (0,1,0)
            Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (0,1,0)
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (0,1,0)
            Zielzustand.ZIELZUSTAENDE['helm_servo'] = (0,1,0)
            Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (60,1,0) 
            sleep(0.4)
            led.stelle_farbe_ein("aus")
            Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("stopp")
            
            
    def angst(self, led):
        led.stelle_farbe_ein("blau")
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (100,1,0)
        Zielzustand.ZIELZUSTAENDE['schrittmotor'] = ("einfahren")
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("rueckwaerts")
        led.stelle_farbe_ein("aus")
        # Helm und Arme zittern lassen und LED flackern
        sleep(0.1)
        led.stelle_farbe_ein("blau")   
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (80,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (80,1,0)
        led.stelle_farbe_ein("aus")
        sleep(0.3)
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("stopp")
        for i in range(6):
            Zielzustand.ZIELZUSTAENDE['helm_servo'] = (70,1,0)
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (0,1,0)
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (0,1,0)
            led.stelle_farbe_ein("blau")
            sleep(0.05)
            Zielzustand.ZIELZUSTAENDE['helm_servo'] = (100,1,0)
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (80,1,0)
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (80,1,0)
            led.stelle_farbe_ein("aus")
            sleep(0.05)
        
        
    def freude(self, led):
        led.stelle_farbe_ein("gelb")
        for i in range(2):
            Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (0,1,0)
            Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts']= (100,1,0)
            for i in range(2):
                Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("rueckwaerts")
                led.stelle_farbe_ein("tuerkis")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (80,1,0)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (80,1,0)
                sleep(0.3)
                Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("vorwaerts")
                led.stelle_farbe_ein("flieder")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (60,1,0)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (60,1,0)
                sleep(0.3)
                Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("rueckwaerts")
                led.stelle_farbe_ein("giftgruen")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (80,1,0)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (80,1,0)
                sleep(0.3)
                Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("vorwaerts")

                led.stelle_farbe_ein("pink")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (60,1,0)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (60,1,0)
                    
            Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (100,1,0)
            Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts']= (0,1,0)
            Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("stopp")

            
            for i in range(2):
                Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("rueckwaerts")
                led.stelle_farbe_ein("gelb")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (80,1,0)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (80,1,0)
                sleep(0.3)
                Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("vorwaerts")
                led.stelle_farbe_ein("tuerkis")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (60,1,0)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (60,1,0)
                sleep(0.3)
                Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("rueckwaerts")
                led.stelle_farbe_ein("flieder")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (80,1,0)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (80,1,0)
                sleep(0.3)
                Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("vorwaerts")
                led.stelle_farbe_ein("giftgruen")
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (60,1,0)
                Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (60,1,0)
            Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("stopp")
            
        
        
    def winken(self):
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (100,1,0)
        Zielzustand.ZIELZUSTAENDE['schrittmotor'] = ("ausfahren")
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("stopp")
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (60,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (100,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts']= (100,1,0)
        for i in range(3):
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (80,1,0)
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (80,1,0)
            sleep(0.1)
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (30,1,0)
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (30,1,0)
            sleep(0.1)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts']= (0,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (0,1,0)

    def kopfschuetteln(self):
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (40,1,0) # Nackenservo hat 40 als Nullposition
        sleep(0.1)
        for i in range(4):
            Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (50,1,0)
            sleep(0.1)
            Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (30,1,0)
    
    
    
    def nullposition(self, led):
        led.stelle_farbe_ein("aus")
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts'] = (0,1,0)

        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (40,1,0)
        Zielzustand.ZIELZUSTAENDE['schrittmotor'] = ("einfahren")



        
        
        
        
        
        
             
        
    

