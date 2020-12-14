#-*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time
import Zielzustand
import Konstanten
from threading import Thread
# Instanzmethode bauen, die servos von außerhalb der Klasse steuert: setWinkel oder so nennen, Wert zwischen 0 und 180 geben und dutycycle umrechnen in Grad

# Jeder Servo eigenen Thread




# ZIELZUSTAENDE = {
#     "Notaus" : False, # direkt als Attribute: self.Notaus = bla bla
#     "Nacken" : "mittig", #links, rechts
#     "Kopf" : "ausgefahren", # eingefahren 
#     "Led" : "aus", # farben reinschreiben 
#     "Schulter_rechts": "0", # Gradzahlen, 0 ist unten und dann gehts bis 180 weiter hoch
#     "Schulter_links" : "0",
#     "Ellbogen_rechts": "0",
#     "Ellbogen_links": "0",
#     "Helm": "0",
#                               # usw.
#                               }
class Servo():   
    def __init__(self, servoname):
        self.servoname = servoname
        servoPIN = Konstanten.MOTOREN_und_PINS.get(servoname)
        gpio.setup(servoPIN, gpio.OUT)
        self.motor = gpio.PWM(servoPIN, Konstanten.SERVO_FREQUENZ)
        self.motor.start(0)
        self.thread = Thread(target = self.action)
        self.thread.start()


    def action(self):
        while True:
            for i in Zielzustand.ZIELZUSTAENDE:
                if Zielzustand.ZIELZUSTAENDE.get(i) == Zielzustand.ALTER_ZIELZUSTAND.get(i):
                    print(Zielzustand.ZIELZUSTAENDE.get(i),"==", Zielzustand.ALTER_ZIELZUSTAND.get(i))
                   # print("nix verändert")
                else:
                    print("hat sich verändert")
            time.sleep(0.1)
 
                

            
            
    def bewegung_um_Grad(self,gradzahl):
        self.gradzahl = gradzahl
        dc = self.berechneDutyCycle_aus_gradzahl(self.gradzahl)
        self.motor.ChangeDutyCycle(dc)
        
    def berechneDutyCycle_aus_gradzahl(self, gradzahl):
        min_dc = Konstanten.MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(self.servoname)[0]  # entspricht 0°
        max_dc = Konstanten.MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(self.servoname)[1]  # entspricht 180°
    
        delta_dc = max_dc - min_dc
        dc_pro_grad = delta_dc/180
        dc = (dc_pro_grad * gradzahl) + min_dc
        return dc
        

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