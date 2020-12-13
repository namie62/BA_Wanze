#-*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio

# Vorwiderstände der LEDs im Modell:
# rot: 270 Ohm    gruen: 220 Ohm     blau: 280 Ohm


#farbcodes evlt hier reinschreiben statt in Methode in CAPS schreiben
# Ginge auch in eigene Konstanten File und importieren


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

        # !!!!Achtung!!!! GPIO Mode kann entweder BOARD oder BCM sein. BCM heißt, dass die GPIO Nummern gleich den GPIO Bezeichnungen sind, BOARD heißt, dass die GPIO am Raspberry PI selbst abgezählt sind
        gpio.setmode(gpio.BOARD)
        gpio.setwarnings(False) #Wenn Warnungen an kommt ständig die Meldung, dass die Channels schon verwendet werden -> False
        
        frequenz = 150   #50 ist grenzwertig, dass gedimmte LED nicht flackert, eher höher gehen und dann nicht von Motor Hat aus steuern 
        self.pwm_objekte_led = self.setupleds(frequenz)
        self.farbcodes = self.setupcolours()
    
    
    def stop(self):   #evtl Schleife machen 
        self.pwm_objekte_led[0].stop()
        self.pwm_objekte_led[1].stop()
        self.pwm_objekte_led[2].stop()
        self.pwm_objekte_led[3].stop()
        self.pwm_objekte_led[4].stop()
        self.pwm_objekte_led[5].stop()
        
        #gpio.cleanup()
        
    # Definiert die GPIOs als Ausgänge und initialisiert und startet die Pulsweitenmodulation
    def setupleds(self, frequenz):  #Als Schleife machen 
        gpio.setup(self.rgb_pin_nummern.get("rot_led1"), gpio.OUT)   # die verschiedenen Pins der verschiedenen LED und Farben als Output definieren
        gpio.setup(self.rgb_pin_nummern.get("gruen_led1"), gpio.OUT)
        gpio.setup(self.rgb_pin_nummern.get("blau_led1"), gpio.OUT)
        gpio.setup(self.rgb_pin_nummern.get("rot_led2"), gpio.OUT)
        gpio.setup(self.rgb_pin_nummern.get("gruen_led2"), gpio.OUT)
        gpio.setup(self.rgb_pin_nummern.get("blau_led2"), gpio.OUT)
        
        rot_led1 = gpio.PWM(self.rgb_pin_nummern.get("rot_led1"), frequenz)  # Pulsweitenmodulation initialisieren mit Pin-Nummer und Frequenz für erste LED
        gruen_led1 = gpio.PWM(self.rgb_pin_nummern.get("gruen_led1"), frequenz)
        blau_led1 = gpio.PWM(self.rgb_pin_nummern.get("blau_led1"),frequenz)
        
        rot_led2 = gpio.PWM(self.rgb_pin_nummern.get("rot_led2"), frequenz)  # Pulsweitenmodulation initialisieren mit Pin-Nummer und Frequenz für zweite LED
        gruen_led2 = gpio.PWM(self.rgb_pin_nummern.get("gruen_led2"), frequenz)
        blau_led2 = gpio.PWM(self.rgb_pin_nummern.get("blau_led2"),frequenz)
        
        rot_led1.start(0)    # Pulsweitenmodulation starten mit Wert 0, damit keine Lampe leuchtet
        gruen_led1.start(0)
        blau_led1.start(0)
        
        rot_led2.start(0)   # das Gleiche für die zweite LED 
        gruen_led2.start(0)
        blau_led2.start(0)
        
        pwm_objekte_led = (rot_led1, gruen_led1, blau_led1, rot_led2, gruen_led2, blau_led2) # Die initialisierten PWM-Objekte in Tupel zusammengefasst
        return pwm_objekte_led



    def setupcolours(self):    #Farben RGB Werte initialisieren und Liste erstellen; Werte sind ausprobierte Werte, in welchen Anteilen welche Farbe eingehen muss, um gewünschte
        # Farbe zu erzielen. Die versch. Farben RGB sind unterschiedlich hell von haus aus und auch durch die unterschiedlichen Vorwiderstände
        farbcodes = {"weiß" : (100,100,100),
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
        return farbcodes
    
    def farbintensitaet(self, intensitaet):  # Schleife
            self.pwm_objekte_led[0].ChangeDutyCycle(intensitaet*100)
            self.pwm_objekte_led[1].ChangeDutyCycle(intensitaet*100)
            self.pwm_objekte_led[2].ChangeDutyCycle(intensitaet*100)
            self.pwm_objekte_led[3].ChangeDutyCycle(intensitaet*100)
            self.pwm_objekte_led[4].ChangeDutyCycle(intensitaet*100)
            self.pwm_objekte_led[5].ChangeDutyCycle(intensitaet*100)
            time.sleep(0.5)
        

    
    def farbverlauf(self):  #Schleife
        for i in self.farbcodes:
            self.pwm_objekte_led[0].ChangeDutyCycle(self.farbcodes.get(i)[0])
            self.pwm_objekte_led[1].ChangeDutyCycle(self.farbcodes.get(i)[1])
            self.pwm_objekte_led[2].ChangeDutyCycle(self.farbcodes.get(i)[2])
            self.pwm_objekte_led[3].ChangeDutyCycle(self.farbcodes.get(i)[0])
            self.pwm_objekte_led[4].ChangeDutyCycle(self.farbcodes.get(i)[1])
            self.pwm_objekte_led[5].ChangeDutyCycle(self.farbcodes.get(i)[2])
            time.sleep(0.5)
            
            
    def aus(self): #Schleife 
        self.pwm_objekte_led[0].ChangeDutyCycle(0)    # Duty Cycle ändern um andere Farben und Helligkeiten einzustellen
        self.pwm_objekte_led[1].ChangeDutyCycle(0)    # -> nur Mittenwert der Versorgungsspannung von Bedeutung -> je größer Duty Cycle, umso heller 
        self.pwm_objekte_led[2].ChangeDutyCycle(0)    
        self.pwm_objekte_led[3].ChangeDutyCycle(0)
        self.pwm_objekte_led[4].ChangeDutyCycle(0)
        self.pwm_objekte_led[5].ChangeDutyCycle(0)
        
    def stelle_farbe_ein(self, farbe): #Schleife
        self.pwm_objekte_led[0].ChangeDutyCycle(self.farbcodes.get(farbe)[0])    # Duty Cycle ändern um andere Farben und Helligkeiten einzustellen
        self.pwm_objekte_led[1].ChangeDutyCycle(self.farbcodes.get(farbe)[1])    # -> nur Mittenwert der Versorgungsspannung von Bedeutung -> je größer Duty Cycle, umso heller 
        self.pwm_objekte_led[2].ChangeDutyCycle(self.farbcodes.get(farbe)[2])    
        self.pwm_objekte_led[3].ChangeDutyCycle(self.farbcodes.get(farbe)[0])
        self.pwm_objekte_led[4].ChangeDutyCycle(self.farbcodes.get(farbe)[1])
        self.pwm_objekte_led[5].ChangeDutyCycle(self.farbcodes.get(farbe)[2])
        
