from __future__ import division
import time
import Adafruit_PCA9685
import Konstanten
from threading import Thread
import Zielzustand
from threading import Lock


class Servo_Adafruit():
    def __init__(self, servoname, motorsteuerung):
        self.servoname = servoname
        self.motorsteuerung = motorsteuerung # Motorsteuerungsobjekt des Motopis
        self.channel = Konstanten.MOTOREN_und_LED_CHANNELS.get(servoname) # Jeder Motor holt sich über seinen Namen seinen Channel, an welchem er am Motopi angeschlossen ist
        
        self.ermittle_extremwinkel_und_setze_default_Werte() #ermittelt, welcher DC-Wert für den minimalen Winkel/Prozentzahl steht und welcher für Max (hängt von Einbaurichtung (wg. Drehrichtung) des Motors ab)
        
        self.alter_zustand = self.default_dc_nullposition #setzt den alten Zustand auf den default 0° Winkel
        
        self.thread = Thread(target = self.action) # initialisiert und startet für jeden Servo einen eigenen Thread
        self.thread.start() 


    def ermittle_extremwinkel_und_setze_default_Werte(self):       
        #Welcher Winkel max und welcher min ist, hängt von Einbaurichtung des Motors ab. Reihenfolge im Dic in Konstanten dabei zu beachten: 0 ist 0%/0° und 1 ist 100%/180°
        self.default_dc_nullposition = Konstanten.MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(self.servoname)[0] # enstspricht defaul_winkel für 0% / 0° 
        self.default_dc_maxposition = Konstanten.MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL.get(self.servoname)[1] # enstspricht defaul_winkel für 100% / 180°
        # holt sich beide Winkel und vergleicht diese
        if self.default_dc_nullposition < self.default_dc_maxposition:
            self.dc_fuer_min_winkel_oder_prozent = self.default_dc_nullposition
            self.dc_fuer_max_winkel_oder_prozent = self.default_dc_maxposition
        else:
            self.dc_fuer_min_winkel_oder_prozent = self.default_dc_maxposition
            self.dc_fuer_max_winkel_oder_prozent = self.default_dc_nullposition


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
        if Konstanten.SERVO_MODUS == "grad":    #das heißt, dass für die Zustände in der Main Gradzahlen eingesetzt werden müssen (alter und und neuer_Zustand sind dann Gradzahlen)
            # war der anfängliche Modus
            #GEFAHR:  nicht alle Servos dürfen im eingebauten Zustand um 180° drehen, da sonst etwas kaputt gehen kann, daher Prozentmodus besser
            while True:
                    self.neuer_zustand = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0] # ermittelt den neuen Zustand
                    if self.neuer_zustand == self.alter_zustand: # nur wenn der neue und der alte Zustand nicht gleich sind, wird Veränderung eingeleitet
                        pass
                    else:
                        self.joystick_bewegungsrichtung = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[2]
                        if self.joystick_bewegungsrichtung == 0: #es gibt 0 1 und 2. Bei 0 ist der Joystick nicht verwendet, bei 1 ist er nach oben geschoben, bei 2 nach unten
                            #self.bewegung_um_Grad(neuer_zustand)
                            self.bewegung_nach_gradzahl_in_schritten()
                            self.alter_zustand = self.neuer_zustand
                        else:
                            #self.joystick_bewegung()
                            print("joystickbewegung")
                            # hier shcauen, ob alter zustand überschrieben werden muss
                    time.sleep(0.2)
        else:
            # Jetzt sind alter und neuer Zustand Prozentwerte zwischen den maximal zulässigen Winkeln -> keine Überdrehungsgefahr der Motoren
            self.alter_zustand = self.berechne_prozentzahl_von(self.alter_zustand) # Da sonst Dc mit Prozent verglichen wird
            while True:
                self.neuer_zustand = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0] # ermittelt den neuen Zustand jetzt in Prozent
                if self.neuer_zustand == self.alter_zustand: # nur wenn der neue und der alte Zustand nicht gleich sind, wird Veränderung eingeleitet
                    pass
                else:
                    self.joystick_bewegungsrichtung = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[2]
                    if self.joystick_bewegungsrichtung == 0: #es gibt 0 1 und 2. Bei 0 ist der Joystick nicht verwendet, bei 1 ist er nach oben geschoben, bei 2 nach unten
                        self.bewegung_nach_prozentzahl_in_schritten()
                        self.alter_zustand = self.neuer_zustand
                    else:
                        #self.joystick_bewegung()
                        print("joystickbewegung")
                        # hier shcauen, ob alter zustand überschrieben werden muss
                time.sleep(0.2)
                
            
    def berechne_dc_fuer_1_prozent(self):
        # damit nicht versehentlich falsche Gradzahlen übergeben werden können, wird ein maxwinkel und minwinkel gesetzt statt den Grad-Angaben. Angabe der Zwischenschritte dann in Prozent zum maximalen Winkel
        schrittanzahl = Konstanten.STUFENANZAHL_ZWISCHEN_MIN_U_MAX_WINKEL_DER_MOTOREN   # 100, weil 100% 
        dc_von_1_prozent = (self.dc_fuer_max_winkel_oder_prozent - self.dc_fuer_min_winkel_oder_prozent)/schrittanzahl   
        return dc_von_1_prozent# entspricht DC bei 1%
            
            
