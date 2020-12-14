import xbox
from threading import Thread
import Zielzustand 
import time

#KNOEPFE = ["leftX", "leftY", "rightX", "rightY", "dpadUp", "dpadDown", "dpadLeft", "dpadRight", "Guide", Start", leftThumbstick, rightThumbstick, A, B, X, Y, leftBumper,rightBumper, leftTrigger, rightTrigger, leftStick, rightStick] 

class Zustandsupdate():
    def __init__(self):
        self.joy = xbox.Joystick()
  
    def update_zielzustand(self): # schauen, dass evtl nur dann Aktion ausgelöst wird, wenn alter Zielzustand != neuer Zielzustand
        Zielzustand.ALTER_ZIELZUSTAND = Zielzustand.ZIELZUSTAENDE
        
        if self.joy.A():
            Zielzustand.ZIELZUSTAENDE['Nacken'] = "ganz nach links gedreht"
            Zielzustand.ZIELZUSTAENDE['Kopf'] = "links"
        if self.joy.B():
            Zielzustand.ZIELZUSTAENDE['Nacken'] = "mittig"
            Zielzustand.ZIELZUSTAENDE['Kopf'] = "rechts"
        if self.joy.X():
            Zielzustand.ZIELZUSTAENDE['Nacken'] = "mittig"
            Zielzustand.ZIELZUSTAENDE['Kopf'] = "rechts"
        if self.joy.Y():
            Zielzustand.ZIELZUSTAENDE['Nacken'] = "mittig"
            Zielzustand.ZIELZUSTAENDE['Kopf'] = "rechts"
                
       # print("update", Zielzustand.ZIELZUSTAENDE)
        #print("alt", Zielzustand.ALTER_ZIELZUSTAND)
                
        time.sleep(0.1)
                    
                
                

        