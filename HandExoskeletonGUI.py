import Tkinter as tk
import datetime
#import matplotlib
#matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure

#!/usr/bin/python

## MOTORS
from Raspi_PWM_Servo_Driver import PWM
import time
import RPi.GPIO as GPIO

global f1forwardfreq, f2forwardfreq, f3forwardfreq, f1reversefreq, f2reversefreq, f3reversefreq
f1forwardfreq=0
f2forwardfreq=0
f3forwardfreq=0
f1reversefreq=0
f2reversefreq=0
f3reversefreq=0


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
        motors.setPWM(THMBCHANNEL, 0, f1forwardfreq) # set the channel
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
        motors.setPWM(THMBCHANNEL, 0, f1reversefreq) # set the channel
        time.sleep(1)
        timeelapsed+=1#counter
    motors.setPWM(THMBCHANNEL, 0 , MOTORMAX)#shut off  

#if button 2 true then

#forefinger
def finger2forward(totaltime):#forefinger
    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
    while (timeelapsed<totaltime): #until the total time has elapsed,
        motors.setPWM(FORECHANNEL, 0, f2forwardfreq) # set the channel
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
        motors.setPWM(FORECHANNEL, 0, f2reversefreq) # set the channel
        time.sleep(1)
        timeelapsed+=1#counter
    motors.setPWM(FORECHANNEL, 0 , MOTORMAX)#shut off    
    
#middle finger
def finger3forward(totaltime):
    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
    while (timeelapsed<totaltime): #until the total time has elapsed,
        motors.setPWM(MIDCHANNEL, 0, f3forwardfreq) # set the channel
        time.sleep(1)
        timeelapsed+=1
    motors.setPWM(MIDCHANNEL, 0 , MOTORMAX)

def finger3reverse(totaltime):#middle finger in reverse 
    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
    while (timeelapsed<totaltime): #until the total time has elapsed,
        motors.setPWM(MIDCHANNEL, 0, f3reversefreq)# set the channel
        time.sleep(1)
        timeelapsed+=1#counter
    motors.setPWM(MIDCHANNEL, 0 , MOTORMAX)#shut off  
    
# first three fingers
def allforward(totaltime):
    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
    while (timeelapsed<totaltime): #until the total time has elapsed,
        motors.setPWM(THMBCHANNEL, 0, f1forwardfreq) # set the channel
        motors.setPWM(FORECHANNEL, 0, f2forwardfreq)
        motors.setPWM(MIDCHANNEL, 0, f3forwardfreq)
        timeelapsed+=1
        time.sleep(1)
    motors.setPWM(THMBCHANNEL, 0 , MOTORMAX)
    motors.setPWM(FORECHANNEL, 0 , MOTORMAX)
    motors.setPWM(MIDCHANNEL, 0 , MOTORMAX)
    
#reverse all fingers
def allreverse(totaltime):#all fingers
    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
    while (timeelapsed<totaltime): #until the total time has elapsed,
        motors.setPWM(THMBCHANNEL, 0, f1reversefreq) # set the channel
        motors.setPWM(FORECHANNEL, 0, f2reversefreq)
        motors.setPWM(MIDCHANNEL, 0, f3reversefreq)
        timeelapsed+=1
        time.sleep(1)
    motors.setPWM(THMBCHANNEL, 0 , MOTORMAX)
    motors.setPWM(FORECHANNEL, 0 , MOTORMAX)
    motors.setPWM(MIDCHANNEL, 0 , MOTORMAX)




#Thumb
#def finger1forward(totaltime):
#    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
#    while (timeelapsed<totaltime): #until the total time has elapsed,
#        motors.setPWM(THMBCHANNEL, 0, 410) # set the channel
#        time.sleep(1)
#        timeelapsed+=1
#    motors.setPWM(THMBCHANNEL, 0 , MOTORMAX)

    #GENERAL LOGIC:
    #while button 1 true then 
    #pwm.setPWM(15, 0, 410)
    #    time.sleep(1)
 

