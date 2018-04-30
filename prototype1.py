#!/usr/bin/python

## MOTORS
from Raspi_PWM_Servo_Driver import PWM
import time
import RPi.GPIO as GPIO

motors = PWM(0x70)# Initialise the PWM device using the default address bmp = PWM(0x40, debug=True)
servoMin = 300  # Min pulse length out of 4096
servoMax = 450 # Max pulse length out of 4096

MOTORMAX = 4096

THMBCHANNEL=15
FORECHANNEL=0
MIDCHANNEL=1

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
  
#Thumb
def finger1forward(totaltime):
    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
    while (timeelapsed<totaltime): #until the total time has elapsed,
        motors.setPWM(THMBCHANNEL, 0, 410) # set the channel
        time.sleep(1)
        timeelapsed+=1
    motors.setPWM(THMBCHANNEL, 0 , MOTORMAX)

    #GENERAL LOGIC:
    #while button 1 true then 
    #pwm.setPWM(15, 0, 410)
    #    time.sleep(1)
 

def finger1reverse(totaltime):#thumb in reverse
    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
    while (timeelapsed<totaltime): #until the total time has elapsed,
        motors.setPWM(THMBCHANNEL, 0, servoMin) # set the channel
        time.sleep(1)
        timeelapsed+=1#counter
    motors.setPWM(THMBCHANNEL, 0 , MOTORMAX)#shut off  

#if button 2 true then

#forefinger
def finger2forward(totaltime):#forefinger
    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
    while (timeelapsed<totaltime): #until the total time has elapsed,
        motors.setPWM(FORECHANNEL, 0, 410) # set the channel
        time.sleep(1)
        
        #if button_press==False:
         #   print('Stopping now')
          #  pwm.setPWM(0, 0 , 4096)
           # time.sleep(1)
        timeelapsed+=1#counter
    motors.setPWM(FORECHANNEL, 0 , MOTORMAX)#shut off
def finger2reverse(totaltime):#forefinger in reverse
    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
    while (timeelapsed<totaltime): #until the total time has elapsed,
        motors.setPWM(FORECHANNEL, 0, servoMin) # set the channel
        time.sleep(1)
        timeelapsed+=1#counter
    motors.setPWM(FORECHANNEL, 0 , MOTORMAX)#shut off    
    
#middle finger
def finger3forward(totaltime):
    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
    while (timeelapsed<totaltime): #until the total time has elapsed,
        motors.setPWM(MIDCHANNEL, 0, 450) # set the channel
        time.sleep(1)
        timeelapsed+=1
    motors.setPWM(MIDCHANNEL, 0 , MOTORMAX)

def finger3reverse(totaltime):#middle finger in reverse 
    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
    while (timeelapsed<totaltime): #until the total time has elapsed,
        motors.setPWM(MIDCHANNEL, 0, servoMin)# set the channel
        time.sleep(1)
        timeelapsed+=1#counter
    motors.setPWM(MIDCHANNEL, 0 , MOTORMAX)#shut off  
    
# first three fingers
def allforward(totaltime):
    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
    while (timeelapsed<totaltime): #until the total time has elapsed,
        motors.setPWM(THMBCHANNEL, 0, servoMax) # set the channel
        motors.setPWM(FORECHANNEL, 0, servoMax)
        motors.setPWM(MIDCHANNEL, 0, servoMax)
        timeelapsed+=1
        time.sleep(1)
    motors.setPWM(THMBCHANNEL, 0 , MOTORMAX)
    motors.setPWM(FORECHANNEL, 0 , MOTORMAX)
    motors.setPWM(MIDCHANNEL, 0 , MOTORMAX)
    
#reverse all fingers
def allreverse(totaltime):#all fingers
    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
    while (timeelapsed<totaltime): #until the total time has elapsed,
        motors.setPWM(THMBCHANNEL, 0, servoMin) # set the channel
        motors.setPWM(FORECHANNEL, 0, servoMin)
        motors.setPWM(MIDCHANNEL, 0, servoMin)
        timeelapsed+=1
        time.sleep(1)
    motors.setPWM(THMBCHANNEL, 0 , MOTORMAX)
    motors.setPWM(FORECHANNEL, 0 , MOTORMAX)
    motors.setPWM(MIDCHANNEL, 0 , MOTORMAX)


motors.setPWMFreq(60)
# Set frequency to 60 Hz

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  
# pwm.setPWM(0, 0, servoMin)
# time.sleep(1)

timeinput= input('Enter the duration (s)')
fingerinput=input('Select which finger you want to move: 1=thumb, 2=index, 3=middle, 4=all, 5=reverse motors')
forwardOrReverse=input('Select foward=0, reverse=1')

x=0
on=4096
off=0

button_press = GPIO.input(7)

if button_press==False:
        print('Stopping now')
        motors.setPWM(FORECHANNEL, 0 , MOTORMAX)
        time.sleep(1)

if int(fingerinput)==1:
    if int(forwardOrReverse)==0:
        finger1forward(timeinput)
    if int(forwardOrReverse)==1:
        finger1reverse(timeinput)
    #if button_press==False:
        #print('Stopping now')
        #pwm.setPWM(0, 0 , 4096)
        #time.sleep(1)
if int(fingerinput)==2:
    if int(forwardOrReverse)==0:
        finger2forward(timeinput)
    if int(forwardOrReverse)==1:
        finger2reverse(timeinput)
    
if int(fingerinput)==3:
    if int(forwardOrReverse)==0:
        finger3forward(timeinput)
    if int(forwardOrReverse)==1:
        finger3reverse(timeinput)
    
if int(fingerinput)==4:
    
    allforward(timeinput)
    
if int(fingerinput)==5:
    
    allreverse(timeinput)