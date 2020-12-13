#-*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio
import Konstanten

class Led():
    def __init__(self):
    # Initialisierung der Pins, bei anderen Pins einfach die Pin-Nummer ändern

        self.pwm_objekte_led = self.setupleds(Konstanten.LED_FREQUENZ)
    
    
    def stop(self):   
        for i in self.pwm_objekte_led:
            self.pwm_objekte_led.stop()
            


    # Definiert die GPIOs als Ausgänge und initialisiert und startet die Pulsweitenmodulation
    def setupleds(self, frequenz):  
        pwm_objekte_led = []
        for i in Konstanten.RGB_PIN_NUMMERN:
            gpio.setup(Konstanten.RGB_PIN_NUMMERN.get(i), gpio.OUT)
            pwm_objekt = gpio.PWM(Konstanten.RGB_PIN_NUMMERN.get(i), frequenz)
            pwm_objekt.start(0)
            pwm_objekte_led.append(pwm_objekt)
        return pwm_objekte_led

            
    def aus(self): 
        for i in range(len(self.pwm_objekte_led)): # Duty Cycle ändern um andere Farben und Helligkeiten einzustellen
            self.pwm_objekte_led[i].ChangeDutyCycle(0) # -> nur Mittenwert der Versorgungsspannung von Bedeutung -> je größer Duty Cycle, umso heller
        
        
    def stelle_farbe_ein(self, farbe):
        # Duty Cycle ändern um andere Farben und Helligkeiten einzustellen
        # -> nur Mittenwert der Versorgungsspannung von Bedeutung -> je größer Duty Cycle, umso heller 
        j = 0
        for i in range(len(self.pwm_objekte_led)):
            self.pwm_objekte_led[i].ChangeDutyCycle(Konstanten.FARBCODES.get(farbe)[j])
            j += 1
            if j == 3:
                j=0
            