#def finger1reverse(totaltime):#thumb in reverse
 #   timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
#    while (timeelapsed<totaltime): #until the total time has elapsed,
#        motors.setPWM(THMBCHANNEL, 0, servoMin) # set the channel
#        time.sleep(1)
#        timeelapsed+=1#counter
#    motors.setPWM(THMBCHANNEL, 0 , MOTORMAX)#shut off  

#if button 2 true then

#forefinger
#def finger2forward(totaltime):#forefinger
#    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
#    while (timeelapsed<totaltime): #until the total time has elapsed,
#        motors.setPWM(FORECHANNEL, 0, 410) # set the channel
#        time.sleep(1)
       
#        #if button_press==False:
#         #   print('Stopping now')
#          #  pwm.setPWM(0, 0 , 4096)
#           # time.sleep(1)
#        timeelapsed+=1#counter
#    motors.setPWM(FORECHANNEL, 0 , MOTORMAX)#shut off
#def finger2reverse(totaltime):#forefinger in reverse
#    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
#    while (timeelapsed<totaltime): #until the total time has elapsed,
#        motors.setPWM(FORECHANNEL, 0, servoMin) # set the channel
#        time.sleep(1)
#        timeelapsed+=1#counter
#    motors.setPWM(FORECHANNEL, 0 , MOTORMAX)#shut off    
    
#middle finger
#def finger3forward(totaltime):
#    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
#    while (timeelapsed<totaltime): #until the total time has elapsed,
#        motors.setPWM(MIDCHANNEL, 0, 450) # set the channel
#        time.sleep(1)
#        timeelapsed+=1
#    motors.setPWM(MIDCHANNEL, 0 , MOTORMAX)

#def finger3reverse(totaltime):#middle finger in reverse 
#    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
#    while (timeelapsed<totaltime): #until the total time has elapsed,
#        motors.setPWM(MIDCHANNEL, 0, servoMin)# set the channel
#        time.sleep(1)
  #      timeelapsed+=1#counter
  #  motors.setPWM(MIDCHANNEL, 0 , MOTORMAX)#shut off  
 #   
## first three fingers
#def allforward(totaltime):
#    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
#    while (timeelapsed<totaltime): #until the total time has elapsed,
#        motors.setPWM(THMBCHANNEL, 0, servoMax) # set the channel
#        motors.setPWM(FORECHANNEL, 0, servoMax)
#        motors.setPWM(MIDCHANNEL, 0, servoMax)
#        timeelapsed+=1
#        time.sleep(1)
#    motors.setPWM(THMBCHANNEL, 0 , MOTORMAX)
#    motors.setPWM(FORECHANNEL, 0 , MOTORMAX)
#    motors.setPWM(MIDCHANNEL, 0 , MOTORMAX)
    
#reverse all fingers
#def allreverse(totaltime):#all fingers
#    timeelapsed=0 # initialize a counter to keep track of how many seconds have elapsed
#    while (timeelapsed<totaltime): #until the total time has elapsed,
#       motors.setPWM(THMBCHANNEL, 0, servoMin) # set the channel
#        motors.setPWM(FORECHANNEL, 0, servoMin)
#        motors.setPWM(MIDCHANNEL, 0, servoMin)
#        timeelapsed+=1
#        time.sleep(1)
#    motors.setPWM(THMBCHANNEL, 0 , MOTORMAX)
#    motors.setPWM(FORECHANNEL, 0 , MOTORMAX)
#    motors.setPWM(MIDCHANNEL, 0 , MOTORMAX)







motors.setPWMFreq(60)
# Set frequency to 60 Hz

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  
# pwm.setPWM(0, 0, servoMin)
# time.sleep(1)

#timeinput= input('Enter the duration (s)')
#fingerinput=input('Select which finger you want to move: 1=thumb, 2=index, 3=middle, 4=all, 5=reverse motors')
#forwardOrReverse=input('Select foward=0, reverse=1')

