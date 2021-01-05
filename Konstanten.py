#-*- coding: utf-8 -*-


# LED:
# Vorwiderstände der LEDs im Modell:
# rot: 270 Ohm    gruen: 220 Ohm     blau: 280 Ohm

# RGB_PIN_NUMMERN = {
#     "rot_led1" : 12,
#     "gruen_led1" : 16,
#     "blau_led1" : 18,
#     "rot_led2": 11,
#     "gruen_led2": 13,
#     "blau_led2":15
#     }


FARBCODES = {
    "weiß" : (100,100,100),
    "hellgruen" : (10,100,10),
    "giftgruen" : (0,100,0),
    "gruen" : (0,100,0),
    "türkis" : (10,100,30),
    "hellblau" : (20,30,100),
    "blau" : (0,0,100),
    "lila" : (100,0,100),
    "flieder" : (70,0,100),
    "hellrosa" : (100,20,30),
    "pink" : (100,0,60),
    "rot" : (100,0,0),
    "orange" : (100,20,0),
    "gelb" : (100,50,0)
    }
# !!!!Achtung!!!! GPIO Mode kann entweder BOARD oder BCM sein. BCM heißt, dass die GPIO Nummern gleich den GPIO Bezeichnungen sind, BOARD heißt, dass die GPIO am Raspberry PI selbst abgezählt sind

LED_FREQUENZ = 150   #50 ist grenzwertig, dass gedimmte LED nicht flackert, eher höher gehen und dann nicht von Motor Hat aus steuern


#Servo

SERVO_FREQUENZ = 50

MOTOREN_und_LED_CHANNELS = {  #Adafruit Motopi hat sogenannte Channel (insgesamt 16 Stück), an denen die Motoren hängen, kann theoretisch beliebig vergeben werden, 
    "ellbogen_servo1" : 0,
    "ellbogen_servo2" : 2,
    "schulter_servo1" : 3,
    "schulter_servo2": 4,
    "nacken_servo": 5,
    "kopf_linear" : 6,
    "helm_servo" : 7,
     "rot_led1" : 8,
    "gruen_led1" : 9,
    "blau_led1" : 10,
    "rot_led2": 11,
    "gruen_led2": 12,
    "blau_led2":13
    }


MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL = { # Bei Test mit zwei versch. Servos fiel auf, dass sie unterschiedliche DC benötigen, um die vollen 180° anzufahren
    "ellbogen_servo1" : (0.6,2.4), # falls immer die gleichen Servos verwendet werden, dann kann das Dic evtl. aufgelöst werden 
    "ellbogen_servo2" : (2.5,12.5),
    "schulter_servo1" : (2.5,12.5),
    "schulter_servo2": (2.5,12.5),# ACHTUNG: mit adafruit library eig 0.6 bis 2.5 aber bei 2.5 brummelt der motor, da es ihm scheinbar zu weit ist. Evtl experimentell ausprobieren bei den anderen motoren
    "nacken_servo": (2.5,12.5),
    "kopf_linear" : (2.5,12.5),
    "helm_servo" : (2.5,12.5)}
