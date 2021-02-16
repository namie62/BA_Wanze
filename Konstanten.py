#-*- coding: utf-8 -*-
import RPi.GPIO as gpio

# LED:
# Vorwiderstände der LEDs im Modell:
# rot: 270 Ohm    gruen: 220 Ohm     blau: 120 Ohm

# Pin-Belegung der LEDs
LED_PINS ={
     "rot_led1" : 8,
    "gruen_led1" : 10,
    "blau_led1" : 12,
    "rot_led2": 7,
    "gruen_led2": 11,
    "blau_led2":13
    }

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

#Fahrgestell
FAHRGESTELL_FREQUENZ = 50

#Servo
SERVO_FREQUENZ = 50

# Dictionary, das die maximalen und minimalen Werte des Duty Cycles (=DC) in Mikrosekunden enthält:
# - je nach Einbaurichtung des Motors, müssen die Drehrichtungen angepasst werden, indem der maximale und minimale DC umgedreht werden.
MOTOREN_MAX_MIN_PULSDAUER = { 
    "ellbogen_servo_links" : (2300, 1261), # 1261 entspricht ca. 110° (also von 180° auf 70°), da Ellbogenmotoren dürfen keine 180° rotieren, sonst wird die Sehne abgerissen!! -> Maximaler DC wurde kleiner gemacht. Experimentell wurde ermittelt, dass 110° Grad reicht -> DCmin = 1261
    "ellbogen_servo_rechts" : (600, 1638),  # 1638 entspricht ca. 110° (also von 0° auf 110°), da Ellbogenmotoren dürfen keine 180° rotieren, sonst wird die Sehne abgerissen!! -> Maximaler DC wurde kleiner gemacht. Experimentell wurde ermittelt, dass 110° Grad reicht -> DCmin = 1261
    "schulter_servo_links" : (600, 2300), # Schulterservos können 180°, rotieren aber wegen Übersetzungsverhältnis der Zahnräder einen kleineren Winkel und dadurch langsamer
    "schulter_servo_rechts": (2300, 600),
    "nacken_servo": (600, 2300), 
    "helm_servo" : (2200,600), }

SERVO_MODUS = "prozent"

STUFENANZAHL_ZWISCHEN_MIN_U_MAX_POSITION_DER_MOTOREN = 100 # Da Prozent

#GRADZAHL_ZWISCHEN_MIN_U_MAX_POSITION_DER_MOTOREN = 180 # Da Prozent

PROZENT_SCHRITTZAHL_JOYSTICK = 5

# Channel-Belegung der Motoren
MOTOREN_und_LED_CHANNELS = {  #Adafruit Motopi hat sogenannte Channel (insgesamt 16 Stück), an denen die Motoren hängen, kann theoretisch beliebig vergeben werden, 
    "ellbogen_servo_links" : 1, # Channelbelegung ist eigentlich egal, muss nur darauf geachtet werden, dass korrekt, da ansonsten was kaputt gehen kann.
    "ellbogen_servo_rechts" : 2, # sind etwas verteilt, weil die Stecker nicht nebeneinander Platz haben
    "schulter_servo_links" : 0,
    "schulter_servo_rechts": 4,
    "nacken_servo": 12,
    "helm_servo" : 13,
    "fahrgestell" : [21,22,23,32],
    "schrittmotor" : [15,16,18,19]}
    
# Schrittmotor Tabelle
SCHRITTMOTOR_TABELLE = [[gpio.HIGH,gpio.LOW,gpio.LOW,gpio.LOW],
         [gpio.HIGH,gpio.HIGH,gpio.LOW,gpio.LOW],
         [gpio.LOW,gpio.HIGH,gpio.LOW,gpio.LOW],
         [gpio.LOW,gpio.HIGH,gpio.HIGH,gpio.LOW],
         [gpio.LOW,gpio.LOW,gpio.HIGH,gpio.LOW],
         [gpio.LOW,gpio.LOW,gpio.HIGH,gpio.HIGH],
         [gpio.LOW,gpio.LOW,gpio.LOW,gpio.HIGH],
         [gpio.HIGH,gpio.LOW,gpio.LOW,gpio.HIGH]]