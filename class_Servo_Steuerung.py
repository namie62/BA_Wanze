from __future__ import division
import time
import Adafruit_PCA9685
import Konstanten
from threading import Thread
import Zielzustand
from threading import Lock


class Servo_Adafruit():
    def __init__(self, servoname, motorsteuerung):
        self.servoname = servoname # Jeder Motor holt sich seinen eigenen Namen -> er überprüft jeweils später nur seinen eigenen Zustand
        self.motorsteuerung = motorsteuerung # Motorsteuerungsobjekt des Motopis
        self.channel = Konstanten.MOTOREN_und_LED_CHANNELS.get(servoname) # Jeder Motor holt sich über seinen Namen seinen Channel, an welchem er am Motopi angeschlossen ist
        self.minimaler_servo_winkel = Konstanten.MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(servoname)[0] # holt sich den default 0° Winkel
        self.maximaler_servo_winkel = Konstanten.MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(servoname)[1] # holt sich maximalen Winkel
        self.alter_zustand = self.minimaler_servo_winkel #setzt den alten Zustand auf den default 0° Winkel
        self.thread = Thread(target = self.action) # initialisiert und startet für jeden Servo einen eigenen Thread
        self.thread.start() 

# errechnet den an die Motorsteuerung zu übergebenden Wert für den Puls über den DC und auf die Auflösung umgerechnet
    def set_servo_pulse(self, pulse):
        pulse_length = 1000000 # 1,000,000 us per second (mikrosekunden sind gemeint)
        pulse_length /= 50 # 50 Hz
        pulse_length /= 4096 # 12 bits of resolution
        pulse /= pulse_length 
        pulse = round(pulse)
        pulse = int(pulse)
        self.motorsteuerung.set_pwm(self.channel, pulse) # Hier wird das Signal an den Motopi gesendet

# Thread Methode, die jeder Servo ausführt
    def action(self):
        while True:
                neuer_zustand = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0] # ermittelt den neuen Zustand
                if neuer_zustand == self.alter_zustand: # nur wenn der neue und der alte Zustand nicht gleich sind, wird Veränderung eingeleitet
                    pass
                else:
                    if Zielzustand.ZIELZUSTAENDE.get(self.servoname)[2]== 0: #es gibt 0 1 und 2. Bei 0 ist der Joystick nicht verwendet, bei 1 ist er nach oben geschoben, bei 2 nach unten
                        #self.bewegung_um_Grad(neuer_zustand)
                        self.bewegung_nach_gradzahl_in_schritten()
                        #self.teile_gradzahlen_in_schritte_ein()  #funktioniert aber es gibt noch keine Methode, die nach diesen schrittenbewegt
                        self.alter_zustand = neuer_zustand
                    else:
                        print("jetzt mache ich die Joystickbewegung")
                        # hier muss vom alten entweder nach oben oder unten gefahren werden. Hängt damit also vom alten zustand ab
                time.sleep(0.2)
            
            
            
    def teile_gradzahlen_in_schritte_ein(self):
        # damit nicht versehentlich falsche Gradzahlen übergeben werden können, wird ein maxwinkel und minwinkel gesetzt statt den Grad-Angaben. dazwischen gibts dann x schritte  (ungerade)
        schrittanzahl = Konstanten.STUFENANZAHL_ZWISCHEN_MIN_U_MAX_WINKEL_DER_MOTOREN
        schritthoehe = (self.maximaler_servo_winkel - self.minimaler_servo_winkel)/schrittanzahl
        dc = (Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0]*schritthoehe)+self.minimaler_servo_winkel
        print(dc)

        
       
    
# Wird wenn immer Bewegung um Grad in Schritten aufgerufen wird eigentlich nicht benötigt        
#     def bewegung_um_Grad(self, gradzahl):
#         pulse = self.berechne_dutycycle_aus_gradzahl(gradzahl) # möglicherweise nicht in Grad übergeben, sondern stattdessen für delta Winkel exakte Schrittanzahl festlegen mit 0 = default 0° und 10 dem maximalen Winkel
#         self.set_servo_pulse(pulse)
#         
        
    def berechne_dutycycle_aus_gradzahl(self, gradzahl):
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
        

    def bewegung_nach_gradzahl_in_schritten(self):
        neuer_zustand = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0] # ermittelt den neuen Zustand
        if self.alter_zustand < neuer_zustand:
            self.berechne_schritthoehe(neuer_zustand,self.alter_zustand)
            ausgangs_gradzahl = self.alter_zustand 
            for schrittanzahl in range(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]):
                ausgangs_gradzahl += self.schritthoehe
                dc = self.berechne_dutycycle_aus_gradzahl(ausgangs_gradzahl)
                self.set_servo_pulse(dc)
                time.sleep(0.01)
        else:
            self.berechne_schritthoehe(self.alter_zustand, neuer_zustand)
            ausgangs_gradzahl = self.alter_zustand 
            for schrittanzahl in range(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]): 
                ausgangs_gradzahl -= self.schritthoehe
                dc = self.berechne_dutycycle_aus_gradzahl(ausgangs_gradzahl)
                self.set_servo_pulse(dc)
                time.sleep(0.01)
                
  
        
        
        
#     def stop(self):
#         self.set_servo_pulse(0) 