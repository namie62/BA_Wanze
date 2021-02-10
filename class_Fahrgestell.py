import time
import RPi.GPIO as gpio
import Konstanten
from threading import Thread
import Zielzustand

class Fahrgestell():
    def __init__(self):
        #gpio.setmode(gpio.BOARD)
        pin_nummern = Konstanten.MOTOREN_und_LED_CHANNELS.get("fahrgestell")
        pin1_rechts = pin_nummern[0] #PIN 21
        pin2_rechts = pin_nummern[1] #PIN 22
        pin1_links = pin_nummern[2] #PIN 23
        pin2_links = pin_nummern[3] #PIN 24

        for i in range(len(Konstanten.MOTOREN_und_LED_CHANNELS.get("fahrgestell"))):
            gpio.setup(Konstanten.MOTOREN_und_LED_CHANNELS.get("fahrgestell")[i], gpio.OUT)
        
        
        self.in1_rechts = gpio.PWM(pin1_rechts, Konstanten.FAHRGESTELL_FREQUENZ)
        self.in2_rechts = gpio.PWM(pin2_rechts, Konstanten.FAHRGESTELL_FREQUENZ)
        self.in1_links = gpio.PWM(pin1_links, Konstanten.FAHRGESTELL_FREQUENZ)
        self.in2_links = gpio.PWM(pin2_links, Konstanten.FAHRGESTELL_FREQUENZ)
        
        self.in1_rechts.start(0)
        self.in2_rechts.start(0)
        self.in1_links.start(0)
        self.in2_links.start(0)
        
        self.thread = Thread(target = self.action) # initialisiert und startet für jeden Servo einen eigenen Thread
        self.thread.start() 

    
    def action(self):
        while True:
            self.zielzustand = Zielzustand.ZIELZUSTAENDE.get("fahrgestell")
            if self.zielzustand == "stopp":
                self.anhalten()
            elif self.zielzustand == "vorwaerts":
                self.vorwaerts()
            elif self.zielzustand == "rueckwaerts":
                self.rueckwaerts()
            elif self.zielzustand == "rechtskurve_vorwaerts":
                self.rechtskurve()
            elif self.zielzustand == "linkskurve_vorwaerts":
                self.linkskurve()
            time.sleep(0.1)
                
    def anhalten(self):
        self.in1_rechts.ChangeDutyCycle(0)
        self.in2_rechts.ChangeDutyCycle(0)
        self.in1_links.ChangeDutyCycle(0)
        self.in2_links.ChangeDutyCycle(0)
        
    def vorwaerts(self):
        self.in1_rechts.ChangeDutyCycle(100)
        self.in2_rechts.ChangeDutyCycle(0)
        self.in1_links.ChangeDutyCycle(100)
        self.in2_links.ChangeDutyCycle(0)
    
    def rueckwaerts(self):
        self.in1_rechts.ChangeDutyCycle(0)
        self.in2_rechts.ChangeDutyCycle(100)
        self.in1_links.ChangeDutyCycle(0)
        self.in2_links.ChangeDutyCycle(100)
        
    def rechtskurve(self):
        self.in1_rechts.ChangeDutyCycle(0)
        self.in2_rechts.ChangeDutyCycle(100)
        self.in1_links.ChangeDutyCycle(100)
        self.in2_links.ChangeDutyCycle(0)
    
    def linkskurve(self):
        self.in1_rechts.ChangeDutyCycle(100)
        self.in2_rechts.ChangeDutyCycle(0)
        self.in1_links.ChangeDutyCycle(0)
        self.in2_links.ChangeDutyCycle(100)
        
           
        
