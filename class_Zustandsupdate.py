import xbox
from threading import Thread
import Zielzustand 
import time

#KNOEPFE = ["leftX", "leftY", "rightX", "rightY", "dpadUp", "dpadDown", "dpadLeft", "dpadRight", "Guide", Start", leftThumbstick, rightThumbstick, A, B, X, Y, leftBumper,rightBumper, leftTrigger, rightTrigger, leftStick, rightStick] 

class Zustandsupdate():
    def __init__(self):
       # self.zielzustandsobjekt = zielzustandsobjekt
        self.joy = xbox.Joystick()
        self.thread = Thread(target = self.update_zielzustand)
        self.thread.start()
    
        
    def update_zielzustand(self): # schauen, dass evtl nur dann Aktion ausgelöst wird, wenn alter Zielzustand != neuer Zielzustand
        while True:
            if self.joy.A():
                #print("update", Zielzustand.ZIELZUSTAENDE)
                Zielzustand.ZIELZUSTAENDE['Nacken'] = "ganz nach links gedreht"
                Zielzustand.ZIELZUSTAENDE['Kopf'] = "links"
            if self.joy.B():
                Zielzustand.ZIELZUSTAENDE['Nacken'] = "mittig"
                Zielzustand.ZIELZUSTAENDE['Kopf'] = "rechts"

                
            time.sleep(0.1)
                    
                
                

        