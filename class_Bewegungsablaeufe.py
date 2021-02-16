#-*- coding: utf-8 -*-
import Zielzustand
import Emotionen
from threading import Thread
from time import sleep


# hier kommen die Methoden rein, welche die Standardbewegungsabläufe enthalten

class Bewegungsablaeufe():
    def __init__(self):
        self.emotion = Emotionen.Emotion()
        
        
    def wackel_mit_den_armen(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (100,1,-1)
#         self.thread = Thread(target = self.__action) 
#         self.thread.start()
        
    def __action(self):
        for i in range(2):
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (100,1,-1)
#             Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (50,1,-1)
#             Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (100,1,-1)
#             Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts'] = (50,1,-1)
  
#             Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (0,1,-1)
#             Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (0,1,-1)
#             Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (0,1,-1)
#             Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts'] = (0,1,-1)
        sleep(5)
            
    
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

   # def froehlich(self):
        
             
        
    

