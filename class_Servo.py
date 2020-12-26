#-*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time
import Zielzustand
import Konstanten
from threading import Thread

class Servo():   
    def __init__(self, servoname):
        self.servoname = servoname
        servoPIN = Konstanten.MOTOREN_UND_LED_CHANNELS.get(servoname)
        print(servoPIN)
        gpio.setup(servoPIN, gpio.OUT)
        self.motor = gpio.PWM(servoPIN, Konstanten.SERVO_FREQUENZ)
        self.alter_zustand = 0
        self.motor.start(self.alter_zustand)
        self.thread = Thread(target = self.action)
        self.thread.start()


    def action(self):
        while True:
            if Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0] == self.alter_zustand:
                pass
            else:
                #self.bewegung_um_Grad()
                #self.bewegung_um_Grad_in_Schritten()
                self.jip()
            self.alter_zustand = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0]
            time.sleep(0.1)
          
            
    def bewegung_um_Grad(self):
        gradzahl = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0]
        dc = self.berechneDutyCycle_aus_gradzahl(gradzahl)
        self.motor.ChangeDutyCycle(dc)
        
        
    def berechneDutyCycle_aus_gradzahl(self, gradzahl):
        min_dc = Konstanten.MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(self.servoname)[0]  # entspricht 0°
        max_dc = Konstanten.MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(self.servoname)[1]  # entspricht 180°
    
        delta_dc = max_dc - min_dc
        dc_pro_grad = delta_dc/180
        dc = (dc_pro_grad * gradzahl) + min_dc
        return dc
        
        
    def berechne_schritthoehe(self, groeßere, kleinere):
        dc_groeßere = self.berechneDutyCycle_aus_gradzahl(groeßere)
        dc_kleinere = self.berechneDutyCycle_aus_gradzahl(kleinere)
        differenz = dc_groeßere - dc_kleinere
        self.schritthoehe = differenz/Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]
        
        
        
    def bewegung_um_Grad_in_Schritten(self):
        if self.alter_zustand < Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0]:
            self.berechne_schritthoehe(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0],self.alter_zustand)
            stufe = self.berechneDutyCycle_aus_gradzahl(self.alter_zustand) + self.schritthoehe
            for i in range(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]):
           # while stufe <= self.berechneDutyCycle_aus_gradzahl(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0]):
                self.motor.ChangeDutyCycle(stufe)
                print("schritthoehe", self.schritthoehe, "dc", stufe , "schritte", Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1], "anfang und ende", self.alter_zustand, Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0])
                stufe += self.schritthoehe
                time.sleep(0.5)
        else:
            self.berechne_schritthoehe(self.alter_zustand,Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0])
            stufe = self.berechneDutyCycle_aus_gradzahl(self.alter_zustand) - self.schritthoehe
            for i in range(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]):
            #while stufe >= self.berechneDutyCycle_aus_gradzahl(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0]):
                self.motor.ChangeDutyCycle(stufe)
                print("schritthoehe", self.schritthoehe, "dc", stufe , "schritte", Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1], "anfang und ende", self.alter_zustand, Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0])
                stufe -= self.schritthoehe
                time.sleep(0.5)

            

        
        
        # In Start eigenen Thread self.thread und in Init initalisieren und in start starten
        # Der Thread hat endlosschleife, die einmal pro x ms schaut wo sie ist (Winkel) und was der Winkel ist, wo er hin soll (kommt von außen)
        # dann schauen was man tun muss, um sich da hin zu bewegen, wo er hinwill
        # Jeder servo kriegt eigenen Thread, Hauptthread darf kein time.sleep haben, nur unterthread
        # evtl Steuerungsabfrage später auch in eigenen Thread packen
        # evtl neben Ziel auch GEschwindigkeit (Schritte übergeben)
        
        # Servo kriegt als Parameter eine Winkelgeschwindigkeit in Grad/S, die ist aktuell fix 
        
        
        # val ist Wert von Joystick, zwischen 0 und 1
        # 1 entspricht 12.5 und 0 enstpricht 2.5 ->
         # entspricht 0°
        #time.sleep(0.5) # Als Kehrwert von Update Frequenz
        #self.motor.ChangeDutyCycle(12.5) # aus Update Frequenz und Winkel berechnen
        #time.sleep(0.5)
#         p.ChangeDutyCycle(7.5) # entspricht 90°
#         time.sleep(0.5)
                  

    def jip(self):
        self.motor.ChangeDutyCycle(2.5) # entspricht 0°
        time.sleep(0.2) 
        self.motor.ChangeDutyCycle(3) # entspricht 180°
        time.sleep(0.2)
        self.motor.ChangeDutyCycle(3.5) # entspricht 180°
        time.sleep(0.2) 
        self.motor.ChangeDutyCycle(4) # entspricht 180°
        time.sleep(0.2)
        self.motor.ChangeDutyCycle(4.5) # entspricht 180°
        time.sleep(0.2) 
        self.motor.ChangeDutyCycle(5) # entspricht 180°
        time.sleep(0.2)
        self.motor.ChangeDutyCycle(5.5) # entspricht 180°
        time.sleep(0.2) 
        self.motor.ChangeDutyCycle(6) # entspricht 180°
        time.sleep(0.2)
        self.motor.ChangeDutyCycle(6.5) # entspricht 180°
        time.sleep(0.2)
        self.motor.ChangeDutyCycle(7) # entspricht 180°
        time.sleep(0.2) 
        self.motor.ChangeDutyCycle(7.5) # entspricht 180°
        time.sleep(0.2)
        self.motor.ChangeDutyCycle(8) # entspricht 180°
        time.sleep(0.2) 
        self.motor.ChangeDutyCycle(8.5) # entspricht 180°
        time.sleep(0.2)
        self.motor.ChangeDutyCycle(9) # entspricht 180°
        time.sleep(0.2) 
        self.motor.ChangeDutyCycle(9.5) # entspricht 180°
        time.sleep(0.2)
        self.motor.ChangeDutyCycle(10) # entspricht 180°
        time.sleep(0.2) 
        self.motor.ChangeDutyCycle(10.5) # entspricht 180°
        time.sleep(0.2)
        self.motor.ChangeDutyCycle(11) # entspricht 180°
        time.sleep(0.2) 
        self.motor.ChangeDutyCycle(11.5) # entspricht 180°
        time.sleep(0.2)
        self.motor.ChangeDutyCycle(12) # entspricht 180°
        time.sleep(0.2) 
        self.motor.ChangeDutyCycle(12.5) # entspricht 180°
        
    def stop(self):
        self.motor.ChangeDutyCycle(0)