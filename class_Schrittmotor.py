#-*- coding: utf-8 -*-
from time import sleep
from datetime import datetime
import RPi.GPIO as gpio
from threading import Thread
from Zielzustand import ZIELZUSTAENDE
from Konstanten import MOTOREN_und_LED_CHANNELS, SCHRITTMOTOR_TABELLE, TASTER

class Schrittmotor():
    def __init__(self):
        
        #holt sich die Pin-Nummern und Tabelle aus Konstanten.py
        pin_nummern = MOTOREN_und_LED_CHANNELS.get("schrittmotor")
        
        self.A = pin_nummern[0] 
        self.B = pin_nummern[1]
        self.C = pin_nummern[2] 
        self.D = pin_nummern[3]
        self.taster = TASTER
        
        gpio.setmode(gpio.BOARD)
        
        gpio.setup(self.A, gpio.OUT)
        gpio.setup(self.B, gpio.OUT)
        gpio.setup(self.C, gpio.OUT)
        gpio.setup(self.D, gpio.OUT)
        gpio.setup(self.taster, gpio.IN)
        
        self.table = SCHRITTMOTOR_TABELLE
        self.position = 0
            
        self.default() #einmal alle auf gpio.LOW setzen zu Beginn, damit der Motor nichts tut von Beginn an
        self.alter_zustand = ZIELZUSTAENDE.get("schrittmotor") #legt initial den eben gesetzten default-Zustand als alten Zustand an
        self.time = 0.0005 #legt Geschwindigkeit der Signale an Schrittmotor fest
        
        #initialisiert und startet für den Schrittmotor einen eigenen Thread
        self.thread = Thread(target = self.__action) 
        self.thread.start()
        
        
    def __action(self):
        while True:
            self.zielzustand = ZIELZUSTAENDE.get("schrittmotor")
            if self.alter_zustand == self.zielzustand: #wenn der alte gleich dem neuen Zustand ist, dann soll sich der Motor nicht bewegen
                pass
            else:
                if self.zielzustand == "stopp": 
                    self.default()
                if self.zielzustand == "ausfahren":
                    self.vorwaerts()
                if self.zielzustand == "einfahren":
                    self.zurueck()
            sleep(0.00000001)
    
    def default(self):
        gpio.output(self.A, gpio.LOW)
        gpio.output(self.B, gpio.LOW)
        gpio.output(self.C, gpio.LOW)
        gpio.output(self.D, gpio.LOW)
        
    #Kopf ausfahren
    def vorwaerts(self):
        if self.position == 0:
            for i in range(230):
                for j in range(7,-1,-1):
                    gpio.output(self.A, self.table[j][0])
                    gpio.output(self.B, self.table[j][1])
                    gpio.output(self.C, self.table[j][2])
                    gpio.output(self.D, self.table[j][3])
                    sleep(self.time)
                    self.default()
        self.position = 1
        ZIELZUSTAENDE['schrittmotor'] = ('stopp')
        
    #Kopf einfahren
    def zurueck(self):
        print("einfahren")
        i=0
        while(True):
            if gpio.input(self.taster) == False:
                if i < 8:
                    gpio.output(self.A, self.table[i][0])
                    gpio.output(self.B, self.table[i][1])
                    gpio.output(self.C, self.table[i][2])
                    gpio.output(self.D, self.table[i][3])
                    sleep(self.time)
                    self.default()
                    i+=1
                    if i >= 8:
                        i = 0
            else:
                break
        self.position = 0
        ZIELZUSTAENDE['schrittmotor'] = ('stopp')