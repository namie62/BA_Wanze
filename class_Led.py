#-*- coding: utf-8 -*-
import RPi.GPIO as gpio
from Konstanten import LED_FREQUENZ, LED_PINS, FARBCODES

class Led():
    def __init__(self):
    # Initialisierung der Pins, bei anderen Pins einfach die Pin-Nummer ändern
        self.pwm_objekte_led = self.__setupleds(LED_FREQUENZ)
    
    #stoppt vor Herunterfahren alle Leds
    def stop(self):   
        gpio.cleanup()       

    # Definiert die GPIOs als Ausgänge und initialisiert und startet die Pulsweitenmodulation
    def __setupleds(self, frequenz):  
        pwm_objekte_led = []
        for i in LED_PINS:
            gpio.setup(LED_PINS.get(i), gpio.OUT)
            pwm_objekt = gpio.PWM(LED_PINS.get(i), frequenz)
            pwm_objekt.start(0)
            pwm_objekte_led.append(pwm_objekt)
        return pwm_objekte_led
        
    def stelle_farbe_ein(self, farbe):
        # Duty Cycle ändern um andere Farben und Helligkeiten einzustellen
        # -> nur Mittenwert der Versorgungsspannung von Bedeutung -> je größer Duty Cycle, umso heller 
        j = 0
        for i in range(len(self.pwm_objekte_led)):
            self.pwm_objekte_led[i].ChangeDutyCycle(FARBCODES.get(farbe)[j])
            j += 1
            if j == 3:
                j=0