x=0
on=4096
off=0

button_press = GPIO.input(7)

#if button_press==False:
#        print('Stopping now')
#        motors.setPWM(FORECHANNEL, 0 , MOTORMAX)
#        time.sleep(1)

#if int(fingerinput)==1:
#    if int(forwardOrReverse)==0:
#        finger1forward(timeinput)
#    if int(forwardOrReverse)==1:
#        finger1reverse(timeinput)
#    #if button_press==False:
#        #print('Stopping now')
#        #pwm.setPWM(0, 0 , 4096)
#        #time.sleep(1)
#if int(fingerinput)==2:
#    if int(forwardOrReverse)==0:
#        finger2forward(timeinput)
#    if int(forwardOrReverse)==1:
#        finger2reverse(timeinput)
#    
#if int(fingerinput)==3:
#    if int(forwardOrReverse)==0:
#        finger3forward(timeinput)
##    if int(forwardOrReverse)==1:
 ##       finger3reverse(timeinput)
  #  
#if int(fingerinput)==4:
#    
#    allforward(timeinput)
#    
#if int(fingerinput)==5:
#    allreverse(timeinput)

def getPatientName():
    return 'John Doe'

def getPatientAge():
    return '25'

def getPatientGender():
    return 'male'

def getDate():
    curdate=datetime.date.today()
    curday=curdate.day
    curmon=curdate.month
    curyea=curdate.year
    return str(curmon)+ '/' + str(curday) + '/' + str(curyea)

def getTrialNum():
    return 1


