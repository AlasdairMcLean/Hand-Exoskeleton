#!/usr/bin/python

## MOTORS
from Raspi_PWM_Servo_Driver import PWM
import time
import RPi.GPIO as GPIO

pwm = PWM(0x70)# Initialise the PWM device using the default address bmp = PWM(0x40, debug=True)
servoMin = 300  # Min pulse length out of 4096
servoMax = 450 # Max pulse length out of 4096

#def setServoPulse(channel, pulse):
  #pulseLength = 1000000                   # 1,000,000 us per second
  #pulseLength /= 60                       # 60 Hz
  #print ("%d us per period") % pulseLength
  #pulseLength /= 4096                     # 12 bits of resolution
  #print ("%d us per bit") % pulseLength
  #pulse *= 1000
  #pulse /= pulseLength
  #print pulseLength
  #pwm.setPWM(channel, 0, pulse)
  
def finger1(n):#finger 1 
    x=0
    while (x<n):#duration
        pwm.setPWM(0, 0, 410)#going foward
        time.sleep(1)
        
        #if button_press==False:
         #   print('Stopping now')
          #  pwm.setPWM(0, 0 , 4096)
           # time.sleep(1)
        x=x+1#counter
    pwm.setPWM(0, 0 , 4096)#shut off
def finger1_r(n):#finger 1 in reverse
    x=0
    while (x<n):#duration
        pwm.setPWM(0, 0, servoMin)#going reverse
        time.sleep(1)
        x=x+1#counter
    pwm.setPWM(0, 0 , 4096)#shut off    
    
    
def finger2(n): # finger 2 forwards
    x=0
    while (x<n):
        pwm.setPWM(1, 0, 450)
        time.sleep(1)
        x=x+1
    pwm.setPWM(1, 0 , 4096)

def finger2_r(n):#finger 2 in reverse
    x=0
    while (x<n):#duration
        pwm.setPWM(1, 0, servoMin)#going foward
        time.sleep(1)
        x=x+1#counter
    pwm.setPWM(1, 0 , 4096)#shut off  
    
def finger3(n): # finger 3
    x=0
    while (x<n):
        pwm.setPWM(15, 0, 410)
        time.sleep(1)
        x=x+1 
    pwm.setPWM(15, 0 , 4096)
    
def finger3_r(n):#finger 3 in reverse
    x=0
    while (x<n):#duration
        pwm.setPWM(15, 0, servoMin)#going foward
        time.sleep(1)
        x=x+1#counter
    pwm.setPWM(15, 0 , 4096)#shut off  
    
def all(n):
    x=0
    while (x<v):
        pwm.setPWM(0, 0, servoMax)
        pwm.setPWM(1, 0, servoMax)
        pwm.setPWM(15, 0, servoMax)
        x=x+1
        time.sleep(1)
    pwm.setPWM(0, 0 , 4096)
    pwm.setPWM(1, 0 , 4096)
    pwm.setPWM(15, 0 , 4096)
    
def reverse(n):#all fingers
    x=0
    while (x<v):#duration
        pwm.setPWM(0, 0, servoMin)
        pwm.setPWM(1, 0, servoMin)
        pwm.setPWM(15, 0, servoMin)
        x=x+1
        time.sleep(1)
    pwm.setPWM(0, 0 , 4096)
    pwm.setPWM(1, 0 , 4096)
    pwm.setPWM(15, 0 , 4096)


pwm.setPWMFreq(60)
# Set frequency to 60 Hz

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  
# pwm.setPWM(0, 0, servoMin)
# time.sleep(1)

v= input('Enter the duration (s)')
# y= input('Enter the strength')
z=input('Select which finger you want to move: 1=index, 2=middle, 3=thumb, 4=all, 5=reverse motors')
w=input('Select foward=0, reverse=1')

x=0
on=4096
off=0

button_press = GPIO.input(7)

if button_press==False:
        print('Stopping now')
        pwm.setPWM(0, 0 , 4096)
        time.sleep(1)
        
if int(z)==1:
    if int(w)==0:
        finger1(v)
    if int(w)==1:
        finger1_r(v)
    #if button_press==False:
        #print('Stopping now')
        #pwm.setPWM(0, 0 , 4096)
        #time.sleep(1)
if int(z)==2:
    if int(w)==0:
        finger2(v)
    if int(w)==1:
        finger2_r(v)
    
if int(z)==3:
    if int(w)==0:
        finger3(v)
    if int(w)==1:
        finger3_r(v)
    
if int(z)==4:
    
    all(v)
    
if int(z)==5:
    
    reverse(v)