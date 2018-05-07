#!/usr/bin/python
import Tkinter as tk
import dialog as dlg
import datetime
import csv
from Raspi_PWM_Servo_Driver import PWM
import time
import RPi.GPIO as GPIO

#a=[]
#with open('test.csv', newline='') as csvfile:
#    myreader=csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in myreader:
#        a.append(row)

#print(a[0:3][0:2])

#['Teacher']
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN
)           #, pull_up_down=GPIO.PUD_UP)
global pwm, SERVOMAXFREQ, INDEXCHANNEL, MIDDLECHANNEL, THUMBCHANNEL

THUMBCHANNEL=0
INDEXCHANNEL=1
MIDDLECHANNEL=15

SERVOMAXFREQ=4096
pwm = PWM(0x70)# Initialise the PWM device using the default address bmp = PWM(0x40, debug=True)

def getPatientName():
    return 'John Doe'

def getPatientAge():
    return '25'

def getPatientGender():
    return 'male'

def getDate():
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    curdate=datetime.date.today()
    curday=curdate.day
    curmon=curdate.month
    curyea=curdate.year
    return months[curmon-1] + ' ' + str(curday) + ', ' + str(curyea)

def getTrialNum():
    return 1

def onefingerstart(finger,time,freq):
    if finger == 0:
        motorchannel=THUMBCHANNEL
    elif finger ==1:
        motorchannel=INDEXCHANNEL
    elif finger ==2:
        motorchannel=MIDDLECHANNEL
    else:
        raise ValueError

    elapsed=0
    while (elapsed<time):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(motorchannel, 0, freq)#going foward
        time.sleep(1)
            
            #print('Stopping now '+ str(x))
            
            #while button_press == False:
            #   button_press = GPIO.input(7)
        elapsed=elapsed+1   #counter
    pwm.setPWM(motorchannel, 0 , 4096)#shut off

def twofingerstart(finger1,finger2,time,freq1,freq2):
    if finger1 ==0:
        motorchannel1=THUMBCHANNEL
    elif finger1==1:
        motorchannel1=INDEXCHANNEL
    elif finger1==2:
        motorchannel1=MIDDLECHANNEL
    else:
        raise ValueError
    if finger2 == 0:
        motorchannel2=THUMBCHANNEL
    elif finger2 == 1:
        motorchannel2=INDEXCHANNEL
    elif finger2 == 2:
        motorchannel2=MIDDLECHANNEL
    else:
        raise ValueError

    elapsed=0
    while (elapsed<time):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(motorchannel1, 0, freq1)#going foward
        pwm.setPWM(motorchannel2, 0, freq2)#going 
        time.sleep(1)
            
            #print('Stopping now '+ str(x))
            
            #while button_press == False:
            #   button_press = GPIO.input(7)
        elapsed=elapsed+1   #counter
    pwm.setPWM(motorchannel1, 0 , 4096)#shut off
    pwm.setPWM(motorchannel2, 0 , 4096)#shut off


def threefingerstart(time,freqthumb,freqind,freqmiddle):

    elapsed=0
    while (elapsed<time):#duration
        button_press = GPIO.input(7)
        pwm.setPWM(THUMBCHANNEL, 0, freqthumb)#going foward
        pwm.setPWM(INDEXCHANNEL, 0, freqind)#going 
        pwm.setPWM(MIDDLECHANNEL, 0, freqmiddle)#going 
        time.sleep(1)
            
            #print('Stopping now '+ str(x))
            
            #while button_press == False:
            #   button_press = GPIO.input(7)
        elapsed=elapsed+1   #counter
    pwm.setPWM(THUMBCHANNEL, 0 , 4096)#shut off
    pwm.setPWM(INDEXCHANNEL, 0 , 4096)#shut off
    pwm.setPWM(MIDDLECHANNEL, 0 , 4096)#shut off

def startprocedure():
    global thumbforceval, middleforceval, indexforceval, thumbdirval, indexdirval, middledirval
    forwardfreq=[410, 420, 430, 440, 450]
    reversefreq=[280, 290, 300, 310, 320]
    isthumbforward=thumbdirval.get()
    isindexforward=indexdirval.get()
    ismiddleforward=middledirval.get()

    if isthumbforward+isindexforward+ismiddleforward == 3:
        threefingerstart(1,forwardfreq[thumbforceval.get()],forwardfreq[indexforceval.get()],forwardfreq[middleforceval.get()])
    elif isthumbforward+isindexforward+ismiddleforward == 2:
        if isthumbforward ==0:
            twofingerstart(1,2,1,forwardfreq[indexforceval.get()],forwardfreq[middleforceval.get()])
        elif isindexforward == 0:
            twofingerstart(0,2,1,forwardfreq[thumbforceval.get()],forwardfreq[middleforceval.get()])
        else:
            twofingerstart(0,1,1,forwardfreq[thumbforceval.get()],forwardfreq[indexforceval.get()])
    elif isthumbforward+isindexforward+ismiddleforward == 1:
        if isthumbforward == 1:
            onefingerstart(0,1,forwardfreq[thumbforceval.get()])
        elif isindexforward == 1:
            onefingerstart(1,1,forwardfreq[indexforceval.get()])
        elif ismiddleforward == 1:
            onefingerstart(2,1,forwardfreq[middleforceval.get()])
    else:
        return

