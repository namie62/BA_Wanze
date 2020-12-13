import xbox
from threading import Thread
from threading import Lock
import Zielzustand 
import time

#KNOEPFE = ["leftX", "leftY", "rightX", "rightY", "dpadUp", "dpadDown", "dpadLeft", "dpadRight", "Guide", Start", leftThumbstick, rightThumbstick, A, B, X, Y, leftBumper,rightBumper, leftTrigger, rightTrigger, leftStick, rightStick] 


Knopfausleselock = Lock()


class Zustandsupdate():
    def __init__(self):
       # self.zielzustandsobjekt = zielzustandsobjekt
        self.joy = xbox.Joystick()
        self.thread = Thread(target = self.update_zielzustand)
        self.thread.start()

    def update_zielzustand(self):
        while not self.joy.Back():
            if self.joy.A():
                print(Zielzustand.ZIELZUSTAENDE)
                Zielzustand.ZIELZUSTAENDE['Nacken'] = "ganz nach links gedreht"
                Zielzustand.ZIELZUSTAENDE['Kopf'] = "links"
            time.sleep(0.1)
                    
                
                

        