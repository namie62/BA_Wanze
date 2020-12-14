import xbox
from threading import Thread
import Zielzustand 
import time

#KNOEPFE = ["leftX", "leftY", "rightX", "rightY", "dpadUp", "dpadDown", "dpadLeft", "dpadRight", "Guide", Start", leftThumbstick, rightThumbstick, A, B, X, Y, leftBumper,rightBumper, leftTrigger, rightTrigger, leftStick, rightStick] 


class Zustandsupdate():
    def __init__(self):
        self.joy = xbox.Joystick()
  
    def update_zielzustand(self): # schauen, dass evtl nur dann Aktion ausgelöst wird, wenn alter Zielzustand != neuer Zielzustand
        if self.joy.A():
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = 0
            
        if self.joy.B():
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = 90
            Zielzustand.ZIELZUSTAENDE['Led'] = "rot"
        if self.joy.X():
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = 180
            Zielzustand.ZIELZUSTAENDE['Led'] = "blau"
        if self.joy.Y():
            Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = 0
            Zielzustand.ZIELZUSTAENDE['Led'] = "orange"
                
       # print("update", Zielzustand.ZIELZUSTAENDE)
        #print("alt", Zielzustand.ALTER_ZIELZUSTAND)
                
        time.sleep(0.1)
                    
                
                

        