#-*- coding: utf-8 -*-
import Zielzustand

# hier werden die Emotionen definiert, sprich:
# Emotion 1 hat folgenden Zielzustand:
# Wird aber noch nicht verwendet

class Emotion():
        
    WUT = {
        "ellbogen_servo1" : (0,1), #(Winkel, Schrittanzahl)
        "ellbogen_servo2" : (0,1), 
        "schulter_servo1": (0,1), 
        "schulter_servo2" : (0,1),
        "nacken_servo" : (0,1), 
        "helm_servo": (0,1),
        "led_farbe" : "rot"
        }
    
    
# in Main wird die Emotion übergeben 
    def stelle_emotion_ein(self, emotion):
        led.stelle_farbe_ein("gruen")
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo1'] = emotion.get("ellbogen_servo1") # Überschreibt bei Knopfdruck die Zielzustände mit (Gradzahl, Schrittanzahl)
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo2'] = emotion.get("ellbogen_servo2")  
        Zielzustand.ZIELZUSTAENDE['schulter_servo1'] = emotion.get("schulter_servo1")
        Zielzustand.ZIELZUSTAENDE['schulter_servo2'] = emotion.get("schulter_servo2")
        Zielzustand.ZIELZUSTAENDE['nacken_servo'] = emotion.get("nacken_servo")
        Zielzustand.ZIELZUSTAENDE['helm_servo'] = emotion.get("helm_servo")

        
        