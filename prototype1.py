#!/usr/bin/python

## MOTORS
from Raspi_PWM_Servo_Driver import PWM
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN
)           #, pull_up_down=GPIO.PUD_UP)

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
  
def finger1_450(n):#finger 1
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(0, 0, 450)#going foward
        time.sleep(1) 
        #if button_press == False:
         #   pwm.setPWM(0,0,4096)
          # time.sleep(n)
           # x=x+1
            
            #print('Stopping now '+ str(x))
            
            #while button_press == False:
            #   button_press = GPIO.input(7)
        x=x+1   #counter
    pwm.setPWM(0, 0 , 4096)#shut off

def finger1_440(n):#finger 1 440
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        if button_press == True:
            pwm.setPWM(0, 0, 440)#going foward
            time.sleep(1)
            x=x+1
        else: #button_press == False:
            
            pwm.setPWM(0,0,4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        time.sleep(1)
        x=x+1   #counter
    pwm.setPWM(0, 0 , 4096)#shut off

def finger1_430(n):#finger 1
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(0, 0, 430)#going foward
        time.sleep(1)
        x=x+1
        if button_press == False:
            pwm.setPWM(0,0,4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        time.sleep(1)
        x=x+1   #counter
    pwm.setPWM(0, 0 , 4096)#shut off

def finger1_420(n):#finger 1 420
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(0, 0, 420)#going foward
        time.sleep(1) 
        if button_press == False:
            pwm.setPWM(0,0,4096)
            time.sleep(n)
            x=x+1 
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        time.sleep(1)
        x=x+1   #counter
    pwm.setPWM(0, 0 , 4096)#shut off
def finger1_410(n):#finger 1 410 
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(0, 0, 410)#going foward
        time.sleep(1) 
        if button_press == False:
            pwm.setPWM(0,0,4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        time.sleep(1)
        x=x+1   #counter
    pwm.setPWM(0, 0 , 4096)#shut off

def finger1_r280(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(0, 0, 280) #going reverse
        time.sleep(1)
        #if button_press == False:
            #pwm.setPWM(0,0,4096)
            #time.sleep(n)
            #x=x+1
            #print('Stopping now '+ str(x))
            #while button_press == False:
                #button_press = GPIO.input(7)
        x=x+1#counter
    pwm.setPWM(0, 0 , 4096) #shut off    

def finger1_r290(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(0, 0, 290) #going reverse
        time.sleep(1)
        if button_press == False:
            pwm.setPWM(0,0,4096)
            time.sleep(1)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1#counter
    pwm.setPWM(0, 0 , 4096) #shut off
    
def finger1_r300(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(0, 0, 300) #going reverse
        time.sleep(1)
        if button_press == False:
            pwm.setPWM(0,0,4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1
    pwm.setPWM(0, 0 , 4096) #shut off
    
def finger1_r310(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(0, 0, 310) #going reverse
        time.sleep(1)
        if button_press == False:
            pwm.setPWM(0,0,4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
        x=x+1#counter
    pwm.setPWM(0, 0 , 4096) #shut off
    
def finger1_r320(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(0, 0, 320) #going reverse
        time.sleep(1)
        if button_press == False:
            pwm.setPWM(0,0,4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
        x=x+1#counter
    pwm.setPWM(0, 0 , 4096) #shut off   
    
def finger2_450(n):#finger 1
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(1, 0, 450)#going foward
        time.sleep(1) 
        #if button_press == False:
            #pwm.setPWM(1,0,4096)
            #time.sleep(n)
            #x=x+1
            #
            #print('Stopping now '+ str(x))
            
            #while button_press == False:
                #button_press = GPIO.input(7)
        x=x+1   #counter
    pwm.setPWM(1, 0 , 4096)#shut off
    
def finger2_440(n):#finger 1
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(1, 0, 440)#going foward
        time.sleep(1) 
        ##if button_press == False:
            ##pwm.setPWM(1,0,4096)
            ##time.sleep(n)
            ##x=x+1
            
            ##print('Stopping now '+ str(x))
            
            ##while button_press == False:
                ##button_press = GPIO.input(7)
        x=x+1   #counter
    pwm.setPWM(1, 0 , 4096)#shut off

def finger2_430(n):#finger 1
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(1, 0, 430)#going foward
        time.sleep(1) 
        ##if button_press == False:
           ## pwm.setPWM(1,0,4096)
           ## time.sleep(n)
           ## x=x+1
            
           ## print('Stopping now '+ str(x))
            
            ##while button_press == False:
                ##button_press = GPIO.input(7)
        x=x+1   #counter
    pwm.setPWM(1, 0 , 4096)#shut off
    
def finger2_420(n):#finger 1
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(1, 0, 420)#going foward
        time.sleep(1) 
        ##if button_press == False:
           ## pwm.setPWM(1,0,4096)
            ##time.sleep(n)
            ##x=x+1
            
            #print('Stopping now '+ str(x))
##            
            #while button_press == False:
             #   button_press = GPIO.input(7)
        x=x+1   #counter
    pwm.setPWM(1, 0 , 4096)#shut off
    
def finger2_410(n):#finger 1
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(1, 0, 410)#going foward
        time.sleep(1) 
        #if button_press == False:
         #   pwm.setPWM(1,0,4096)
          #  time.sleep(n)
           # x=x+1
            
           #print('Stopping now '+ str(x))
            
            #while button_press == False:
             #   button_press = GPIO.input(7)
        x=x+1   #counter
    pwm.setPWM(1, 0 , 4096)#shut off

def finger2_r280(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(1, 0, 280) #going reverse
        time.sleep(1)
        #if button_press == False:
            #pwm.setPWM(1,0,4096)
            #time.sleep(n)
            ##x=x+1
            #print('Stopping now '+ str(x))
            #while button_press == False:
                #button_press = GPIO.input(7)
        x=x+1#counter
    pwm.setPWM(1, 0 , 4096) #shut off
    
def finger2_r290(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(1, 0, 290) #going reverse
        time.sleep(1)
        ##if button_press == False:
          ##  pwm.setPWM(1,0,4096)
            ##time.sleep(n)
            ##x=x+1
            ##print('Stopping now '+ str(x))
            ##while button_press == False:
              ##  button_press = GPIO.input(7)
        ##x=x+1#counter
    pwm.setPWM(1, 0 , 4096) #shut off
    
def finger2_r300(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(1, 0, 300) #going reverse
        time.sleep(1)
        if button_press == False:
            pwm.setPWM(1,0,4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1#counter
    pwm.setPWM(1, 0 , 4096) #shut off
    
def finger2_r310(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(1, 0, 310) #going reverse
        time.sleep(1)
        if button_press == False:
            pwm.setPWM(1,0,4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1#counter
    pwm.setPWM(1, 0 , 4096) #shut off
    
def finger2_r320(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(1, 0, 320) #going reverse
        time.sleep(1)
        if button_press == False:
            pwm.setPWM(1,0,4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1#counter
    pwm.setPWM(1, 0 , 4096) #shut off
    
def finger3_450(n):#finger 1
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(15, 0, 450)#going foward
        time.sleep(1) 
        #if button_press == False:
            #pwm.setPWM(15,0,4096)
            #time.sleep(n)
            #x=x+1
            
            #print('Stopping now '+ str(x))
            
            #while button_press == False:
                #button_press = GPIO.input(7)
        x=x+1   #counter
    pwm.setPWM(15, 0 , 4096)#shut off
    
def finger3_440(n):#finger 1
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(15, 0, 440)#going foward
        time.sleep(1) 
        if button_press == False:
            pwm.setPWM(15,0,4096)
            time.sleep(n)
            x=x+1
            
            print('Stopping now '+ str(x))
            
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1   #counter
    pwm.setPWM(15, 0 , 4096)#shut off
    
def finger3_430(n):#finger 1
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(15, 0, 430)#going foward
        time.sleep(1) 
        if button_press == False:
            pwm.setPWM(15,0,4096)
            time.sleep(n)
            x=x+1
            
            print('Stopping now '+ str(x))
            
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1   #counter
    pwm.setPWM(15, 0 , 4096)#shut off
    
def finger3_420(n):#finger 1
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(15, 0, 420)#going foward
        time.sleep(1) 
        if button_press == False:
            pwm.setPWM(15,0,4096)
            time.sleep(n)
            x=x+1
            
            print('Stopping now '+ str(x))
            
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1   #counter
    pwm.setPWM(15, 0 , 4096)#shut off
    
def finger3_410(n):#finger 1
    
    x=0
    while (x<n):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(15, 0, 410)#going foward
        time.sleep(1) 
        if button_press == False:
            pwm.setPWM(15,0,4096)
            time.sleep(n)
            x=x+1
            
            print('Stopping now '+ str(x))
            
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1   #counter
    pwm.setPWM(15, 0 , 4096)#shut off
    
def finger3_r280(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(15, 0, 280) #going reverse
        time.sleep(1)
       # if button_press == False:
            #pwm.setPWM(15,0,4096)
           # time.sleep(n)
            #x=x+1
            #print('Stopping now '+ str(x))
            #while button_press == False:
                #button_press = GPIO.input(7)
        x=x+1#counter
    pwm.setPWM(15, 0 , 4096) #shut off
    
def finger3_r290(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(15, 0, 290) #going reverse
        time.sleep(1)
        if button_press == False:
            pwm.setPWM(15,0,4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1#counter
    pwm.setPWM(15, 0 , 4096) #shut off
    
def finger3_r300(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(15, 0, 300) #going reverse
        time.sleep(1)
        if button_press == False:
            pwm.setPWM(15,0,4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1#counter
    pwm.setPWM(15, 0 , 4096) #shut off

def finger3_r310(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(15, 0, 310) #going reverse
        time.sleep(1)
        if button_press == False:
            pwm.setPWM(15,0,4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1#counter
    pwm.setPWM(15, 0 , 4096) #shut off
    
def finger3_r320(n): #finger 1
    
    x=0
    while (x<n): #duration
        button_press = GPIO.input(7)
        pwm.setPWM(15, 0, 320) #going reverse
        time.sleep(1)
        if button_press == False:
            pwm.setPWM(15,0,4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1#counter
    pwm.setPWM(15, 0 , 4096) #shut off
    
def all_450(n):
    x=0
    while (x<n):
        button_press = GPIO.input(7)
        pwm.setPWM(0, 0, 450)
        pwm.setPWM(1, 0, 450)
        pwm.setPWM(15, 0, 450)
        time.sleep(1)
        x=x+1
        if button_press == False:
            pwm.setPWM(0,0,4096)
            pwm.setPWM(1, 0, 4096)
            pwm.setPWM(15, 0, 4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1
    pwm.setPWM(0, 0 , 4096)
    pwm.setPWM(1, 0 , 4096)
    pwm.setPWM(15, 0 , 4096)
    
def all_440(n):
    x=0
    while (x<n):
        button_press = GPIO.input(7)
        pwm.setPWM(0, 0, 440)
        pwm.setPWM(1, 0, 440)
        pwm.setPWM(15, 0, 440)
        time.sleep(1)
        x=x+1
        if button_press == False:
            pwm.setPWM(0,0,4096)
            pwm.setPWM(1, 0, 4096)
            pwm.setPWM(15, 0, 4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1
    pwm.setPWM(0, 0 , 4096)
    pwm.setPWM(1, 0 , 4096)
    pwm.setPWM(15, 0 , 4096)
    
def all_430(n):
    x=0
    while (x<n):
        button_press = GPIO.input(7)
        pwm.setPWM(0, 0, 430)
        pwm.setPWM(1, 0, 430)
        pwm.setPWM(15, 0, 430)
        time.sleep(1)
        x=x+1
        if button_press == False:
            pwm.setPWM(0,0,4096)
            pwm.setPWM(1, 0, 4096)
            pwm.setPWM(15, 0, 4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1
    pwm.setPWM(0, 0 , 4096)
    pwm.setPWM(1, 0 , 4096)
    pwm.setPWM(15, 0 , 4096)
    
def all_420(n):
    x=0
    while (x<n):
        button_press = GPIO.input(7)
        pwm.setPWM(0, 0, 420)
        pwm.setPWM(1, 0, 420)
        pwm.setPWM(15, 0, 420)
        time.sleep(1)
        x=x+1
        if button_press == False:
            pwm.setPWM(0,0,4096)
            pwm.setPWM(1, 0, 4096)
            pwm.setPWM(15, 0, 4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1
    pwm.setPWM(0, 0 , 4096)
    pwm.setPWM(1, 0 , 4096)
    pwm.setPWM(15, 0 , 4096)
    
def all_410(n):
    x=0
    while (x<n):
        button_press = GPIO.input(7)
        pwm.setPWM(0, 0, 410)
        pwm.setPWM(1, 0, 410)
        pwm.setPWM(15, 0, 410)
        time.sleep(1)
        x=x+1
        if button_press == False:
            pwm.setPWM(0,0,4096)
            pwm.setPWM(1, 0, 4096)
            pwm.setPWM(15, 0, 4096)
            time.sleep(n)
            x=x+1
            print('Stopping now '+ str(x))
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1
    pwm.setPWM(0, 0 , 4096)
    pwm.setPWM(1, 0 , 4096)
    pwm.setPWM(15, 0 , 4096)
    
def reverse_280(n):#all fingers
    x=0
    while (x<n):#duration
        button_press=GPIO.input(7)
        pwm.setPWM(0, 0, 280)
        pwm.setPWM(1, 0, 280)
        pwm.setPWM(15, 0, 280)
        x=x+1
        time.sleep(1)
        if button_press==False:
            pwm.setPWM(0,0,4096)
            pwm.setPWM(1,0,4096)
            pwm.setPWM(15,0,4096)
            time.sleep(n)
            x=x+1
            print("stopping now " +x)
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1
    pwm.setPWM(0, 0 , 4096)
    pwm.setPWM(1, 0 , 4096)
    pwm.setPWM(15, 0 , 4096)
    
def reverse_290(n):#all fingers
    x=0
    while (x<n):#duration
        button_press=GPIO.input(7)
        pwm.setPWM(0, 0, 290)
        pwm.setPWM(1, 0, 290)
        pwm.setPWM(15, 0, 290)
        x=x+1
        time.sleep(1)
        if button_press==False:
            pwm.setPWM(0,0,4096)
            pwm.setPWM(1,0,4096)
            pwm.setPWM(15,0,4096)
            time.sleep(n)
            x=x+1
            print("stopping now " +x)
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1
    pwm.setPWM(0, 0 , 4096)
    pwm.setPWM(1, 0 , 4096)
    pwm.setPWM(15, 0 , 4096)

def reverse_300(n):#all fingers
    x=0
    while (x<n):#duration
        button_press=GPIO.input(7)
        pwm.setPWM(0, 0, 300)
        pwm.setPWM(1, 0, 300)
        pwm.setPWM(15, 0, 300)
        x=x+1
        time.sleep(1)
        if button_press==False:
            pwm.setPWM(0,0,4096)
            pwm.setPWM(1,0,4096)
            pwm.setPWM(15,0,4096)
            time.sleep(n)
            x=x+1
            print("stopping now " +x)
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1
    pwm.setPWM(0, 0 , 4096)
    pwm.setPWM(1, 0 , 4096)
    pwm.setPWM(15, 0 , 4096)
    
def reverse_310(n):#all fingers
    x=0
    while (x<n):#duration
        button_press=GPIO.input(7)
        pwm.setPWM(0, 0, 310)
        pwm.setPWM(1, 0, 310)
        pwm.setPWM(15, 0,310)
        x=x+1
        time.sleep(1)
        if button_press==False:
            pwm.setPWM(0,0,4096)
            pwm.setPWM(1,0,4096)
            pwm.setPWM(15,0,4096)
            time.sleep(n)
            x=x+1
            print("stopping now " +x)
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1
    pwm.setPWM(0, 0 , 4096)
    pwm.setPWM(1, 0 , 4096)
    pwm.setPWM(15, 0 , 4096)
    
def reverse_280(n):#all fingers
    x=0
    while (x<n):#duration
        button_press=GPIO.input(7)
        pwm.setPWM(0, 0, 320)
        pwm.setPWM(1, 0, 320)
        pwm.setPWM(15, 0, 320)
        x=x+1
        time.sleep(1)
        if button_press==False:
            pwm.setPWM(0,0,4096)
            pwm.setPWM(1,0,4096)
            pwm.setPWM(15,0,4096)
            time.sleep(n)
            x=x+1
            print("stopping now " +x)
            while button_press == False:
                button_press = GPIO.input(7)
        x=x+1
    pwm.setPWM(0, 0 , 4096)
    pwm.setPWM(1, 0 , 4096)
    pwm.setPWM(15, 0 , 4096)
    
pwm.setPWMFreq(60) # Set frequency to 60 Hz

M_duration= input('Enter the duration (s)')
M_finger=input('Select which finger you want to move: 1=thumb, 2=middle, 3=index, 4=all, 5=Reverse motors')
M_direction=input('Select forward=0, reverse=1')
M_strength= input('Enter the strength (1-5)')

x=0
on=4096
off=0
        
if int(M_finger)==1: #Channel 1
    if int(M_direction)==0: #Channel 1, foward, 410-450
        if int(M_strength)==5:
            finger1_450(M_duration)
        elif int(M_strength)==4:
            finger1_440(M_duration)
        elif int(M_strength)==3:
            finger1_430(M_duration)
        elif int(M_strength)==2:
            finger1_420(M_duration)
        elif int(M_strength)==1:
            finger1_410(M_duration)
            
    if int(M_direction)==1: #Channel 1, Reverse 280-320
        if int(M_strength)==5:
            finger1_r280(M_duration)
        elif int(M_strength)==4:
            finger1_r290(M_duration)
        elif int(M_strength)==3:
            finger1_r300(M_duration)
        elif int(M_strength)==2:
            finger1_r310(M_duration)
        elif int(M_strength)==1:
            finger1_r320(M_duration)
    
if int(M_finger)==2: #Channel 2
    if int(M_direction)==0: #Channel 2, foward, 410-450
        if int(M_strength)==5:
            finger2_450(M_duration)
        elif int(M_strength)==4:
            finger2_440(M_duration)
        elif int(M_strength)==3:
            finger2_430(M_duration)
        elif int(M_strength)==2:
            finger2_420(M_duration)
        elif int(M_strength)==1:
            finger2_410(M_duration)
            
    if int(M_direction)==1: #Channel 2, Reverse 280-320
        if int(M_strength)==5:
            finger2_r280(M_duration)
        elif int(M_strength)==4:
            finger2_r290(M_duration)
        elif int(M_strength)==3:
            finger2_r300(M_duration)
        elif int(M_strength)==2:
            finger2_r310(M_duration)
        elif int(M_strength)==1:
            finger2_r320(M_duration)
    
if int(M_finger)==3: #Channel 3
    if int(M_direction)==0: #Channel 3, forward, 410-450
        if int(M_strength)==5:
            finger3_450(M_duration)
        elif int(M_strength)==4:
            finger3_440(M_duration)
        elif int(M_strength)==3:
            finger3_430(M_duration)
        elif int(M_strength)==2:
            finger3_420(M_duration)
        elif int(M_strength)==1:
            finger3_410(M_duration)
            
    if int(M_direction)==1: #Channel 3, Reverse 280-320
        if int(M_strength)==5:
            finger3_r280(M_duration)
        elif int(M_strength)==4:
            finger3_r290(M_duration)
        elif int(M_strength)==3:
            finger3_r300(M_duration)
        elif int(M_strength)==2:
            finger3_r310(M_duration)
        elif int(M_strength)==1:
            finger3_r320(M_duration)
    
if int(M_finger)==4:
    if int(M_strength==5):
        all_450(M_duration)
    elif int(M_strength)==4:
        all_440(M_duration)
    elif int(M_strength)==3:
        all_430(M_duration)
    elif int(M_strength)==2:
        all_420(M_duration)    
    elif int(M_strength)==1:
        all_410(M_duration)
        
if int(M_finger)==5:
    if int(M_strength==5):
        reverse_280(M_duration)
    elif int(M_strength==4):
        reverse_290(M_duration)
    elif int(M_strength==3):
        reverse_300(M_duration)
    elif int(M_strength==2):
        reverse_310(M_duration)
    elif int(M_strength==1):
        reverse_320(M_duration)    