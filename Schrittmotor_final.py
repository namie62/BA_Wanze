from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Verwendete Pins am Rapberry Pi
A=11
B=13
C=15
D=19
time = 0.0005


table = [[True,False,False,False],
         [True,True,False,False],
         [False,True,False,False],
         [False,True,True,False],
         [False,False,True,False],
         [False,False,True,True],
         [False,False,False,True],
         [True,False,False,True]]
        
# Pins aus Ausgänge definieren
GPIO.setup(A,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
GPIO.setup(C,GPIO.OUT)
GPIO.setup(D,GPIO.OUT)
GPIO.output(A, False)
GPIO.output(B, False)
GPIO.output(C, False)
GPIO.output(D, False)

def default():
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    

#Kopf ausfahren
def vorwaerts():
    readfile = open('position.txt', 'r')
    position = int(readfile.read())
    readfile.close()
    while position < 2600:
        for j in range(7,-1,-1):
            GPIO.output(A, table[j][0])
            GPIO.output(B, table[j][1])
            GPIO.output(C, table[j][2])
            GPIO.output(D, table[j][3])
            sleep(time)
            position += 1
            GPIO.output(A, False)
            GPIO.output(B, False)
            GPIO.output(C, False)
            GPIO.output(D, False)
            if(position >=2600):
                break
    writefile = open('position.txt', 'w')
    writefile.write(str(position))
    writefile.close()        
    print(position)

#Kopf einfahren
def zurueck():
    readfile = open('position.txt', 'r')
    position = int(readfile.read())
    readfile.close()
    while position >=0:
        for j in range(8):
            GPIO.output(A, table[j][0])
            GPIO.output(B, table[j][1])
            GPIO.output(C, table[j][2])
            GPIO.output(D, table[j][3])
            sleep(time)
            position -= 1
            GPIO.output(A, False)
            GPIO.output(B, False)
            GPIO.output(C, False)
            GPIO.output(D, False)
            if position<0:
                break
    writefile = open('position.txt', 'w')
    writefile.write(str(position))
    writefile.close()
    print(position)


GPIO.cleanup()

