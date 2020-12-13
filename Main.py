#!/usr/bin/python3
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio
import class_led
#import xbox
import class_servo
import classZielzustand
import class_Action


if __name__=="__main__":
    #joy = xbox.Joystick()
    #zielzustandsobjekt = class_Zielzustand.Zielzustand()
    led = class_led.Led()
    ellbogen_servo1 = class_servo.Servo("ellbogen_servo1")
    led.start()
    action = class_Action.Action()
    
    try:
        action.update_zielzustand()
            
            
#     while not joy.Back():
#         try:
#             
#             #update_Zielzustand
#             if joy.A():
#                 print(zielzustand.zielzustaende)
#                 
#                 led.stelle_farbe_ein("gruen")
#             if joy.B():
#                 led.stelle_farbe_ein("rot")
#             if joy.Y():
#                 led.stelle_farbe_ein("gelb")
#             if joy.X():
#                 led.stelle_farbe_ein("blau")
#             
#             if joy.leftThumbstick():
#                 print(joy.leftStick())      
#                        
#             if joy.rightTrigger >0 :sg
#                 rightTrigger = joy.rightTrigger()
#                 led.farbintensitaet(rightTrigger)
#             
#             if joy.rightBumper():
#                 ellbogen_servo1.start()
#                 
#                 
#             if joy.leftBumper():
#                 ellbogen_servo1.start()
#                 
# 
#                
#                
#                
#                
#                #ellbogen_servo1.start()
#                  
# #             if joy.leftBumper():
# #                 xl,yl = joy.leftStick()
# #                 xr,yr = joy.rightStick()
# #                 ellbogen_servo1.jip()
#                 
#             if joy.Start():
#                 gpio.cleanup()
#                 joy.close()
#                 ellbogen_servo1.stop()
#                     
            #if bla bla break
                
                                   
#             if xl < 0:
#                 led.farbverlauf()    #hier blockiert wegen der Methode logischerweise das Programm. Muss ich hier also threaden? 
#             else:
#                 print("no")
#             
    except KeyboardInterrupt:  #finally
        gpio.cleanup()
            
            
            # ein thread tasten drücken und zielzustand ermitteln -> aktuelles Ziel benennen (objekt mit klasse)
            # zweiter thread : aktorik thread  -> überprüft das ziel und wo er sich befindet und was er unternehmen muss um das ziel zu erreichen, also zustand und zielzustand bekannt und überlegt was zu tun; zielzustand ist gemeinsame ressource
            # thread 2 interessiert nicht wer die zielzustände setzt, sondern steuert nur den zielzustand an (also 1 weiß von 2 nix und 2 von 1 nix außer zielzustand) 
        