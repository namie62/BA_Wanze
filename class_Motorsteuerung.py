from threading import Lock
import Adafruit_PCA9685
import time

# Wrapper Klasse für Adafruit_PCA9685 Klasse, um einen Lock einzubauen. Alle Servo Threads in class_Servo_Steuerung greifen sonst gleichzeitig beim Senden des Signals an den
# Motopi auf die selbe Ressource zu und dadurch wird oft das Signal unterbrochen
class Motorsteuerung:
    def __init__(self):
        self.motorsteuerung = Adafruit_PCA9685.PCA9685(address=0x41)
        self.lock = Lock()

    def set_pwm(self, channel, pulse):
        with self.lock:
            #print("[%s] pulse=%s, channel=%s" % (time.time(), pulse, channel) )
            self.motorsteuerung.set_pwm(channel, 0, pulse)
            self.motorsteuerung.set_pwm_freq(50)