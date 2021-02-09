#-*- coding: utf-8 -*-

# Gradzahlen, 0 ist unten und dann gehts bis zum maximalen Winkel weiter hoch
ZIELZUSTAENDE = { 
    "ellbogen_servo_links" : (0,1,0), 
    "ellbogen_servo_rechts" : (0,1,0), 
    "schulter_servo_links": (0,1,0), 
    "schulter_servo_rechts" : (0,1,0),
    "nacken_servo" : (0,1,0), 
    "helm_servo": (0,1,0),
    "fahrgestell" : ("stopp")  # (toggle, richtung) 0 heißt aus, 1 ein und richtung 0 noch keine eingegeben, 1: vowärts; 2: rückwärts; 3: Rechtskurve; 4: Linkskurve
    }