class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self)
        self.grid()
        self.winfo_toplevel().title("Hand Exoskeleton")
        self.create_info()
        self.create_forceinput()
        self.create_actionpanel()
        self.create_rompanel()
        self.create_romgraph()
        self.create_handpos()

    def create_info(self):
        infoframe=tk.LabelFrame(root,text="Patient Information:")
        infoframe.grid(row=0,column=0,sticky='nsew')
        infoframe.columnconfigure(0,weight=1)
        
        PN=tk.StringVar()
        self.PatientName=tk.Label(master=infoframe, textvariable=PN)
        PN.set('Patient: ' + getPatientName())
        self.PatientName.grid(row=0,column=0,sticky='w')
        
        DT=tk.StringVar()
        self.DateTime=tk.Label(master=infoframe, textvariable=DT)
        DT.set('Date: ' + getDate())
        self.DateTime.grid(row=1,column=0,sticky='w')
        
        PG=tk.StringVar()
        self.PatientGender=tk.Label(master=infoframe, textvariable=PG)
        PG.set('Gender: ' + getPatientGender())
        self.PatientGender.grid(row=2,column=0,sticky='w')
        
        PA=tk.StringVar()
        self.PatientGender=tk.Label(master=infoframe, textvariable=PA)
        PA.set('Age: ' + getPatientAge())
        self.PatientGender.grid(row=3,column=0,sticky='w')

        TN=tk.StringVar()
        self.PatientGender=tk.Label(master=infoframe, textvariable=TN)
        TN.set('Trial: ' + str(getTrialNum()))
        self.PatientGender.grid(row=4,column=0,sticky='w')
        
        #self.hi_there = tk.Button(self)
        #self.hi_there["text"] = "Hello World\n(click me)"
        #self.hi_there["command"] = self.say_hi
        #elf.hi_there.grid(row=0,column=2,sticky='E')

        #self.quit = tk.Button(self, text="QUIT", fg="red",
        #                      command=root.destroy)
        #self.quit.grid(row=1,column=2,sticky='E')

        #frame = tk.Frame(root)
        #Label(master, text="First").grid(row=0, sticky=W)
        #bottomframe = tk.Frame(root)
    def create_forceinput(self):

        forceinputframe=tk.LabelFrame(root,text='Device tension:')
        forceinputframe.grid(row=1,column=0,sticky='nsew')
        forceinputframe.columnconfigure(0,weight=1)
        forceinputframe.columnconfigure(1,weight=1)
        forceinputframe.columnconfigure(2,weight=1)
        forceinputframe.columnconfigure(3,weight=1)
        forceinputframe.columnconfigure(4,weight=1)
        forceinputframe.columnconfigure(5,weight=1)



        thumblabeltxt=tk.StringVar()
        thumbforceval=tk.IntVar()
        thumblabel=tk.Label(forceinputframe,textvariable=thumblabeltxt).grid(row=0,column=0)
        thumblabeltxt.set('Thumb')
        thumbradio1=tk.Radiobutton(forceinputframe,text="1", variable = thumbforceval, value=1).grid(row=0,column=1)
        thumbradio2=tk.Radiobutton(forceinputframe,text="2", variable = thumbforceval, value=2).grid(row=0,column=2)
        thumbradio3=tk.Radiobutton(forceinputframe,text="3", variable = thumbforceval, value=3).grid(row=0,column=3)
        thumbradio4=tk.Radiobutton(forceinputframe,text="4", variable = thumbforceval, value=4).grid(row=0,column=4)
        thumbradio5=tk.Radiobutton(forceinputframe,text="5", variable = thumbforceval, value=5).grid(row=0,column=5)
       

        indexlabeltxt=tk.StringVar()
        indexforceval=tk.IntVar()
        indexlabel=tk.Label(forceinputframe,textvariable=indexlabeltxt).grid(row=1,column=0)
        indexlabeltxt.set('Index')
        indexradio1=tk.Radiobutton(forceinputframe,text="1", variable = indexforceval, value=1).grid(row=1,column=1)
        indexradio2=tk.Radiobutton(forceinputframe,text="2", variable = indexforceval, value=2).grid(row=1,column=2)
        indexradio3=tk.Radiobutton(forceinputframe,text="3", variable = indexforceval, value=3).grid(row=1,column=3)
        indexradio4=tk.Radiobutton(forceinputframe,text="4", variable = indexforceval, value=4).grid(row=1,column=4)
        indexradio5=tk.Radiobutton(forceinputframe,text="5", variable = indexforceval, value=5).grid(row=1,column=5)

        middlelabeltxt=tk.StringVar()
        middleforceval=tk.IntVar()
        middlelabel=tk.Label(forceinputframe,textvariable=middlelabeltxt).grid(row=2,column=0)
        middlelabeltxt.set('Thumb')
        middleradio1=tk.Radiobutton(forceinputframe,text="1", variable = middleforceval, value=1).grid(row=2,column=1)
        middleradio2=tk.Radiobutton(forceinputframe,text="2", variable = middleforceval, value=2).grid(row=2,column=2)
        middleradio3=tk.Radiobutton(forceinputframe,text="3", variable = middleforceval, value=3).grid(row=2,column=3)
        middleradio4=tk.Radiobutton(forceinputframe,text="4", variable = middleforceval, value=4).grid(row=2,column=4)
        middleradio5=tk.Radiobutton(forceinputframe,text="5", variable = middleforceval, value=5).grid(row=2,column=5)

    def f1for(self):
        global f1forwardfreq
        print(string(f1forwardfreq))
    def f1rev(self):
        global f1reversefreq
        print(string(f1reversefreq))


    def create_actionpanel(self):
        actionframe=tk.Frame(root)
        actionframe.grid(row=2,column=0,sticky='nsew')
        actionframe.columnconfigure(0,weight=1)        
        
        f1ftxt=tk.StringVar()
        f1fbtn=tk.Button(actionframe,textvariable=f1ftxt,command=f1for).grid(row=0,column=0)
        f1ftxt.set('F1forward')

        f1rtxt=tk.StringVar()
        f1rbtn=tk.Button(actionframe,textvariable=starttxt,command=f1rev).grid(row=0,column=1)
        starttxt.set('F1reverse')

        starttxt=tk.StringVar()
        startbtn=tk.Button(actionframe,textvariable=starttxt).grid(row=0,column=2)
        starttxt.set('F1for')

        stoptxt=tk.StringVar()
        stopbtn=tk.Button(actionframe,textvariable=stoptxt).grid(row=1,column=3)
        stoptxt.set('F2rev')

        
    def create_rompanel(self):
        romframe=tk.LabelFrame(root,text='Range of Motion:')
        romframe.grid(row=0,column=1,sticky='nsew')
        romframe.columnconfigure(0,weight=1)
        romframe.rowconfigure(0,weight=1)
        romslider = tk.Scale(romframe, from_=0, to=100, orient=tk.HORIZONTAL,length=400)
        romslider.grid(column=0,row=0,sticky='nsew')
    def update_f1f(self,value):
        f1forwardfreq=value
    def update_f1r(self,value):
        f1reversefreq=value
    def update_f2f(self,value):
        f2forwardfreq=value
    def update_f2r(self,value):
        f2reversefreq=value
    def update_f3f(self,value):
        f3forwardfreq=value
    def update_f3r(self,value):
        f3reversefreq=value

    def create_romgraph(self):
        graphframe=tk.Frame(root)
        graphframe.grid(row=1,column=1,sticky='nsew')
        graphframe.columnconfigure(0,weight=1)
        graphframe.rowconfigure(0,weight=1)
        f1fslider = tk.Scale(graphframe, from_=0, to=4096, orient=tk.HORIZONTAL,length=400, command=update_f1f)
        f1fslider.grid(column=0,row=0,sticky='nsew')
        f2fslider = tk.Scale(graphframe, from_=0, to=4096, orient=tk.HORIZONTAL,length=400, command=update_f1r)
        f2fslider.grid(column=0,row=1,sticky='nsew')
        f3fslider = tk.Scale(graphframe, from_=0, to=4096, orient=tk.HORIZONTAL,length=400, command=update_f2f)
        f3fslider.grid(column=0,row=2,sticky='nsew')
        f1rslider = tk.Scale(graphframe, from_=0, to=4096, orient=tk.HORIZONTAL,length=400, command=update_f2r)
        f1rslider.grid(column=0,row=3,sticky='nsew')
        f2rslider = tk.Scale(graphframe, from_=0, to=4096, orient=tk.HORIZONTAL,length=400, command=update_f3f)
        f2rslider.grid(column=0,row=4,sticky='nsew')
        f3rslider = tk.Scale(graphframe, from_=0, to=4096, orient=tk.HORIZONTAL,length=400, command=update_f3r)
        f3rslider.grid(column=0,row=5,sticky='nsew')
        #f=Figure(figsize=(3,3),dpi=100)
        #a=f.add_subplot(111)
        #a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        #canvas = FigureCanvasTkAgg(f, graphframe)
        #canvas.show()
        #canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        #toolbar = NavigationToolbar2TkAgg(canvas, self)
        #toolbar.update()
        #canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def create_handpos(self):
        handposframe=tk.Frame(root)
        handposframe.grid(row=2,column=1,sticky='nsew')
        #logo = tk.PhotoImage(file="indexfinger.png")
        #im1 = tk.Label(handposframe, image=logo).grid(row=0,column=0)
        #im2 = tk.Label(handposframe, image=logo).grid(row=0,column=1)
        #im3 = tk.Label(handposframe, image=logo).grid(row=0,column=2)
        #im1 = tk.Label(handposframe, image=logo).pack(side='left',fill=tk.BOTH,expand=True)
        
        #im2 = tk.Label(handposframe, image=logo).pack(side='left',fill=tk.BOTH,expand=True)
        
        #im3 = tk.Label(handposframe, image=logo).pack(side='left',fill=tk.BOTH,expand=True)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
