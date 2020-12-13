#-*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time

# Getter und Setter rausnehmen 
# Instanzmethode bauen, die servos von außerhalb der Klasse steuert: setWinkel oder so nennen, Wert zwischen 0 und 180 geben und dutycycle umrechnen in Grad

# Jeder Servo eigenen Thread  

class Servo():   # Zeile 7, 8, 10, usw rausnehmen was nicht servo spezifisch ist 
    def __init__(self):
        gpio.setwarnings(False) #Wenn Warnungen an kommt ständig die Meldung, dass die Channels schon verwendet werden -> False
        servoPIN = 22 
        # !!!!Achtung!!!! GPIO Mode kann entweder BOARD oder BCM sein. BCM heißt, dass die GPIO Nummern gleich den GPIO Bezeichnungen sind, BOARD heißt, dass die GPIO am Raspberry PI selbst abgezählt sind
        gpio.setmode(gpio.BOARD)
        gpio.setup(servoPIN, gpio.OUT)
        frequenz = 50
        self.servo1 = gpio.PWM(servoPIN, frequenz)
        self.servo1.start(0)

    def start(self): # In Start eigenen Thread self.thread und in Init initalisieren und in start starten
        # Der Thread hat endlosschleife, die einmal pro x ms schaut wo sie ist (Winkel) und was der Winkel ist, wo er hin soll (kommt von außen)
        # dann schauen was man tun muss, um sich da hin zu bewegen, wo er hinwill
        # Jeder servo kriegt eigenen Thread, Hauptthread darf kein time.sleep haben, nur unterthread
        # evtl Steuerungsabfrage später auch in eigenen Thread packen
        # evtl neben Ziel auch GEschwindigkeit (Schritte übergeben)
        
        # Servo kriegt als Parameter eine Winkelgeschwindigkeit in Grad/S, die ist aktuell fix 
        
        
        # val ist Wert von Joystick, zwischen 0 und 1
        # 1 entspricht 12.5 und 0 enstpricht 2.5 ->
        self.servo1.ChangeDutyCycle(2.5) # entspricht 0°
        time.sleep(0.5) # Als Kehrwert von Update Frequenz
        self.servo1.ChangeDutyCycle(12.5) # aus Update Frequenz und Winkel berechnen
        #time.sleep(0.5)
#         p.ChangeDutyCycle(7.5) # entspricht 90°
#         time.sleep(0.5)

    def jip(self):
        self.servo1.ChangeDutyCycle(2.5) # entspricht 0°
        
        
        time.sleep(0.2) 
        self.servo1.ChangeDutyCycle(3) # entspricht 180°
        time.sleep(0.2)
        self.servo1.ChangeDutyCycle(3.5) # entspricht 180°
        time.sleep(0.2) 
        self.servo1.ChangeDutyCycle(4) # entspricht 180°
        time.sleep(0.2)
        self.servo1.ChangeDutyCycle(4.5) # entspricht 180°
        time.sleep(0.2) 
        self.servo1.ChangeDutyCycle(5) # entspricht 180°
        time.sleep(0.2)
        self.servo1.ChangeDutyCycle(5.5) # entspricht 180°
        time.sleep(0.2) 
        self.servo1.ChangeDutyCycle(6) # entspricht 180°
        time.sleep(0.2)
        self.servo1.ChangeDutyCycle(6.5) # entspricht 180°
        time.sleep(0.2)
        self.servo1.ChangeDutyCycle(7) # entspricht 180°
        time.sleep(0.2) 
        self.servo1.ChangeDutyCycle(7.5) # entspricht 180°
        time.sleep(0.2)
        self.servo1.ChangeDutyCycle(8) # entspricht 180°
        time.sleep(0.2) 
        self.servo1.ChangeDutyCycle(8.5) # entspricht 180°
        time.sleep(0.2)
        self.servo1.ChangeDutyCycle(9) # entspricht 180°
        time.sleep(0.2) 
        self.servo1.ChangeDutyCycle(9.5) # entspricht 180°
        time.sleep(0.2)
        self.servo1.ChangeDutyCycle(10) # entspricht 180°
        time.sleep(0.2) 
        self.servo1.ChangeDutyCycle(10.5) # entspricht 180°
        time.sleep(0.2)
        self.servo1.ChangeDutyCycle(11) # entspricht 180°
        time.sleep(0.2) 
        self.servo1.ChangeDutyCycle(11.5) # entspricht 180°
        time.sleep(0.2)
        self.servo1.ChangeDutyCycle(12) # entspricht 180°
        time.sleep(0.2) 
        self.servo1.ChangeDutyCycle(12.5) # entspricht 180°
        
    def stop(self):
        self.servo1.ChangeDutyCycle(0)