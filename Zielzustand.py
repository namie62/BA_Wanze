#-*- coding: utf-8 -*-

#hier können beliebige Namen für Zielzustände gesetzt werden


ZIELZUSTAENDE = {
    "Notaus" : False, # direkt als Attribute: self.Notaus = bla bla
    "ellbogen_servo1" : [0,1], # 90 Grad muss Mitte sein
    "ellbogen_servo2" : [0,1],  # eingefahren 
    "schulter_servo1": [0,1], # Gradzahlen, 0 ist unten und dann gehts bis 180 weiter hoch
    "schulter_servo2" : [0,1],
    "nacken_servo" : [0,1], #Zustand 0 und 1, 0 heißt aus, 1 heißt an
    "helm_servo": [0,1],
                              # usw.
                              }