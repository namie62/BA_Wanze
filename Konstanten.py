#-*- coding: utf-8 -*-

# LED:
# Vorwiderstände der LEDs im Modell:
# rot: 270 Ohm    gruen: 220 Ohm     blau: 280 Ohm

LED_FREQUENZ = 150   #50 ist grenzwertig, dass gedimmte LED nicht flackert, eher höher gehen und dann nicht von Motor Hat aus steuern


#Farbcodes wurden über Dimmung experimentell ermittelt
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


#Servo
SERVO_FREQUENZ = 50

# Channel-Belegung der Motoren
MOTOREN_und_LED_CHANNELS = {  #Adafruit Motopi hat sogenannte Channel (insgesamt 16 Stück), an denen die Motoren hängen, kann theoretisch beliebig vergeben werden, 
    "ellbogen_servo1" : 1, # Channelbelegung ist eigentlich egal, muss nur darauf geachtet werden, dass korrekt, da ansonsten was kaputt gehen kann.
    "ellbogen_servo2" : 2, # sind etwas verteilt, weil die Stecker nicht nebeneinander Platz haben
    "schulter_servo1" : 0,
    "schulter_servo2": 4,
    "nacken_servo": 12,
    "helm_servo" : 15}
    

# Pin-Belegung der LEDs
LED_PINS ={
     "rot_led1" : 7,
    "gruen_led1" : 8,
    "blau_led1" : 10,
    "rot_led2": 11,
    "gruen_led2": 12,
    "blau_led2":13
    }


# Dictionary, das die maximalen und minimalen Werte des Duty Cycles (=DC) in Mikrosekunden enthält:
# - je nach Einbaurichtung des Motors, müssen die Drehrichtungen angepasst werden, indem der maximale und minimale DC umgedreht werden.
MOTOREN_MAX_MIN_DC_FÜR_GRADZAHL = { 
    "ellbogen_servo1" : (2300, 1261), # 1261 entspricht ca. 110° (also von 180° auf 70°), da Ellbogenmotoren dürfen keine 180° rotieren, sonst wird die Sehne abgerissen!! -> Maximaler DC wurde kleiner gemacht. Experimentell wurde ermittelt, dass 110° Grad reicht -> DCmin = 1261
    "ellbogen_servo2" : (600, 1638),  # 1638 entspricht ca. 110° (also von 0° auf 110°), da Ellbogenmotoren dürfen keine 180° rotieren, sonst wird die Sehne abgerissen!! -> Maximaler DC wurde kleiner gemacht. Experimentell wurde ermittelt, dass 110° Grad reicht -> DCmin = 1261
    "schulter_servo1" : (600, 2300), # Schulterservos können 180°, rotieren aber wegen Übersetzungsverhältnis der Zahnräder einen kleineren Winkel und dadurch langsamer
    "schulter_servo2": (2300, 600),
    "nacken_servo": (600, 2300), 
    "helm_servo" : (600,2300), }