def stopprocedure():
    pwm = PWM(0x70)# Initialise the PWM device using the default address bmp = PWM(0x40, debug=True)

def inputpatientinfocallback():
    global PN,PG,PA,TN
    patientinfoinput=dlg.InputDialog(root,'Input patient session info:')
    if len(patientinfoinput.result)==4:
        PN.set('Patient: ' + patientinfoinput.result['PatientName'])
        PA.set('Age: ' + patientinfoinput.result['PatientAge'])
        PG.set('Gender: ' + patientinfoinput.result['PatientGender'])
        TN.set('Trial: ' + patientinfoinput.result['TrialNum'])

def printromval():
    global romvar
    strromvar=str(romvar.get())
    print(strromvar)


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.winfo_toplevel().title("Hand Exoskeleton")
        self.create_info()
        self.create_forceinput()
        self.create_actionpanel()
        self.create_rompanel()

    def create_info(self):
        global PN,PA,TN,PG
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
        
        inputpatientinfotxt=tk.StringVar()
        inputpatientinfo=tk.Button(master=infoframe, command=inputpatientinfocallback, textvariable=inputpatientinfotxt).grid(row=4,column=1)
        inputpatientinfotxt.set('Input patient information')
        
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
        global thumbforceval, indexforceval, middleforceval
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

    def create_directionpanel(self):
        global thumbdirval, indexdirval, middledirval
        directionframe=tk.Frame(root)
        directionframe.grid(row=3,column=0,sticky='nsew')
        directionframe.columnconfigure(0,weight=1)      
        forwardlabeltxt=tk.StringVar()
        forwardlabel=tk.Label(directionframe,textvariable=forwardlabeltxt).grid(row=0,column=1)
        forwardlabeltxt.set('Forward')
        
        offlabeltxt=tk.StringVar()
        offlabel=tk.Label(directionframe,textvariable=offlabeltxt).grid(row=0,column=2)
        offlabeltxt.set('Off')

        thumbdirlabeltxt=tk.StringVar()
        thumbdirlabel=tk.Label(directionframe,textvariable=thumbdirlabeltxt).grid(row=1,column=0)
        thumbdirlabeltxt.set('Thumb')

        indexlabeltxt=tk.StringVar()
        indexlabel=tk.Label(directionframe,textvariable=indexlabeltxt).grid(row=2,column=0)
        indexlabeltxt.set('Index')

        middlelabeltxt=tk.StringVar()
        middlelabel=tk.Label(directionframe,textvariable=middlelabeltxt).grid(row=0,column=2)
        middlelabeltxt.set('Middle')

        thumbdirval=tk.IntVar()
        thumbforwardradio=tk.Radiobutton(directionframe,text="", variable = thumbdirval, value=1).grid(row=1,column=1)
        thumboffradio=tk.Radiobutton(directionframe,text="", variable = thumbdirval, value=0).grid(row=1,column=2)

        indexdirval=tk.IntVar()
        indexforwardradio=tk.Radiobutton(directionframe,text="", variable = indexdirval, value=1).grid(row=2,column=1)
        indexoffradio=tk.Radiobutton(directionframe,text="", variable = indexdirval, value=0).grid(row=2,column=2)

        middledirval=tk.IntVar()
        middleforwardradio=tk.Radiobutton(directionframe,text="", variable = middledirval, value=1).grid(row=3,column=1)
        middleoffradio=tk.Radiobutton(directionframe,text="", variable = middledirval, value=0).grid(row=3,column=2)        

    def create_actionpanel(self):
        actionframe=tk.Frame(root)
        actionframe.grid(row=4,column=0,sticky='nsew')
        actionframe.columnconfigure(0,weight=1)        
        
        starttxt=tk.StringVar()
        startbtn=tk.Button(actionframe,textvariable=starttxt,command=startprocedure).grid(row=0,column=0)
        starttxt.set('Start Procedure')

        stoptxt=tk.StringVar()
        stopbtn=tk.Button(actionframe,textvariable=stoptxt, command=stopprocedure).grid(row=1,column=0)
        stoptxt.set('Stop Procedure')

        savetxt=tk.StringVar()
        savebtn=tk.Button(actionframe,textvariable=savetxt).grid(row=3,column=0)
        savetxt.set('Save')
        
    def create_rompanel(self):
        global romvar
        romframe=tk.LabelFrame(root,text='Range of Motion:')
        romframe.grid(row=2,column=0,sticky='nsew')
        romframe.columnconfigure(0,weight=1)
        romframe.rowconfigure(0,weight=1)
        romvar=tk.IntVar()
        romslider = tk.Scale(romframe, variable=romvar, from_=0, to=100, orient=tk.HORIZONTAL,length=400)
        romslider.grid(column=0,row=0,sticky='nsew')

    # def create_romgraph(self):
    #     graphframe=tk.Frame(root)
    #     graphframe.grid(row=1,column=1,sticky='nsew')

    #     #toolbar = NavigationToolbar2TkAgg(canvas, self)
    #     #toolbar.update()
    #     #canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # def create_handpos(self):
    #     handposframe=tk.Frame(root)
    #     handposframe.grid(row=2,column=1,sticky='nsew')

        

root = tk.Tk()
app = Application(master=root)
app.mainloop()