#     def joystick_bewegung(self):
#         dc_von_1_prozent = self.berechne_dc_fuer_1_prozent()
#         
#         dc_von_alter_zustand = self.berechne_dc_aus_prozentzahl(self.alter_zustand)
# 
#         if self.joystick_bewegungsrichtung == 1: #das heißt er ist nach oben gedrückt
#             naechster_schritt = dc_von_alter_zustand + dc_von_1_prozent
#             if naechster_schritt < 100:
#                 dc = naechster_schritt
#                 dc_von_alter_zustand = naechster_schritt
#                 self.alter_zustand += 1
#                 self.set_servo_pulse(dc)
#             else:
#                 dc = self.default_dc_maxposition
#                 self.set_servo_pulse(dc)
#         else:
#             naechster_schritt = dc_von_alter_zustand - dc_von_1_prozent
#             if naechster_schritt > 0 :
#                 dc = naechster_schritt
#                 dc_von_alter_zustand = naechster_schritt #- schritthoehe
#                 self.alter_zustand -= 1
#                 self.set_servo_pulse(dc)
#             else:
#                 dc = self.default_dc_nullposition
#                 self.set_servo_pulse(dc)
#         
        
    
    def berechne_dc_aus_prozentzahl(self, wert):
        delta_dc = self.default_dc_maxposition - self.default_dc_nullposition
        dc_pro_grad = delta_dc/Konstanten.STUFENANZAHL_ZWISCHEN_MIN_U_MAX_WINKEL_DER_MOTOREN   #hier muss evlt noch eine Variable eingefügt werden, da helmservo nur 145 Grad kann. Wäre aber auch möglich, dass das egal ist, weil die GEadbewegung bei dem nciht so genau sein muss.
        dc = (dc_pro_grad * wert) + self.default_dc_nullposition
        return dc
    
    
    def berechne_prozentzahl_von(self, wert):
        dc_fuer_1_prozent = self.berechne_dc_fuer_1_prozent()
        wert = wert - self.dc_fuer_min_winkel_oder_prozent
        wert = wert / dc_fuer_1_prozent
        return wert
        
    def bewegung_nach_prozentzahl_in_schritten(self):
        print("prozentzahl", self.neuer_zustand)
        if self.alter_zustand < self.neuer_zustand:
            self.berechne_schritthoehe(self.neuer_zustand,self.alter_zustand)
            ausgangs_position = self.alter_zustand
            for schrittanzahl in range(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]):
                 ausgangs_position += self.schritthoehe
                 dc = self.berechne_dc_aus_prozentzahl(ausgangs_position)
                 print("dc", dc)
                 self.set_servo_pulse(dc)
                 time.sleep(0.01)
        else:
            self.berechne_schritthoehe(self.alter_zustand, self.neuer_zustand)
            ausgangs_position = self.alter_zustand 
            for schrittanzahl in range(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]): 
                ausgangs_position -= self.schritthoehe
                dc = self.berechne_dc_aus_prozentzahl(ausgangs_position)
                print("dc", dc)
                self.set_servo_pulse(dc)
                time.sleep(0.01)
        
        
        
    def berechne_dc_aus_gradzahl(self, wert):
        delta_dc = self.default_dc_maxposition - self.default_dc_nullposition
        dc_pro_grad = delta_dc/Konstanten.GRADZAHL_ZWISCHEN_MIN_U_MAX_WINKEL_DER_MOTOREN  #hier muss evlt noch eine Variable eingefügt werden, da helmservo nur 145 Grad kann. Wäre aber auch möglich, dass das egal ist, weil die GEadbewegung bei dem nciht so genau sein muss.
        dc = (dc_pro_grad * wert) + self.default_dc_nullposition
        return dc
        
        
    def berechne_schritthoehe(self, groeßere, kleinere):
        differenz = groeßere - kleinere
        schrittanzahl = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]
        self.schritthoehe = differenz/schrittanzahl
        print("schritthoehe", self.schritthoehe)
        

    def bewegung_nach_gradzahl_in_schritten(self):
        if self.alter_zustand < self.neuer_zustand:
            self.berechne_schritthoehe(self.neuer_zustand,self.alter_zustand)
            ausgangs_position = self.alter_zustand 
            for schrittanzahl in range(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]):
                ausgangs_position += self.schritthoehe
                dc = self.berechne_dc_aus_gradzahl(ausgangs_position)
                self.set_servo_pulse(dc)
                time.sleep(0.01)
        else:
            self.berechne_schritthoehe(self.alter_zustand, self.neuer_zustand)
            ausgangs_position = self.alter_zustand 
            for schrittanzahl in range(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]): 
                ausgangs_position -= self.schritthoehe
                dc = self.berechne_dc_aus_gradzahl(ausgangs_position)
                self.set_servo_pulse(dc)
                time.sleep(0.01)


# Wird wenn immer Bewegung um Grad in Schritten aufgerufen wird eigentlich nicht benötigt        
#     def bewegung_um_Grad(self, gradzahl):
#         pulse = self.berechne_dc_aus_gradzahl(gradzahl) # möglicherweise nicht in Grad übergeben, sondern stattdessen für delta Winkel exakte Schrittanzahl festlegen mit 0 = default 0° und 10 dem maximalen Winkel
#         self.set_servo_pulse(pulse)   
        
#     def stop(self):
#         self.set_servo_pulse(0) 