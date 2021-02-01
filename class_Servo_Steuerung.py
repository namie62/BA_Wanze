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
        self.default_dc_nullposition = Konstanten.MOTOREN_MAX_MIN_PULSDAUER.get(self.servoname)[0] # enstspricht defaul_winkel für 0% / 0° 
        self.default_dc_maxposition = Konstanten.MOTOREN_MAX_MIN_PULSDAUER.get(self.servoname)[1] # enstspricht defaul_winkel für 100% / 180°
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
            self.alter_zustand = self.prozentmodus_berechne_prozentzahl_von(self.alter_zustand) # Da sonst Dc mit Prozent verglichen wird
            while True:
                self.neuer_zustand = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[0] # ermittelt den neuen Zustand jetzt in Prozent
                if self.neuer_zustand == self.alter_zustand: # nur wenn der neue und der alte Zustand nicht gleich sind, wird Veränderung eingeleitet
                    pass
                else:
                    self.checke_joystick_toggle_und_löse_bewegung_aus()
                time.sleep(0.001)
                

    def checke_joystick_toggle_und_löse_bewegung_aus(self):
        self.toggle_joystick = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[2] # Mögliche Werte sind Zahlen von 0 bis 4 
        if self.toggle_joystick == 0: # bei 0 wird keiner der beiden Joysticks verwendet, bei 1 ist der Joystick nach oben gedrückt, bei 2 nach unten
            self.prozentmodus_standardbewegung_ermittle_bewegungsrichtung()
            self.alter_zustand = self.neuer_zustand
        else:
            self.prozentmodus_joystick_bewegung()

    def prozentmodus_joystick_bewegung(self):
        if self.toggle_joystick == 1: # das heißt er ist nach oben gedrückt
                self.prozentmodus_joystick_bewege_arm_nach_oben()
        elif self.toggle_joystick == 2: # wenn Joystick nach unten gedrückt wird
                self.prozentmodus_joystick_bewege_arm_nach_unten()
                
    def prozentmodus_joystick_bewege_arm_nach_oben(self):
        neuer_zustand = self.alter_zustand + Konstanten.PROZENT_SCHRITTZAHL_JOYSTICK
        if neuer_zustand <= 100: # nicht weiter als 100 Prozent, sonst Gefahr von Beschädigungen
            self.alter_zustand = neuer_zustand
            dc = self.prozentmodus_berechne_dc_aus_prozentzahl(neuer_zustand)
        else:
            dc = self.default_dc_maxposition # Wenn der neu errechnete Wert über 100 Prozent wäre, dann ist der dc der 100 Prozent Wert
        self.set_servo_pulse(dc)
    
    def prozentmodus_joystick_bewege_arm_nach_unten(self):
        neuer_zustand = self.alter_zustand - Konstanten.PROZENT_SCHRITTZAHL_JOYSTICK
        if neuer_zustand >= 0 :  # nicht weiter als 0 Prozent, sonst Gefahr von Beschädigungen
            self.alter_zustand = neuer_zustand
            dc = self.prozentmodus_berechne_dc_aus_prozentzahl(neuer_zustand)
        else:
            dc = self.default_dc_nullposition  # wenn der neu errechnete Wert unter 0 Prozent wäre, dann ist der dc der 0 Prozent Wert
        self.set_servo_pulse(dc)
    
    def prozentmodus_berechne_dc_fuer_1_prozent(self):
        # damit nicht versehentlich falsche Gradzahlen übergeben werden können, wird ein maxwinkel und minwinkel gesetzt statt den Grad-Angaben. Angabe der Zwischenschritte dann in Prozent zum maximalen Winkel
        schrittanzahl = Konstanten.STUFENANZAHL_ZWISCHEN_MIN_U_MAX_POSITION_DER_MOTOREN  # 100, weil 100% 
        dc_von_1_prozent = (self.dc_fuer_max_winkel_oder_prozent - self.dc_fuer_min_winkel_oder_prozent)/schrittanzahl   
        return dc_von_1_prozent #entspricht DC bei 1%
            
    def prozentmodus_berechne_dc_aus_prozentzahl(self, wert):
        delta_dc = self.default_dc_maxposition - self.default_dc_nullposition
        dc_pro_grad = delta_dc/Konstanten.STUFENANZAHL_ZWISCHEN_MIN_U_MAX_POSITION_DER_MOTOREN   #hier muss evlt noch eine Variable eingefügt werden, da helmservo nur 145 Grad kann. Wäre aber auch möglich, dass das egal ist, weil die GEadbewegung bei dem nciht so genau sein muss.
        dc = (dc_pro_grad * wert) + self.default_dc_nullposition
        return dc
    
    def prozentmodus_berechne_prozentzahl_von(self, wert):
        dc_fuer_1_prozent = self.prozentmodus_berechne_dc_fuer_1_prozent()
        wert = wert - self.dc_fuer_min_winkel_oder_prozent
        wert = wert / dc_fuer_1_prozent
        return wert
    
        
    def prozentmodus_standardbewegung_ermittle_bewegungsrichtung(self):
        if self.alter_zustand < self.neuer_zustand:
            self.prozentmodus_bewegung_nach_oben()
        else:
            self.prozentmodus_bewegung_nach_unten()

        
    def prozentmodus_bewegung_nach_oben(self):
        self.beide_Modi_berechne_schritthoehe(self.neuer_zustand,self.alter_zustand)
        ausgangs_position = self.alter_zustand
        for schrittanzahl in range(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]):
            ausgangs_position += self.schritthoehe
            dc = self.prozentmodus_berechne_dc_aus_prozentzahl(ausgangs_position)
            self.set_servo_pulse(dc)
            #time.sleep(0.01)
            
    def prozentmodus_bewegung_nach_unten(self):
        self.beide_Modi_berechne_schritthoehe(self.alter_zustand, self.neuer_zustand)
        ausgangs_position = self.alter_zustand 
        for schrittanzahl in range(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]): 
            ausgangs_position -= self.schritthoehe
            dc = self.prozentmodus_berechne_dc_aus_prozentzahl(ausgangs_position)
            self.set_servo_pulse(dc)
            #time.sleep(0.01)
                
                
    # Sowohl für Gradmodus als auch für Prozentmodus gleich      
    def beide_Modi_berechne_schritthoehe(self, groeßere, kleinere):
        differenz = groeßere - kleinere
        schrittanzahl = Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]
        self.schritthoehe = differenz/schrittanzahl
