#!/usr/bin/python3
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio
import class_led
import xbox
import class_servo

if __name__=="__main__":
    joy = xbox.Joystick()
    led = class_led.led()
    servo1 = class_servo.servo()
    led.start()
    while not joy.Back():
        try:
            if joy.A():
                led.stelle_farbe_ein("gruen")
            if joy.B():
                led.stelle_farbe_ein("rot")
            if joy.Y():
                led.stelle_farbe_ein("orange")
            if joy.X():
                led.stelle_farbe_ein("blau")
            
            if joy.leftThumbstick():
                print(joy.leftStick())      
                       
#             if joy.rightTrigger >0 :
#                 rightTrigger = joy.rightTrigger()
#                 led.farbintensitaet(rightTrigger)
            
            if joy.rightBumper():
                xl,yl = joy.leftStick()
                xr,yr = joy.rightStick()
                servo1.start()
                
            
            if joy.leftBumper():
                xl,yl = joy.leftStick()
                xr,yr = joy.rightStick()
                servo1.jip()
                
            if joy.Start():
                gpio.cleanup()
                joy.close()
                servo1.stop()
                    
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
            