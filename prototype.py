#!/usr/bin/python

from Raspi_PWM_Servo_Driver import PWM
import time
import RPi.GPIO as GPIO

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x70)

servoMin = 300  # Min pulse length out of 4096
servoMax = 600 # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  print pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)
# Set frequency to 60 Hz

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  
# pwm.setPWM(0, 0, servoMin)
# time.sleep(1)

v=input('Enter the duration (s)')
# y= input('Enter the strength')
z=input('Select which finger you want to move: 1=index, 2=middle, 3=thumb, 4=all, 5=reverse motors')

x=0
on=4096
off=0

button_press = GPIO.input(13)

if int(z)==1:
    
    while (x<v):
        pwm.setPWM(0, 0, 410)
        time.sleep(1)
        x=x+1
            
    pwm.setPWM(0, 0 , 4096)
      
if int(z)==2:
    while (x<v):
        pwm.setPWM(1, 0, 410)
        time.sleep(1)
        x=x+1
    


if int(z)==3:
    pwm.setPWM(14, 0, servoMax)
    time.sleep(1)
    
if int(z)==4:
    while (x<v):
        pwm.setPWM(0, 0, servoMax)
        time.sleep(1)
        
        pwm.setPWM(1, 0, servoMax)
        time.sleep(1)
        
        pwm.setPWM(15, 0, servoMax)
        time.sleep(1)
        x=x+1
        
    pwm.setPWM(0, 0 , 4096)
    pwm.setPWM(1, 0 , 4096)
    pwm.setPWM(15, 0 , 4096)
    
   
    
if int(z)==5:
    while (x<v):
        pwm.setPWM(0, 1, servoMin)
        time.sleep(1)
        
        pwm.setPWM(1, 1, servoMin)
        time.sleep(1)
        
        pwm.setPWM(15, 1, servoMin)
        time.sleep(1)
        
        x=x+1
    
    pwm.setPWM(0, 0 , 4096)   