#-*- coding: utf-8 -*-
import xbox
import RPi.GPIO as gpio


class zielzustand():
    def __init__(self):
        self.joy = xbox.Joystick()
        #default Werte:
        self.zielzustaende = {"Notaus" : False, # direkt als Attribute: self.Notaus = bla bla 
                              "Kopf" : "gerade",
                              "Led" : "aus",
                              "Arm_rechts": "ausgestreckt", # Zu ungenau
                              "Arm_links" : "eingefahren"
                              # usw.
                              }


#Nicht Teil vom Zielzustand
#     def get_alle_zielzustaende(self):
#         return self.zielzustaende
#     
# 
#     def ermittle_zielzustand(self):
#            #while not self.joy.Back():
#                 if self.joy.rightBumper():
#                     self.zielzustaende["Kopf"]= "rechts"
#                 if self.joy.leftBumper():
#                     self.zielzustaende["Kopf"]= "links"
#                 if self.joy.A():
#                     self.zielzustaende["Led"] = "gruen"
#                     print("a")
#                 if self.joy.B():
#                     self.zielzustaende["Led"] = "rot"
#                 if self.joy.X():
#                     self.zielzustaende["Led"] = "blau"
#                 if self.joy.Y():
#                     self.zielzustaende["Led"] = "orange"
#                 if self.joy.Start():
#                     gpio.cleanup()
#                     self.joy.close()
#                 #usw..

        
        
