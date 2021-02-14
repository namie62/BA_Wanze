#-*- coding: utf-8 -*-
from time import sleep
import RPi.GPIO as gpio
from threading import Thread
from Zielzustand import ZIELZUSTAENDE 
from Konstanten import MOTOREN_und_LED_CHANNELS, FAHRGESTELL_FREQUENZ

class Fahrgestell():
    def __init__(self):
        #holt sich die Pin-Nummern aus Konstanten.py
        pin_nummern = MOTOREN_und_LED_CHANNELS.get("fahrgestell")
        pin1_rechts = pin_nummern[0] #PIN 21
        pin2_rechts = pin_nummern[1] #PIN 22
        pin1_links = pin_nummern[2] #PIN 23
        pin2_links = pin_nummern[3] #PIN 24

        for i in range(len(MOTOREN_und_LED_CHANNELS.get("fahrgestell"))):
            gpio.setup(MOTOREN_und_LED_CHANNELS.get("fahrgestell")[i], gpio.OUT)
        
        #initialisiert PWM
        self.in1_rechts = gpio.PWM(pin1_rechts, FAHRGESTELL_FREQUENZ)
        self.in2_rechts = gpio.PWM(pin2_rechts, FAHRGESTELL_FREQUENZ)
        self.in1_links = gpio.PWM(pin1_links, FAHRGESTELL_FREQUENZ)
        self.in2_links = gpio.PWM(pin2_links, FAHRGESTELL_FREQUENZ)
        
        #startet PWM
        self.in1_rechts.start(0)
        self.in2_rechts.start(0)
        self.in1_links.start(0)
        self.in2_links.start(0)
        
        #initialisiert und startet Thread
        self.thread = Thread(target = self.__action) # initialisiert und startet für jeden Servo einen eigenen Thread
        self.thread.start() 

    def __action(self):
        while True:
            self.zielzustand = ZIELZUSTAENDE.get("fahrgestell")
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
            sleep(0.00001)
                
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