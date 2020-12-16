#-*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time
import Zielzustand
import Konstanten
from threading import Thread


class Servo():   
    def __init__(self, servoname):
        self.servoname = servoname
        servoPIN = Konstanten.MOTOREN_und_PINS.get(servoname)
        gpio.setup(servoPIN, gpio.OUT)
        self.motor = gpio.PWM(servoPIN, Konstanten.SERVO_FREQUENZ)
        self.alter_zustand = 0
        self.motor.start(self.alter_zustand)
        self.thread = Thread(target = self.action)
        self.thread.start()

    def action(self):
        while True:
            #print("hi", Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0])
            self.neuer_zustand = Zielzustand.ZIELZUSTAENDE.get(self.servoname)
            #self.schritte = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]
            if self.neuer_zustand == self.alter_zustand:
                pass
            else:
                self.bewegung_um_Grad_in_Schritten()
            self.alter_zustand = self.neuer_zustand
            time.sleep(0.1)
          
    def bewegung_um_Grad_in_Schritten(self):
        self.gradzahl = Zielzustand.ZIELZUSTAENDE.get(self.servoname)
        dc = self.berechneDutyCycle_aus_gradzahl()
        self.motor.ChangeDutyCycle(dc)
        print(dc)
            
        
    def berechneDutyCycle_aus_gradzahl(self):
        min_dc = Konstanten.MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(self.servoname)  # entspricht 0°
        max_dc = Konstanten.MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(self.servoname)  # entspricht 180°
        delta_dc = max_dc - min_dc
        dc_pro_grad = delta_dc/180
        dc = (dc_pro_grad * self.neuer_zustand) + min_dc
        return dc
         
    
    

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