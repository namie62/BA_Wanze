#-*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time
from threading import Thread
import classZielzustand

# Instanzmethode bauen, die servos von außerhalb der Klasse steuert: setWinkel oder so nennen, Wert zwischen 0 und 180 geben und dutycycle umrechnen in Grad

# Jeder Servo eigenen Thread

gpio.setwarnings(False) #Wenn Warnungen an kommt ständig die Meldung, dass die Channels schon verwendet werden -> False
 # !!!!Achtung!!!! GPIO Mode kann entweder BOARD oder BCM sein. BCM heißt, dass die GPIO Nummern gleich den GPIO Bezeichnungen sind, BOARD heißt, dass die GPIO am Raspberry PI selbst abgezählt sind
gpio.setmode(gpio.BOARD)
FREQUENZ = 50

MOTOREN_und_PINS = {
    "ellbogen_servo1" : 22,
    "ellbogen_servo2" : 0,
    "schulter_servo1" : 0,
    "schulter_servo2": 0,
    "kopf_servo": 0,
    "kopf_linear" : 0,
    "helm_servo" : 0}

MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL = { # Bei Test mit zwei versch. Servos fiel auf, dass sie unterschiedliche DC benötigen, um die vollen 180° anzufahren
    "ellbogen_servo1" : (2.5,12.5), # falls immer die gleichen Servos verwendet werden, dann kann das Dic evtl. aufgelöst werden
    "ellbogen_servo2" : (2.5,12.5),
    "schulter_servo1" : (2.5,12.5),
    "schulter_servo2": (2.5,12.5),
    "kopf_servo": (2.5,12.5),
    "kopf_linear" : (2.5,12.5),
    "helm_servo" : (2.5,12.5)}



class Servo():   
    def __init__(self, servoname):
        self.servoname = servoname
        servoPIN = MOTOREN_und_PINS.get(servoname)
        gpio.setup(servoPIN, gpio.OUT)
        self.motor = gpio.PWM(servoPIN, FREQUENZ)
        self.motor.start(0)
        self.thread = Thread(target = self.erfuelle_zustand)

    def bewegung_um_Grad(self,gradzahl):
        self.gradzahl = gradzahl
        dc = self.berechneDutyCycle_aus_gradzahl(self.gradzahl)
        self.motor.ChangeDutyCycle(dc)
        
        
    def berechneDutyCycle_aus_gradzahl(self, gradzahl):
        min_dc = MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(self.servoname)[0]  # entspricht 0°
        max_dc = MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(self.servoname)[1]  # entspricht 180°
    
        delta_dc = max_dc - min_dc
        dc_pro_grad = delta_dc/180
        dc = (dc_pro_grad * gradzahl) + min_dc
        return dc
        


    def start(self):
        self.thread.start()
        
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

    def erfuelle_zustand(self):
        while True:
            # schaue wo du bist und wo du hin willst
            #print("ich bin servo", zielzustand.Zielzustaende)
            self.bewegung_um_Grad(180)
            
            
            
        




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