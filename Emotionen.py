#-*- coding: utf-8 -*-
import Zielzustand
import class_Led
# hier werden die Emotionen definiert, sprich:
# Emotion 1 hat folgenden Zielzustand:
# Wird aber noch nicht verwendet

class Emotion():
    def __init__(self):
                
        self.SCHUECHTERN = {
            "ellbogen_servo_links" : (0,1,0), #(Winkel, Schrittanzahl)
            "ellbogen_servo_rechts" : (0,1,0), 
            "schulter_servo_links": (0,1,0), 
            "schulter_servo_rechts" : (0,1,0),
            "nacken_servo" : (0,1,0), 
            "helm_servo": (0,1,0),
            "led_farbe" : "rot"
            }


# in Main wird die Emotion übergeben 
    def stelle_emotion_ein(self, emotion):
        self.led.stelle_farbe_ein(emotion.get("led_farbe"))
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = emotion.get("ellbogen_servo1") # Überschreibt bei Knopfdruck die Zielzustände mit (Gradzahl, Schrittanzahl)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = emotion.get("ellbogen_servo2")  
        Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = emotion.get("schulter_servo1")
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts'] = emotion.get("schulter_servo2")
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = emotion.get("nacken_servo")
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = emotion.get("helm_servo")

        
        