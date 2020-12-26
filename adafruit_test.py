from __future__ import division
import time
import Adafruit_PCA9685
import Konstanten
from threading import Thread
import Zielzustand


class Servo_Adafruit():
    def __init__(self, servoname, pwm):
        self.servoname = servoname
        self.pwm = pwm
        self.channel = Konstanten.MOTOREN_und_LED_CHANNELS.get(servoname)
        print("channel", self.channel)
        #gpio.setup(servoPIN, gpio.OUT)
        #self.motor = gpio.PWM(servoPIN, Konstanten.SERVO_FREQUENZ)
        self.alter_zustand = 0.6
        #self.motor.start(self.alter_zustand)
        self.servoStart = 0.6
        self.servo = self.servoStart
        self.servoEnd = 2.4

        self.thread = Thread(target = self.action)
        self.thread.start()



    def set_servo_pulse(self, pulse):
        pulse_length = 1000000 # 1,000,000 us per second (mikrosekunden sind gemeint)
        pulse_length /= 50 # 60 Hz
        pulse_length /= 4096 # 12 bits of resolution
        pulse *= 1000
        pulse /= pulse_length
        pulse = round(pulse)
        pulse = int(pulse)
        print(pulse)
        self.pwm.set_pwm(self.channel, 0, pulse)
        self.pwm.set_pwm_freq(50)
        
        
    def action(self):
        while True:
            if Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0] == self.alter_zustand:
                pass
            else:
                self.bewegung_um_Grad()
                #self.bewegung_um_Grad_in_Schritten()
                #self.jip()
                #self.set_servo_pulse(self.servoStart)
                #time.sleep(0.5)
                #self.set_servo_pulse(self.servoEnd)
            self.alter_zustand = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0]
            time.sleep(0.1)
            
            
            
    def bewegung_um_Grad(self):
        gradzahl = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0]
        pulse = self.berechneDutyCycle_aus_gradzahl(gradzahl)
        self.set_servo_pulse(pulse)
        
        
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

            
##################################################
######### Initialise Start-Up-Positions ##########
##################################################
# for x in range(0, 16):
#     set_servo_pulse(x, servoStart)
#     time.sleep(2)
# ##################################################
# ######### Max-Range for every servo ##############
# ##################################################
# for x in range (0, 16):
#     while (servo < servoEnd):
#         set_servo_pulse(x, servo0)
#         servo = (servo + 0.05)
#         time.sleep(0.04)
#         time.sleep(1)


    def stop(self):
        self.motor.ChangeDutyCycle(0)


