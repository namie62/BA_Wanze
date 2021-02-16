#-*- coding: utf-8 -*-
import Zielzustand
import Emotionen
from threading import Thread
from time import sleep


# hier kommen die Methoden rein, welche die Standardbewegungsabläufe enthalten

class Bewegungsablaeufe():
    def __init__(self):
        self.emotion = Emotionen.Emotion()
    
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

    def froehlich(self):
        for i in range(2):
            Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("rechtskurve_vorwaerts")
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (80,1,0)
            Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (80,1,0)
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (60,1,0)
            Zielzustand.ZIELZUSTAENDE['helm_servo'] = (100,1,0)
            Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (30,1,0) 
            sleep(0.4)
            Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("linkskurve_vorwaerts")
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (0,1,0)
            Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (0,1,0)
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (0,1,0)
            Zielzustand.ZIELZUSTAENDE['helm_servo'] = (0,1,0)
            Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (60,1,0) 
            sleep(0.4)
            Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("stopp")
            
    def schuechtern(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts']= (0,1,0)
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (40,1,0)
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['schrittmotor'] = ("ausfahren")
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("vorwaerts")
        sleep(0.1)
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("stopp")
        sleep(1)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (20,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (20,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (20,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts']= (20,1,0)
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (60,1,0)
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (20,1,0)
            
    def angst(self):
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['schrittmotor'] = ("einfahren")
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("rueckwaerts")
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (80,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (80,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts']= (0,1,0)
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (40,1,0)
        sleep(0.2)
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("stopp")
        sleep(1)
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (20,1,0)
        sleep(0.2)
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (0,1,0)
        
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
    
    def nullposition(self):
        Zielzustand.ZIELZUSTAENDE['fahrgestell'] = ("stopp")
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = (0,1,0)
        Zielzustand.ZIELZUSTAENDE['schrittmotor'] = ("einfahren")



        
        
        
        
        
        
             
        
    

