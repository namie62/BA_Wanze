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
        
        