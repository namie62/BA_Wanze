#-*- coding: utf-8 -*-

#hier können beliebige Namen für Zielzustände gesetzt werden


ZIELZUSTAENDE = {
    "Notaus" : False, # direkt als Attribute: self.Notaus = bla bla
    "ellbogen_servo1" : [180,1], # 90 Grad muss Mitte sein
    "nacken_servo" : [90,9],  # eingefahren 
    "Schulter_rechts": "0", # Gradzahlen, 0 ist unten und dann gehts bis 180 weiter hoch
    "Schulter_links" : "0",
    "Ellbogen_rechts": "0",
    "Ellbogen_links": "0",
    "Helm": "0",
                              # usw.
                              }