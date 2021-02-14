#-*- coding: utf-8 -*-
from time import sleep
from datetime import datetime
import RPi.GPIO as gpio
from threading import Thread
from Zielzustand import ZIELZUSTAENDE
from Konstanten import MOTOREN_und_LED_CHANNELS, SCHRITTMOTOR_TABELLE

class Schrittmotor():
    def __init__(self):
        #holt sich die Pin-Nummern und Tabelle aus Konstanten.py
        pin_nummern = MOTOREN_und_LED_CHANNELS.get("schrittmotor")
        self.A = pin_nummern[0] #PIN 21
        self.B = pin_nummern[1] #PIN 22
        self.C = pin_nummern[2] #PIN 23
        self.D = pin_nummern[3] #PIN 24
        self.table = SCHRITTMOTOR_TABELLE
        
        #legt alle Pins als Outputs fest
        for i in range(len(MOTOREN_und_LED_CHANNELS.get("schrittmotor"))):
            gpio.setup(MOTOREN_und_LED_CHANNELS.get("schrittmotor")[i], gpio.OUT)
            
        self.default() #einmal alle auf gpio.LOW setzen zu Beginn, damit der Motor nichts tut von Beginn an
        self.alter_zustand = ZIELZUSTAENDE.get("schrittmotor") #legt initial den eben gesetzten default-Zustand als alten Zustand an
        self.time = 0.0005 #legt Geschwindigkeit der Signale an Schrittmotor fest
        
        #initialisiert und startet für den Schrittmotor einen eigenen Thread
        self.thread = Thread(target = self.__action) 
        self.thread.start()

    def __action(self):
        while gpio.HIGH:
            self.zielzustand = ZIELZUSTAENDE.get("schrittmotor")
            if self.alter_zustand == self.zielzustand: #wenn der alte gleich dem neuen Zustand ist, dann soll sich der Motor nicht bewegen
                self.default()
            else:
                if self.zielzustand == "stopp": 
                    self.default()
                if self.zielzustand == "ausfahren":
                    self.vorwaerts()
                if self.zielzustand == "einfahren":
                    self.zurueck()
            self.alter_zustand == self.zielzustand #der neue Zustand wird zum alten
         
    def default(self):
        gpio.output(self.A, gpio.LOW)
        gpio.output(self.B, gpio.LOW)
        gpio.output(self.C, gpio.LOW)
        gpio.output(self.D, gpio.LOW)
        
    #Kopf ausfahren
    def vorwaerts(self):
        readfile = open('position.txt', 'r')
        position = int(readfile.read())
        readfile.close()
        while position < 2600:
            for j in range(7,-1,-1):
                gpio.output(self.A, self.table[j][0])
                gpio.output(self.B, self.table[j][1])
                gpio.output(self.C, self.table[j][2])
                gpio.output(self.D, self.table[j][3])
                sleep(self.time)
                position += 1
                gpio.output(self.A, gpio.LOW)
                gpio.output(self.B, gpio.LOW)
                gpio.output(self.C, gpio.LOW)
                gpio.output(self.D, gpio.LOW)
                if(position >=2600):
                    break
        writefile = open('position.txt', 'w')
        writefile.write(str(position))
        writefile.close()        

    #Kopf einfahren
    def zurueck(self):
        readfile = open('position.txt', 'r')
        position = int(readfile.read())
        readfile.close()
        while position >=0:
            for j in range(8):
                gpio.output(self.A, self.table[j][0])
                gpio.output(self.B, self.table[j][1])
                gpio.output(self.C, self.table[j][2])
                gpio.output(self.D, self.table[j][3])
                sleep(self.time)
                position -= 1
                gpio.output(self.A, gpio.LOW)
                gpio.output(self.B, gpio.LOW)
                gpio.output(self.C, gpio.LOW)
                gpio.output(self.D, gpio.LOW)
                if position<0:
                    break
        writefile = open('position.txt', 'w')
        writefile.write(str(position))
        writefile.close()