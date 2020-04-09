#import all necessary library
from tkinter import *
from tkinter import filedialog
import os
import sys
import webbrowser
from tkinter import messagebox

path=os.getcwd()
print("current path : "+path)
os.chdir(path)

root=Tk()
root.title("HUMAN ACTIVITY RECOGNIZATION")
root.geometry("800x400")
root.config(bg="blue")
label1=Label(root,text="Human Activity Recognition",bg="red",fg="white",width=89,justify="center")
label1.config(font=('times',12,'bold'))
label1.place(x=0,y=0)
label2=Label(root,text="File Name: ",bg="blue",fg="black",width=20)
label2.config(font=('times',13,'bold'))
label2.place(x=0,y=310)
label0=Label(root,text="[No File Selected]",bg="white",fg="black",width=60)
label0.config(font=('times',10,'bold'))
label0.place(x=160,y=310)
photo=PhotoImage(file="activity_recognition_1.png")
labelb=Label(root,image=photo,relief=RAISED)
labelb.image=photo
labelb.place(x=22,y=30)

def aboutDataset():
    messagebox.showinfo('[INFO]',"INTERNET REQUIRED!!")
    print("Kinetics400 dataset used")
    # opening dataset website using python need net
    webbrowser.open('https://deepmind.com/research/open-source/kinetics')    

def aboutUs():
    window3=Tk()
    window3.title("steps To Run")
    T3 = Text(window3, height=10, width=60)
    T3.config(bg='orange')
    T3.configure(font='times 12')
    T3.pack()
    T3.insert(INSERT,"WORK BY :: \n")
    T3.insert(END,"\n\t[Ch. Vinay Kumar --  11716840]\n")
    T3.insert(END,"\n\t[K.Sai Chand --  11706932]\n")
    T3.insert(END,"\n\t[K. Snehith Reddy -- 11709185]")
    
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="INFO", menu=filemenu)
filemenu.add_command(label="About Dataset", command=aboutDataset)
filemenu.add_separator()
filemenu.add_command(label="About us", command=aboutUs)

def stepsToRun():
    window2=Tk()
    window2.title("steps To Run")
    T2 = Text(window2, height=10, width=60)
    T2.config(bg='orange')
    T2.configure(font='times 12')
    T2.pack()
    T2.insert(INSERT,"\n1) Click Browse a File Button\n\n")
    T2.insert(END,"2) Select a Video File from you local drive with extension .mp4 \n\t[NOTE: the video show be at atleast 50 sec long]\n\n")
    T2.insert(END,"3) Click on Start Predection button\n\n")
    T2.insert(END,"4) To Stop just close the command prompt \n\n")
    window2.mainloop()
def stepsToViewModel():
    window1=Tk()
    window1.title("steps To View Model Architecture")
    T = Text(window1, height=13, width=60)
    T.configure(font='times 12')
    T.config(bg='orange')
    T.pack()
    T.insert(INSERT,"\n1) Click on View Model Architecture Button\n\n")
    T.insert(END,"2) You will be directed to a netron website [INFO: needed net connectivity]\n\n")
    T.insert(END,"3) Click on OpenModel.. button\n\n")
    T.insert(END,"4) Select resnet-34_kinetics.onnx model\n\n")
    T.insert(END,"5) You will see the architecture of the model used\n\n")
    T.insert(END,"\t[Netron is used to visualize the model architecture]")
    window1.mainloop()

helpmenu = Menu(menu)    
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="How To Run",command=stepsToRun)
helpmenu.add_separator()
helpmenu.add_command(label="How To View Model Architecture",command=stepsToViewModel)

filepath=""


def openFile():
    global filepath
    filepath=filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("video Files","*.mp4"),("All Files","*.*")))    
    label0.config(text=filepath)
    if(filepath==""):
        label0.config(text="[No File Selected]")
    print(filepath)


def startPrediction():
    print("in start prediction: ",filepath)
    # running command using cmd from python
    command="python human_activity_recognition.py --model resnet-34_kinetics.onnx --classes action_recognition_kinetics.txt --input "+filepath 
    os.system('cmd /k "'+str(command)+'"')    
    
button0=Button(root,text="Browse a File",bg="red",fg="white",activebackground="green",width=20,command=openFile)
button0.config(font=('times',10,'bold'))
button0.place(x=600,y=310)

button1=Button(root,text="Start Prediction",bg="red",fg="white",activebackground="green",width=20,command=startPrediction)
button1.config(font=('times',10,'bold'))
button1.place(x=380,y=350)
def destroy():
    root.destroy()
    print("command: exit")
button2=Button(root,text="Exit",bg="red",fg="white",activebackground="green",width=20,command=destroy)
button2.config(font=('times',10,'bold'))
button2.place(x=600,y=350)
def architectureModel():
    messagebox.showinfo('[INFO]',"INTERNET REQUIRED!! ")
    # opening netron for model visualization using python need net
    webbrowser.open('https://lutzroeder.github.io/netron/')
button3=Button(root,text="View Model  Architecture ",bg="red",fg="white",activebackground="green",width=40,command=architectureModel)
button3.config(font=('times',10,'bold'))
button3.place(x=30,y=350)
root.mainloop()
