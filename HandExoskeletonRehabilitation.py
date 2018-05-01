import tkinter as tk
import datetime
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

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
    def __init__(self, master=None):
        super().__init__(master)
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

    def create_actionpanel(self):
        actionframe=tk.Frame(root)
        actionframe.grid(row=2,column=0,sticky='nsew')
        actionframe.columnconfigure(0,weight=1)        
        
        starttxt=tk.StringVar()
        startbtn=tk.Button(actionframe,textvariable=starttxt).grid(row=0,column=0)
        starttxt.set('Start Procedure')

        stoptxt=tk.StringVar()
        stopbtn=tk.Button(actionframe,textvariable=stoptxt).grid(row=1,column=0)
        stoptxt.set('Stop Procedure')

        savetxt=tk.StringVar()
        savebtn=tk.Button(actionframe,textvariable=savetxt).grid(row=3,column=0)
        savetxt.set('Save')
        
    def create_rompanel(self):
        romframe=tk.LabelFrame(root,text='Range of Motion:')
        romframe.grid(row=0,column=1,sticky='nsew')
        romframe.columnconfigure(0,weight=1)
        romframe.rowconfigure(0,weight=1)
        romslider = tk.Scale(romframe, from_=0, to=100, orient=tk.HORIZONTAL,length=400)
        romslider.grid(column=0,row=0,sticky='nsew')

    def create_romgraph(self):
        graphframe=tk.Frame(root)
        graphframe.grid(row=1,column=1,sticky='nsew')
        f=Figure(figsize=(3,3),dpi=100)
        a=f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        canvas = FigureCanvasTkAgg(f, graphframe)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        #toolbar = NavigationToolbar2TkAgg(canvas, self)
        #toolbar.update()
        #canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def create_handpos(self):
        handposframe=tk.Frame(root)
        handposframe.grid(row=2,column=1,sticky='nsew')
        logo = tk.PhotoImage(file="indexfinger.png")
        #im1 = tk.Label(handposframe, image=logo).grid(row=0,column=0)
        #im2 = tk.Label(handposframe, image=logo).grid(row=0,column=1)
        #im3 = tk.Label(handposframe, image=logo).grid(row=0,column=2)
        im1 = tk.Label(handposframe, image=logo).pack(side='left',fill=tk.BOTH,expand=True)
        
        im2 = tk.Label(handposframe, image=logo).pack(side='left',fill=tk.BOTH,expand=True)
        
        im3 = tk.Label(handposframe, image=logo).pack(side='left',fill=tk.BOTH,expand=True)
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()
