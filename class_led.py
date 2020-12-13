#-*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio

# Vorwiderstände der LEDs im Modell:
# rot: 270 Ohm    gruen: 220 Ohm     blau: 280 Ohm

FARBCODES = {"weiß" : (100,100,100),
                      "hellgruen" : (10,100,10),
                      "giftgruen" : (0,100,0),
                      "gruen" : (0,100,0),
                      "türkis" : (10,100,30),
                      "hellblau" : (20,30,100),
                      "blau" : (0,0,100),
                      "lila" : (100,0,100),
                      "flieder" : (70,0,100),
                      "hellrosa" : (100,20,30),
                      "pink" : (100,0,60),
                      "rot" : (100,0,0),
                      "orange" : (100,20,0),
                      "gelb" : (100,50,0)
                      }
# !!!!Achtung!!!! GPIO Mode kann entweder BOARD oder BCM sein. BCM heißt, dass die GPIO Nummern gleich den GPIO Bezeichnungen sind, BOARD heißt, dass die GPIO am Raspberry PI selbst abgezählt sind
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False) #Wenn Warnungen an kommt ständig die Meldung, dass die Channels schon verwendet werden -> False
FREQUENZ = 150   #50 ist grenzwertig, dass gedimmte LED nicht flackert, eher höher gehen und dann nicht von Motor Hat aus steuern 

class Led():
    # Initialisierung der Pins, bei anderen Pins einfach die Pin-Nummer ändern
    def start(self):
        self.rgb_pin_nummern = {
                    "rot_led1" : 12,
                    "gruen_led1" : 16,
                    "blau_led1" : 18,
                    "rot_led2": 11,
                    "gruen_led2": 13,
                    "blau_led2":15}

        self.pwm_objekte_led = self.setupleds(FREQUENZ)
    
    
    def stop(self):   
        for i in self.pwm_objekte_led:
            self.pwm_objekte_led.stop()
            


    # Definiert die GPIOs als Ausgänge und initialisiert und startet die Pulsweitenmodulation
    def setupleds(self, frequenz):  
        pwm_objekte_led = []
        for i in self.rgb_pin_nummern:
            gpio.setup(self.rgb_pin_nummern.get(i), gpio.OUT)
            pwm_objekt = gpio.PWM(self.rgb_pin_nummern.get(i), frequenz)
            #self.pwm_objekte_led.add(pwm_objekt)
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
            self.pwm_objekte_led[i].ChangeDutyCycle(FARBCODES.get(farbe)[j])
            j += 1
            if j == 3:
                j=0
            