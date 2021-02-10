from time import sleep
from datetime import datetime
import RPi.GPIO as gpio
from threading import Thread
import Zielzustand
import Konstanten

class Schrittmotor():
    def __init__(self):
        pin_nummern = Konstanten.MOTOREN_und_LED_CHANNELS.get("schrittmotor")
        self.time = 0.0005
        self.A = pin_nummern[0] #PIN 21
        self.B = pin_nummern[1] #PIN 22
        self.C = pin_nummern[2] #PIN 23
        self.D = pin_nummern[3] #PIN 24
        
        self.table = Konstanten.SCHRITTMOTOR_TABELLE
        for i in range(len(Konstanten.MOTOREN_und_LED_CHANNELS.get("schrittmotor"))):
            gpio.setup(Konstanten.MOTOREN_und_LED_CHANNELS.get("schrittmotor")[i], gpio.OUT)
            gpio.output(Konstanten.MOTOREN_und_LED_CHANNELS.get("schrittmotor")[i], gpio.LOW)
        self.default() # einmal alle auf gpio.LOW setzen zu Beginn, damit der Motor nichts tut von Beginn an
        self.alter_zustand = Zielzustand.ZIELZUSTAENDE.get("schrittmotor")
        self.thread = Thread(target = self.action) # initialisiert und startet für den Schrittmotor einen eigenen Thread
        self.thread.start()
        
        

# table = [[gpio.HIGH,gpio.LOW,gpio.LOW,gpio.LOW],
#          [gpio.HIGH,gpio.HIGH,gpio.LOW,gpio.LOW],
#          [gpio.LOW,gpio.HIGH,gpio.LOW,gpio.LOW],
#          [gpio.LOW,gpio.HIGH,gpio.HIGH,gpio.LOW],
#          [gpio.LOW,gpio.LOW,gpio.HIGH,gpio.LOW],
#          [gpio.LOW,gpio.LOW,gpio.HIGH,gpio.HIGH],
#          [gpio.LOW,gpio.LOW,gpio.LOW,gpio.HIGH],
#          [gpio.HIGH,gpio.LOW,gpio.LOW,gpio.HIGH]]
       
# Pins aus Ausgänge definieren


    def action(self):
        while gpio.HIGH:
            self.zielzustand = Zielzustand.ZIELZUSTAENDE.get("schrittmotor")
            if self.alter_zustand == self.zielzustand:
                self.default()
              #  pass
            else:
                if self.zielzustand == "stopp":
                    self.default()
                if self.zielzustand == "ausfahren":
                    self.vorwaerts()
                if self.zielzustand == "einfahren":
                    self.zurueck()
            self.alter_zustand == self.zielzustand
         
    def default(self):
        gpio.output(self.A, gpio.LOW)
        gpio.output(self.B, gpio.LOW)
        gpio.output(self.C, gpio.LOW)
        gpio.output(self.D, gpio.LOW)
        
    #Kopf ausfahren
    def vorwaerts(self):
        #print("ausfahren")
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
        #print("einfahren")
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



    #gpio.cleanup()

