from __future__ import division
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685(address=0x41)
servoStart = 0.6
servo = servoStart
servoEnd = 2.5

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000 # 1,000,000 us per second
    pulse_length /= 50 # 60 Hz
    pulse_length /= 4096 # 12 bits of resolution
    pulse *= 1000
    pulse /= pulse_length
    pulse = round(pulse)
    pulse = int(pulse)
    pwm.set_pwm(channel, 0, pulse)
    pwm.set_pwm_freq(50)
    
    
##################################################
######### Initialise Start-Up-Positions ##########
##################################################
# for x in range(0, 16):
#     set_servo_pulse(x, servoStart)
#     time.sleep(2)
# ##################################################
# ######### Max-Range for every servo ##############
# ##################################################
# for x in range (0, 16):
#     while (servo < servoEnd):
#         set_servo_pulse(x, servo0)
#         servo = (servo + 0.05)
#         time.sleep(0.04)
#         time.sleep(1)

set_servo_pulse(1, servoStart)
time.sleep(1)
set_servo_pulse(1, servoEnd)