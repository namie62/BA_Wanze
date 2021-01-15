from __future__ import division
import time
import Adafruit_PCA9685
import Konstanten
from threading import Thread
import Zielzustand
from threading import Lock


class Servo_Adafruit():
    def __init__(self, servoname, motorsteuerung):
        self.servo_lock = Lock()
        self.action_lock = Lock()
        self.schreiblock = Lock()
        self.servoname = servoname
        self.motorsteuerung = motorsteuerung
        self.channel = Konstanten.MOTOREN_und_LED_CHANNELS.get(servoname)
        self.servoStart = Konstanten.MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(servoname)[0]
        #gpio.setup(servoPIN, gpio.OUT)
        #self.motor = gpio.PWM(servoPIN, Konstanten.SERVO_FREQUENZ)
        self.alter_zustand = self.servoStart
        #self.motor.start(self.alter_zustand) 
        self.servoEnd = Konstanten.MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(servoname)[1]
        #self.set_servo_pulse(self.alter_zustand)
        self.thread = Thread(target = self.action)
        self.thread.start()


    def set_servo_pulse(self, pulse):
        pulse_length = 1000000 # 1,000,000 us per second (mikrosekunden sind gemeint)
        pulse_length /= 50 # 50 Hz
        pulse_length /= 4096 # 12 bits of resolution
        pulse *= 1000
        pulse /= pulse_length
        pulse = round(pulse)
        pulse = int(pulse)
        
        with (self.schreiblock):
            self.motorsteuerung.set_pwm(self.channel, pulse)
            
        
        
    def action(self):
        while True:
            with (self.action_lock):
                gradzahl = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0] 
                if gradzahl == self.alter_zustand:
                    pass
                else:
                    self.bewegung_um_Grad(gradzahl)
                    #self.bewegung_um_Grad_in_Schritten()
                    #self.jip()
                    #self.set_servo_pulse(self.servoStart)
                    #time.sleep(0.5)
                    #self.set_servo_pulse(self.servoEnd)
                self.alter_zustand = gradzahl
            time.sleep(0.2)
            
                
    def bewegung_um_Grad(self, gradzahl):
        pulse = self.berechneDutyCycle_aus_gradzahl(gradzahl)
        self.set_servo_pulse(pulse)
        
        
    def berechneDutyCycle_aus_gradzahl(self, gradzahl):
        min_dc = Konstanten.MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(self.servoname)[0]  # entspricht 0°
        max_dc = Konstanten.MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(self.servoname)[1]  # entspricht maximalenm Winkel
        
        delta_dc = max_dc - min_dc
        dc_pro_grad = delta_dc/180   #hier muss evlt noch eine Variable eingefügt werden, da helmservo nur 145 Grad kann. Wäre aber auch möglich, dass das egal ist, weil die GEadbewegung bei dem nciht so genau sein muss.
        dc = (dc_pro_grad * gradzahl) + min_dc
        return dc
        
        
    def berechne_schritthoehe(self, groeßere, kleinere):
        differenz = groeßere - kleinere
        schrittanzahl = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]
        self.schritthoehe = differenz/schrittanzahl
        
        
        
    def bewegung_um_Grad_in_Schritten(self):
        neuer_zustand = self.berechneDutyCycle_aus_gradzahl(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0])
        with (self.servo_lock ):
            if self.alter_zustand < neuer_zustand :
                print(self.alter_zustand, neuer_zustand)
                self.berechne_schritthoehe(neuer_zustand,self.alter_zustand)
                stufe = self.alter_zustand 
                for i in range(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]):
               # while stufe <= self.berechneDutyCycle_aus_gradzahl(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0]):
                    print("schritthoehe", self.schritthoehe, "dc", stufe , "schritte", Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1], "anfang und ende:", self.alter_zustand, "Gradzahl", Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0])
                    stufe += self.schritthoehe
                    self.set_servo_pulse(stufe)
                    time.sleep(0.5)
            else:
                self.berechne_schritthoehe(self.alter_zustand,Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0])
                stufe = self.berechneDutyCycle_aus_gradzahl(self.alter_zustand) - self.schritthoehe
                for i in range(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]):
                #while stufe >= self.berechneDutyCycle_aus_gradzahl(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0]):
                    print("stufe", stufe)
                    self.set_servo_pulse(stufe)
                    print("schritthoehe", self.schritthoehe, "dc", stufe , "schritte", Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1], "anfang und ende", self.alter_zustand, Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0])
                    stufe -= self.schritthoehe
    

    
    def stop(self):
        self.set_servo_pulse(0)
        #self.pwm.set_pwm_freq(0)
        