# 
#     def gradmodus_berechne_dc_aus_gradzahl(self, wert):
#         delta_dc = self.default_dc_maxposition - self.default_dc_nullposition
#         dc_pro_grad = delta_dc/Konstanten.GRADZAHL_ZWISCHEN_MIN_U_MAX_WINKEL_DER_MOTOREN  #hier muss evlt noch eine Variable eingefügt werden, da helmservo nur 145 Grad kann. Wäre aber auch möglich, dass das egal ist, weil die GEadbewegung bei dem nciht so genau sein muss.
#         dc = (dc_pro_grad * wert) + self.default_dc_nullposition
#         return dc
# 
#     # Nur benötigt bei Gradmodus
#     def gradmodus_bewegung_nach_gradzahl_in_schritten(self):
#         if self.alter_zustand < self.neuer_zustand:
#             self.beide_Modi_berechne_schritthoehe(self.neuer_zustand,self.alter_zustand)
#             ausgangs_position = self.alter_zustand 
#             for schrittanzahl in range(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]):
#                 ausgangs_position += self.schritthoehe
#                 dc = self.gradmodus_berechne_dc_aus_gradzahl(ausgangs_position)
#                 self.set_servo_pulse(dc)
#                 time.sleep(0.01)
#         else:
#             self.beide_Modi_berechne_schritthoehe(self.alter_zustand, self.neuer_zustand)
#             ausgangs_position = self.alter_zustand 
#             for schrittanzahl in range(Zielzustand.ZIELZUSTAENDE.get(self.servoname)[1]): 
#                 ausgangs_position -= self.schritthoehe
#                 dc = self.gradmodus_berechne_dc_aus_gradzahl(ausgangs_position)
#                 self.set_servo_pulse(dc)
#                 time.sleep(0.01)


# Wird wenn immer Bewegung um Grad in Schritten aufgerufen wird eigentlich nicht benötigt        
#     def gradmodus_bewegung_um_Grad(self, gradzahl):
#         pulse = self.gradmodus_berechne_dc_aus_gradzahl(gradzahl) # möglicherweise nicht in Grad übergeben, sondern stattdessen für delta Winkel exakte Schrittanzahl festlegen mit 0 = default 0° und 10 dem maximalen Winkel
#         self.set_servo_pulse(pulse)   
        

         