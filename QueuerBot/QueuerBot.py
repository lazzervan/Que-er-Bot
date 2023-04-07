#!/usr/bin/python

import pathlib
import cv2
import numpy as np
import face_recognition
import tkthread; tkthread.patch() 
import tkinter as tk
import os
import threading
import time
import pyttsx3
import evdev
import mysql.connector
from time import strftime
from helpbox import *
from tkinter import *
from PIL import Image, ImageTk
from gpiozero import Button
#requirements for rpi
#sudo install cmake and dlib wheel for the face_recognition lib
#sudo apt update && sudo apt install espeak ffmpeg libespeak1

#################NOTENTOENOTENOTE READ PLSSS, i set the hdmi to sound mode in config.txt revert after using VGA monitor tyty uwu
##specifically uncommented the hdmi group=1 and hdmi drive=2, comment back if it causes error in future 
#PHYSICAL BUTTONS
#from signal import pause

#admin var
totalserve = 0


#queue ui var
qid = 0
rid = 0
timerrunning = False
someonedequed = False
firstinque = None
lastinque = None
idnow = None
passed = False
tagaloglang = False

#simulation var
simid = 0 

#face register lib
tid = 0
imgvar = "testimage.jpg"
nextimgvar = None
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
mydir = r'/home/zhed/Documents/QueuerBot/dataset'

#Front Window
root = tk.Tk()
#root.geometry("1280x700+1500+30") #for second screen
root.geometry("1280x900+0+50")
root.title("Que'er Bot")

#Now Serving UI
imgframe = Frame (root, width=600, height=600)
imgframe.place(x=10, y=48)

nimgframe = Frame (root, width=600, height=600)
nimgframe.place(x=310, y=440)


oobqueue = [] 
class Queue:
    global oobqueue   
    
    def __init__(self):
        self.queue=[]
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    def display(self):
        print(self.queue)
    def size(self):
        return len(self.queue) 
        

    def reg():
        blackout()
        global qid, rid
        print("rid is")
        qid += 1
        q.enqueue(qid)
        rid +=1
        print(rid)
        if rid < 21:
            if rid == 1:
                slot1.set(qid)
            elif rid == 2:
                slot2.set(qid)
            elif rid == 3:
                slot3.set(qid)
            elif rid == 4:
                slot4.set(qid)
            elif rid == 5:
                slot5.set(qid)
            elif rid == 6:
                slot6.set(qid)
            elif rid == 7:
                slot7.set(qid)
            elif rid == 8:
                slot8.set(qid)
            elif rid == 9:
                slot9.set(qid)
            elif rid == 10:
                slot10.set(qid)
            elif rid == 11:
                slot11.set(qid)
            elif rid == 12:
                slot12.set(qid)
            elif rid == 13:
                slot13.set(qid)
            elif rid == 14:
                slot14.set(qid)
            elif rid == 15:
                slot15.set(qid)
            elif rid == 16:
                slot16.set(qid)
            elif rid == 17:
                slot17.set(qid)
            elif rid == 18:
                slot18.set(qid)
            elif rid == 19:
                slot19.set(qid)
            elif rid == 20:
                slot20.set(qid)
        elif rid > 20:
            oobqueue.append(qid)
            print(oobqueue)
        nextpic()
                
    
    def deq():
        blackout()
        global qid, rid, someonedequed,totalserve
        someonedequed = True
        rid -=1
        totalserve +=1
        time.sleep(.5)
        someonedequed = False
        if not oobqueue:

            if rid == 0:
                slot1.set("EMPTY SLOT")
            elif rid >= 1 and rid < 21:
                slot1.set(slot2.get())
                slot2.set(slot3.get())
                slot3.set(slot4.get())
                slot4.set(slot5.get())
                slot5.set(slot6.get())
                slot6.set(slot7.get())
                slot7.set(slot8.get())
                slot8.set(slot9.get())
                slot9.set(slot10.get())
                slot10.set(slot11.get())
                slot11.set(slot12.get())
                slot12.set(slot13.get())
                slot13.set(slot14.get())
                slot14.set(slot15.get())
                slot15.set(slot16.get())
                slot16.set(slot17.get())
                slot17.set(slot18.get())
                slot18.set(slot19.get())
                slot19.set(slot20.get())
                slot20.set("EMPTY SLOT")
            else:
                pass
            
            
                
        elif oobqueue:
            oobslot = str(oobqueue.pop(0))
            slot1.set(slot2.get())
            slot2.set(slot3.get())
            slot3.set(slot4.get())
            slot4.set(slot5.get())
            slot5.set(slot6.get())
            slot6.set(slot7.get())
            slot7.set(slot8.get())
            slot8.set(slot9.get())
            slot9.set(slot10.get())
            slot10.set(slot11.get())
            slot11.set(slot12.get())
            slot12.set(slot13.get())
            slot13.set(slot14.get())
            slot14.set(slot15.get())
            slot15.set(slot16.get())
            slot16.set(slot17.get())
            slot17.set(slot18.get())
            slot18.set(slot19.get())
            slot19.set(slot20.get())
            slot20.set(oobslot)
            
        if rid == 1:
            print("pass")
        elif rid != 1:
            nextpic()
        q.dequeue()

q = Queue()
q.display()

def callinline():
    global firstinque, lastinque
    firstinque = str(slot1.get())
    lastq10 = str(slot10.get())
    lastq9 = str(slot9.get())
    lastq8 = str(slot8.get())
    lastq7 = str(slot7.get())
    lastq6 = str(slot6.get())
    lastq5 = str(slot5.get())
    lastq4 = str(slot4.get())
    lastq3 = str(slot3.get())
    lastq2 = str(slot2.get())
    

    if lastq2 == "EMPTY SLOT":
        pass
    elif lastq2 != "EMPTY SLOT":
        lastinque = str(slot2.get())
    if lastq3 == "EMPTY SLOT":
        pass
    elif lastq3 != "EMPTY SLOT":
        lastinque = str(slot3.get())
    if lastq4 == "EMPTY SLOT":
        pass
    elif lastq4 != "EMPTY SLOT":
        lastinque = str(slot4.get())
    if lastq5 == "EMPTY SLOT":
        pass
    elif lastq5 != "EMPTY SLOT":
        lastinque = str(slot5.get())
    if lastq6 == "EMPTY SLOT":
        pass
    elif lastq6 != "EMPTY SLOT":
        lastinque = str(slot6.get())
    if lastq7 == "EMPTY SLOT":
        pass
    elif lastq7 != "EMPTY SLOT":
        lastinque = str(slot7.get())
    if lastq8 == "EMPTY SLOT":
        pass
    elif lastq8 != "EMPTY SLOT":
        lastinque = str(slot8.get())
    if lastq9 == "EMPTY SLOT":
        pass
    elif lastq9 != "EMPTY SLOT":
        lastinque = str(slot9.get())

    if lastq10 == "EMPTY SLOT":
        pass
    elif lastq10 != "EMPTY SLOT":
        lastinque = str(slot10.get())       
    
#OPTIONAL AND EXPERIMENTAL CALLER
def caller():
    global engine
    engine = pyttsx3.init()
    missingpersoncall = str(slot1.get())
    slotisempty = str(slot1.get())
    
    while True:
        global calls,nagnext, firstinque, lastinque
        callinline()
        nagnext = False
        calls = 0
        missingpersoncall = str(slot1.get())
        slotisempty = str(slot1.get())
        time.sleep(3)


        if timerrunning == True and slotisempty != "EMPTY SLOT" and str(slot2.get()) != "EMPTY SLOT":
            engine.stop()
            engine.setProperty("rate",100)
            tts = ("Calling Queue I dees" + firstinque + "to" + lastinque + "to get ready.")
            engine.say(tts)
            engine.runAndWait()
            time.sleep(10)
        else:
            pass


        if (slotisempty != "EMPTY SLOT" and timerrunning) and nagnext == False:
            missingpersoncall = str(slot1.get())
            if slotisempty == "EMPTY SLOT":
                tts= ""

            elif slotisempty != "EMPTY SLOT":
                engine.setProperty("rate",100)
                tts = ("Calling Queue ID number," + missingpersoncall)
            
            engine.say(tts)
            engine.runAndWait()

            while (calls < 3 and timerrunning and slotisempty != "EMPTY SLOT") and nagnext == False:
                global someonedequed
                someonedequed == False
                time.sleep(8)
                missingpersoncall = str(slot1.get())
                if slotisempty == "EMPTY SLOT":
                    tts= ""
                elif slotisempty != "EMPTY SLOT":
                    engine.setProperty("rate",100)
                    tts = ("Calling Queue ID number," + missingpersoncall)
                engine.say(tts)
                engine.runAndWait()
                calls+=1
                
                if (calls == 3 and slotisempty != "EMPTY SLOT" and timerrunning) and nagnext == False:
                    someonedequed == False
                    time.sleep(8)
                    tts = ("Final call for Queue ID number," + missingpersoncall)
                    engine.stop()
                    engine.say(tts)
                    engine.runAndWait()
                    time.sleep(4)
                    if nagnext == True:
                        break
                    if someonedequed == True:
                        break

                    if nagnext == False or someonedequed == False:
                        time.sleep(4)
                        missedlist()
                        Queue.deq()
                if timerrunning == False or nagnext == True:
                    pass

            if timerrunning == False or nagnext == True:
                pass
        elif timerrunning == False or nagnext == True:
            engine.stop()
            time.sleep(1)

def callerstartthread():
    global callertime
    callertime = threading.Thread(target=caller, daemon = True)


def pausetimer():
    global timerrunning,engine
    timerrunning = False
    engine.stop()
    print("paused")

def unpausetimer():
    global timerrunning
    timerrunning = True
    print("unpaused")
    time.sleep(1)
    timerrunning = True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   

def callpeople():
    global callingpeople, timerrunning
    timerrunning = True
    callingpeople = True
    try:
        callertime.start()
    except:
        print("thread already started")
    
    callingpeople = True
    
  
def warningbox():
    warningframe = Frame(root, background="red")
    warningframe.place(height=100, width=300, x=325, y=100)

    warning = tk.Label(warningframe)
    warning.configure(text = "Warning", fg="white",bg="red", font=('Engravers MT', 14, 'bold'))
    warning.place(x=80)


    warninginfo = tk.Label(warningframe)
    global warningtxt
    warningtxt = tk.StringVar(value="error")
    warninginfo.configure(text= warningtxt, textvariable=warningtxt, fg="white",bg="red",font=('Helvetica', 15))
    warninginfo.place(x=0, y=30)

    global warningque
    warningque=tk.Label(warningframe)
    global warningquetxt
    warningquetxt = tk.StringVar(value='nani')
    warningque.configure(text= warningquetxt, textvariable=warningquetxt, fg="white",bg="red",font=('Helvetica', 24, "bold"))
    warningque.place(x=250, y=35)

    root.after(5000, warningframe.destroy)


def warning1():
    global warningquetxt
    warningbox()
    warningtxt1 = ("You're not next in queue\nYour queue number is: ")
    warningtxt.set(warningtxt1)
    warningquetxt1 = id
    warningquetxt.set(warningquetxt1)

def warning2():
    global warningquetxt
    warningbox()
    warningtxt2 = "You are not registered yet\nPlease register behind the device."
    warningtxt.set(warningtxt2)
    warningque.destroy()
    
def warning3():
    global warningquetxt
    warningbox()
    warningtxt3 = "Scanning Failed\nPlease try again."
    warningtxt.set(warningtxt3)
    warningque.destroy()

def next():
    global nagnext
    izempty = str(slot1.get())
    if izempty != "EMPTY SLOT":
        nagnext= True
        missedlist()
        Queue.deq()
    else:
        pass

npgen = False
def nextpic():
    global npgen
    nid = int(slot1.get())
    nextimgvar = ("dataset/User." + str(nid) + ".15.jpg")
    if issimul == True:
        nextimgvar = ("simulationpic/" + str(nid) + ".png")	
    #global nextimgvar
    openimg = Image.open(nextimgvar)
    resizedimg = openimg.resize((150, 150))#width height
    userimg = ImageTk.PhotoImage (resizedimg)
    if npgen == False:
        global nimglbl
        nimglbl = Label(nimgframe, image = userimg)
        nimglbl.image = userimg
        nimglbl.pack()
        npgen = True
        
    nimglbl.configure(image = userimg)
    nimglbl.image = userimg
    
    # (x=310, y=440)
    nowservimg = tk.Text(root)
    nowservimg.configure(
        background="#06304b",
        font="{Engravers MT} 12 {bold}",
        foreground="#ffffff",
        height=10,
        padx=30,
        pady=4,
        state="disabled",
        width=20)
    _text_ = 'Next'
    nowservimg.configure(state="normal")
    nowservimg.insert("0.0", _text_)
    nowservimg.configure(state="disabled")
    nowservimg.place(
        anchor="nw", x=310, y=425, height = 35,width = 152)
    nowservimg = tk.Frame(root)
    nowservimg.configure(height=20, width=20)

    

def QueueUI():
    global imgvar
    openimg = Image.open(imgvar)
    resizedimg = openimg.resize((300, 300))#width height
    userimg = ImageTk.PhotoImage (resizedimg)
    
    global imglbl
    imglbl = Label(imgframe, image = userimg)
    imglbl.image = userimg
    imglbl.pack()

    nowservimg = tk.Text(root)
    nowservimg.configure(
        background="#06304b",
        font="{Engravers MT} 12 {bold}",
        foreground="#ffffff",
        height=10,
        padx=60,
        pady=4,
        state="disabled",
        width=20)
    _text_ = 'NOW SERVING'
    nowservimg.configure(state="normal")
    nowservimg.insert("0.0", _text_)
    nowservimg.configure(state="disabled")
    nowservimg.place(
        anchor="nw", x=12, y=15, height = 35,width = 300)
    nowservimg = tk.Frame(root)
    nowservimg.configure(height=20, width=20)
    

    queidtext = tk.Label(root)
    global idnow
    idnow = str(tid)
    que = ("QUEUE ID: " + idnow)
    global queidnow
    queidnow = tk.StringVar(value = que)
    queidtext.configure(text= "QUEUE ID: ", fg="white", bg="#06304b", textvariable=queidnow, justify= "center", font=('Engravers MT', 14, 'bold'))
    queidtext.place(x= 12, y= 321)
    
    #####Missed List
    missframe = Frame(root, highlightbackground="#06304b", highlightthickness=2, bg="white")
    missframe.place(height=200, width=300, x=12, y=390)

    miss = tk.Label(missframe)
    miss.configure(text = "MISSING LIST",fg= "black", bg="white", font=('Engravers MT', 14, 'bold'))
    miss.place(x=60)

    global missinfo
    missinfo = tk.Text(missframe)
    missinfo.configure(state="disabled", font=('Helvetica', 14))
    missinfo.place(x=0, y=30, height=165,width=296.2)
    
    
    #####LAST PERSON IN QUEUE
    global queidlast
    last = tk.Label(root)
    quelaststr = ("Last Person in Queue: "+ str(qid))
    queidlast = tk.StringVar(value = quelaststr)
    last.configure(textvariable = queidlast ,bg="#ffce3f", font=('Engravers MT', 16, 'bold'))
    last.place(x=12,y=620)

    ##clock ui
    global clocklbl, clockstr
    clocklbl = tk.Label(root, font=("Engravers MT",21,"bold"), bg="#ffce3f", fg="black")
    clocklbl.place(x=330, y=15,width=250, height = 70)
        
    
    global slot, slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20
    headlist_header = tk.Text(root)
    headlist_header.configure(
        background="#06304b",
        font="{Engravers MT} 12 {bold}",
        foreground="#ffffff",
        height=10,
        padx=38,
        pady=4,
        state="disabled",
        width=50)
    _text_ = 'HEADLIST'
    headlist_header.configure(state="normal")
    headlist_header.insert("0.0", _text_)
    headlist_header.configure(state="disabled")
    headlist_header.place(
        anchor="nw",
        relheight=0.05,
        relwidth=0.201,
        relx=0.771,
        rely=0.02,
        x=0,
        y=0)
    headlist_frame = tk.Frame(root)
    headlist_frame.configure(height=200, width=200)
    separator = tk.Canvas(headlist_frame)
    separator.configure(
        background="#1e1c20",
        highlightbackground="#000000",
        highlightcolor="#4d6af4",
        insertbackground="#4fe6f2",
        selectbackground="#5f7ce2")
    separator.place(
        anchor="nw",
        relheight=0.04,
        relwidth=1.0,
        relx=0.0,
        x=0,
        y=0)
    canvas3 = tk.Canvas(headlist_frame)
    canvas3.configure(
        highlightbackground="#040033",
        highlightcolor="#4d6af4",
        insertbackground="#4fe6f2",
        selectbackground="#5f7ce2")
    canvas3.place(
        anchor="nw",
        relheight=0.95,
        relwidth=1.0,
        relx=0.0,
        rely=0.04,
        x=0,
        y=0)
    headlist_slot1 = tk.Message(headlist_frame)
    slot1 = tk.StringVar(value='EMPTY SLOT')
    headlist_slot1.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot1)
    headlist_slot1.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.046,
        x=0,
        y=0)
    headlist_slot2 = tk.Message(headlist_frame)
    slot2 = tk.StringVar(value='EMPTY SLOT')
    headlist_slot2.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot2)
    headlist_slot2.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.14,
        x=0,
        y=0)
    headlist_slot3 = tk.Message(headlist_frame)
    slot3 = tk.StringVar(value='EMPTY SLOT')
    headlist_slot3.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot3)
    headlist_slot3.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.235,
        x=0,
        y=0)
    headlist_slot4 = tk.Message(headlist_frame)
    slot4 = tk.StringVar(value='EMPTY SLOT')
    headlist_slot4.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot4)
    headlist_slot4.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.33,
        x=0,
        y=0)
    headlist_slot5 = tk.Message(headlist_frame)
    slot5 = tk.StringVar(value='EMPTY SLOT')
    headlist_slot5.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot5)
    headlist_slot5.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.424,
        x=0,
        y=0)
    headlist_slot6 = tk.Message(headlist_frame)
    slot6 = tk.StringVar(value='EMPTY SLOT')
    headlist_slot6.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot6)
    headlist_slot6.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.518,
        x=0,
        y=0)
    headlist_slot7 = tk.Message(headlist_frame)
    slot7 = tk.StringVar(value='EMPTY SLOT')
    headlist_slot7.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot7)
    headlist_slot7.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.612,
        x=0,
        y=0)
    headlist_slot8 = tk.Message(headlist_frame)
    slot8 = tk.StringVar(value='EMPTY SLOT')
    headlist_slot8.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot8)
    headlist_slot8.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.706,
        x=0,
        y=0)
    headlist_slot9 = tk.Message(headlist_frame)
    slot9 = tk.StringVar(value='EMPTY SLOT')
    headlist_slot9.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot9)
    headlist_slot9.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.799,
        x=0,
        y=0)
    headlist_slot10 = tk.Message(headlist_frame)
    slot10 = tk.StringVar(value='EMPTY SLOT')
    headlist_slot10.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot10)
    headlist_slot10.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.893,
        x=0,
        y=0)
    headlist_frame.place(
        anchor="nw",
        relheight=0.88,
        relwidth=0.20,
        relx=0.771,
        rely=0.07,
        x=0,
        y=0)
    taillist_header = tk.Text(root)
    taillist_header.configure(
        background="#06304b",
        font="{Engravers MT} 12 {bold}",
        foreground="#ffffff",
        height=10,
        padx=38,
        pady=4,
        relief="flat",
        setgrid="false",
        state="disabled",
        width=50,)
    _text_ = 'TAIL LIST'
    taillist_header.configure(state="normal")
    taillist_header.insert("0.0", _text_)
    taillist_header.configure(state="disabled")
    taillist_header.place(
        anchor="nw",
        relheight=0.05,
        relwidth=0.201,
        relx=0.5,
        rely=0.02,
        x=0,
        y=0)
    taillist_frame = tk.Frame(root)
    taillist_frame.configure(height=200, width=200)
    canvas4 = tk.Canvas(taillist_frame)
    canvas4.configure(
        background="#1e1c20",
        highlightbackground="#000000",
        highlightcolor="#4d6af4",
        insertbackground="#4fe6f2",
        selectbackground="#5f7ce2")
    canvas4.place(
        anchor="nw",
        relheight=0.04,
        relwidth=1.0,
        relx=0.0,
        x=0,
        y=0)
    canvas5 = tk.Canvas(taillist_frame)
    canvas5.configure(
        highlightbackground="#040033",
        highlightcolor="#4d6af4",
        insertbackground="#4fe6f2",
        selectbackground="#5f7ce2")
    canvas5.place(
        anchor="nw",
        relheight=0.95,
        relwidth=1.0,
        relx=0.0,
        rely=0.04,
        x=0,
        y=0)
    taillist_slot1 = tk.Message(taillist_frame)
    slot11 = tk.StringVar(value='EMPTY SLOT')
    taillist_slot1.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot11)
    taillist_slot1.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.046,
        x=0,
        y=0)
    taillist_slot2 = tk.Message(taillist_frame)
    slot12 = tk.StringVar(value='EMPTY SLOT')
    taillist_slot2.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot12)
    taillist_slot2.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.14,
        x=0,
        y=0)
    taillist_slot3 = tk.Message(taillist_frame)
    slot13 = tk.StringVar(value='EMPTY SLOT')
    taillist_slot3.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot13)
    taillist_slot3.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.235,
        x=0,
        y=0)
    taillist_slot4 = tk.Message(taillist_frame)
    slot14 = tk.StringVar(value='EMPTY SLOT')
    taillist_slot4.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot14)
    taillist_slot4.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.33,
        x=0,
        y=0)
    taillist_slot5 = tk.Message(taillist_frame)
    slot15 = tk.StringVar(value='EMPTY SLOT')
    taillist_slot5.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot15)
    taillist_slot5.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.424,
        x=0,
        y=0)
    taillist_slot6 = tk.Message(taillist_frame)
    slot16 = tk.StringVar(value='EMPTY SLOT')
    taillist_slot6.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot16)
    taillist_slot6.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.518,
        x=0,
        y=0)
    taillist_slot7 = tk.Message(taillist_frame)
    slot17 = tk.StringVar(value='EMPTY SLOT')
    taillist_slot7.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot17)
    taillist_slot7.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.612,
        x=0,
        y=0)
    taillist_slot8 = tk.Message(taillist_frame)
    slot18 = tk.StringVar(value='EMPTY SLOT')
    taillist_slot8.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot18)
    taillist_slot8.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.706,
        x=0,
        y=0)
    taillist_slot9 = tk.Message(taillist_frame)
    slot19 = tk.StringVar(value='EMPTY SLOT')
    taillist_slot9.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot19)
    taillist_slot9.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.799,
        x=0,
        y=0)
    taillist_slot10 = tk.Message(taillist_frame)
    slot20 = tk.StringVar(value='EMPTY SLOT')
    taillist_slot10.configure(
        background="white",
        font=("TkMenuFont","18","bold"),
        justify="center",
        text='EMPTY SLOT',
        textvariable=slot20)
    taillist_slot10.place(
        anchor="nw",
        relheight=0.09,
        relwidth=0.97,
        relx=0.015,
        rely=0.893,
        x=0,
        y=0)
    taillist_frame.place(
        anchor="nw",
        relheight=0.88,
        relwidth=0.20,
        relx=0.5003,
        rely=0.07,
        x=0,
        y=0)
QueueUI()

missedlistarray = np.array([])
def missedlist():
    global missedlistarray, missingperson, missinfo
    print("missed fdsfkdslfdsjlkl")
    missingperson = int(slot1.get())
    izempty = str(slot1.get())
    if izempty != "EMPTY SLOT":
        print("missed list call")
        missedlistarray =np.append(missedlistarray, missingperson)
        print(missedlistarray)
        missinfo.configure(state="normal")
        missinfo.delete('1.0', END)
        #missedlistarraytext = missedlistarray.tostring()
        arraytxt = str(missedlistarray)
        cleantxt = arraytxt.replace('[', '').replace(']','').replace('.','|')
        missinfo.insert(END, cleantxt)
        #dlistarray.replace("[",",","]").replace("","|",""))
        missinfo.configure(state="disabled")
    #else:
     #   pass

def clock():
    global clocklbl, clockstr, queidlast, qid
    clockstr= time.strftime("%I:%M:%S %p")
    clocklbl.config(text=clockstr)
    lastque = ("Last person in Queue: " + str(qid))
    queidlast.set(lastque)
    root.after(1000,clock)
clock()

averagetime = 0
def runtimer():
    global averagetime
    timer = 0
    averagetime = 0
    while True:
        time.sleep(1)
        timer +=1
        print(timer)

        if someonedequed == True:
            waitingtime=timer
            averagetime = (waitingtime + averagetime)/2
            #print(waitingtime)
            print("tinawag na aq yuh")
            print("average time is")
            print(averagetime)
            break


def admindata():
    global totalserve, qid, idnow,missedlistarray

   # izempty = str(slot1.get())
   # firstque = str(slot1.get())
   # if izempty != "EMPTY SLOT":
    #    lastque = str(qid)
    #else:
    #    firstque = "None"
   #     lastque = "None"
    file = open("admindata.txt","w")
    #totalserved
    file.write(str(totalserve))
    #howmany in que? 
    file.write("\n"+str(qid))
    #last person served
    file.write("\n"+str(idnow))
    #missing list
    file.write("\n"+str(missedlistarray))
    #waitingtime
  #  file.write("\n"+str(averagetime))
   # file.close()


    

    root.after(10000,admindata)
admindata()

issimul = False
def database():
    global rid, idnow, qid, averagetime,simid
    if issimul == True:
        idnow = simid
    else:
        pass
    
    izempty = str(slot1.get())
    firstque = str(slot1.get())
    if izempty != "EMPTY SLOT":
        lastque = str(qid)
    else:
        firstque = 0
        lastque = 0
    ###############################
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="queuerdb")
    
    mycursor = mydb.cursor()
    
    sql = "UPDATE data SET howmany = %s, nowserve = %s, first = %s, last = %s, average = %s"
    val = (rid,idnow,firstque,lastque,averagetime)
    
    mycursor.execute(sql, val)
    mydb.commit()
    #print(mycursor.rowcount, "records affected")
        
    root.after(10000,database)
database()
    

cfrunning = False
def claim_face():
    #print("work")
    blackout()
    global cfrunning
    cfrunning = True
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
    #iniciate id counter
    global id
    id = 0

    # names related to ids: example ==> Marcelo: id=1,  etc
    names = str(tid)
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.grab()
    cam.set(4, 480) # set video height
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    t_end = time.time() + 10
    while time.time() < t_end:
        ret, img =cam.read()
        img = cv2.flip(img, 1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence= recognizer.predict(gray[y:y+h,x:x+w])
        
            # If confidence is less them 100 ==> "0" : perfect match 
            if (confidence < 100):
                #id = names[id]
                confidence = "{0}%".format(round(100 - confidence))
                
                passing = int(confidence.rstrip("%"))

                #time.sleep(5)
                if (passing > 60):
                    global passed
                    #print("PASSish")
                    passed = True
                    #print(passed)
                    
                    
                    cv2.putText(
                        img, 
                        str(id), 
                        (x+5,y-5), 
                        font, 
                        1, 
                        (255,255,255), 
                        2
                        )
                    cv2.putText(
                        img, 
                        str(confidence), 
                        (x+5,y+h-5), 
                        font, 
                        1, 
                        (255,255,0), 
                        1
                        )
                    #for missed queue
                    

                    #if(firstq != "EMPTY SLOT"):
                     #   firstq = 0
                    #else:
                     #   pass
                    nslot = str(slot1.get())
                    if nslot != "EMPTY SLOT":
                        firstq = int(slot1.get())   
                    else:
                        firstq= None
                     
                    global missedlistarray

                    #print("id is " + str(id) + "slot is " + str(firstq))
                    if (passed == 1 and id == firstq):                     
                        Queue.deq()
                        nowservingthread()

                    elif passed == 1 and (int(id) in missedlistarray):
                        print("missed access")
                        missedlistarray = np.delete(missedlistarray, np.where(missedlistarray == id))

                        missinfo.configure(state="normal")
                        missinfo.delete('1.0', END)
                        arraytxt = str(missedlistarray)
                        missingpersonstr = str(id)
                        cleantxt = arraytxt.replace('[', '').replace(']','').replace('.','|').replace(missingpersonstr,'')
                        missinfo.insert(END, cleantxt)
                        missinfo.configure(state="disabled")
                        nowservingthread()

                      
                    #time.sleep(1)                                
                    elif (passed == 1 and id != firstq):
                        #global warningquetxt
                        #warningquetxt1 = str(id)
                        #warningquetxt.set(warningquetxt1)
                        time.sleep(1)
                        if (passed == 1 and id != firstq):
                            warning1()
                        #print(id)
                        #print(missedlistarray)
                    else:
                        pass
                else:
                    pass
            else:
                id = "unknown"
                confidence = "{0}%".format(round(100 - confidence))
                warning2()
                

            cv2.putText(
                        img, 
                        str(id), 
                        (x+5,y-5), 
                        font, 
                        1, 
                        (255,255,255), 
                        2
                       )
            cv2.putText(
                        img, 
                        str(confidence), 
                        (x+5,y+h-5), 
                        font, 
                        1, 
                        (255,255,0), 
                        1
                       )  
    
        cv2.imshow('Claim Camera',img)
        cv2.moveWindow('Claim Camera', 0, 450)
        #cv2.moveWindow('Back Camera', 1500, 400)second window  
        cv2.waitKey(1)
        #k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        cv2.waitKey(3000)
        if passed == 1:
            break
        elif passed == 0:
            warning3()
            break
            
        
    print("\n [INFO] Exiting Program and cleanup stuff")
    #print("error?")
    cfrunning=False
    cam.release()
    cv2.destroyAllWindows()
    
def nowserving():
    global idnow
    #time.sleep(1)
    #timthr = threading.Thread(target=runtimer, daemon = True)
    #timthr.start()
    
    print("now serving thread running")

    imgvar = ("dataset/User." + str(id) + ".15.jpg")
    openimg = Image.open(imgvar)
    resizedimg = openimg.resize((300, 300))#width height
    userimg = ImageTk.PhotoImage (resizedimg)
    
    imglbl.configure(image = userimg)
    imglbl.image = userimg
    #print("nowserving opened")
    idnow = str(id)
    que = ("QUEUE ID: " + idnow)
    queidnow.set(que)
    print(imgvar)

    #text to speech
    engine.stop()
    engine = pyttsx3.init()
    voices= engine.getProperty("voices")
    engine.setProperty("rate",100)
    tts = ("We are now serving Queue ID number,"+idnow)
    engine.say(tts)
    engine.runAndWait()
    print(tts)
    #DELETION OF FACE DATA AFTER CLAIM, (IF DSWD SAYS TO KEEP IT)
    #filelist = [ f for f in os.listdir(mydir) if f.startswith("User."+str(id)) ]
    #for f in filelist:
     #   os.remove(os.path.join(mydir, f))
        
    runtimer()

def nowservingthread():
    nowser = threading.Thread(target=nowserving, daemon = True)
    nowser.start()

rfrunning = False
def register_face():
    blackout()
    global tid, rfrunning
    rfrunning = True
    tid += 1
    id = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    cam = cv2.VideoCapture(0)
    cam.grab()
    #cam.set(4, 480) # set video height
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    t_end = time.time() + 10
    while time.time() < t_end:
        ret, img =cam.read()
        img = cv2.flip(img, 1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence= recognizer.predict(gray[y:y+h,x:x+w])
        
            # If confidence is less them 100 ==> "0" : perfect match 
            if (confidence < 100):
                #id = names[id]
                confidence = "{0}%".format(round(100 - confidence))
                
                passing = int(confidence.rstrip("%"))

                #time.sleep(5)
                if (passing > 60):
                    global passed
                    #print("PASSish")
                    passed = True
                    #print(passed)
                    
                    
                    #if(firstq != "EMPTY SLOT"):
                     #   firstq = 0
                    #else:
                     #   pass
                    #print("id is " + str(id) + "slot is " + str(firstq))
                    if (passed == 1):                     
                        #warningbox()
                        #warningtxt3 = "Registration Denied\nYou are already registered."
                        #warningtxt.set(warningtxt3)
                        #warningque.destroy()
                        
                        if tagaloglang == True:
                            helpbox.configure(text = helpbox7fil)
                            time.sleep(3)
                            helpbox.configure(text = helpbox7fil)
                        elif tagaloglang == False:
                            helpbox.configure(text = helpbox7)
                            time.sleep(3)
                            helpbox.configure(text = helpbox7)

                        return
                    elif passed == 0:
                        pass
                else:
                    pass
            else:
                pass
        else:
            cam.release()
            break
    cam = cv2.VideoCapture(0)
    cam.set(3, 380) # set video width
    cam.set(4, 270) # set video height
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # For each person, enter one numeric face id
    face_id = tid

    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0
    while (cam.isOpened()):
        if tagaloglang == True:
            helpbox.configure(text = helpbox2fil)
        elif tagaloglang == False:
            helpbox.configure(text = helpbox2)
        
        ret, img = cam.read()
        img = cv2.flip(img, 1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('Register Camera', img)
            cv2.moveWindow('Register Camera', 0, 200)
            cv2.waitKey(1)

        if len(faces)==0:
                time.sleep(3)
                print("No faces found")
                #t_end = time.time() + 30
                while True:
                    tid -=1
                    print("tid has been reduced")
                    
                    if tagaloglang == True:
                        helpbox.configure(text = helpbox5fil)
                        time.sleep(3)
                        helpbox.configure(text = helpbox1fil)
                    elif tagaloglang == False:
                        helpbox.configure(text = helpbox5)
                        time.sleep(3)
                        helpbox.configure(text = helpbox1)
                        cam.release()
                        cv2.destroyAllWindows()
                        rfrunning=False
                    return None, None

        time.sleep(1)
        #k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if len(faces)==0:
            break
        elif count >= 30: # Take 30 face sample and stop video
             break

    # Do a bit of cleanup
    #reg()
    #train()
    
    if tagaloglang == True:
        helpbox.configure(text = helpbox3fil + str(qid))
        time.sleep(10)
        helpbox.configure(text = helpbox1fil)
    elif tagaloglang == False:
        helpbox.configure(text = helpbox3 + str(qid))
        time.sleep(10)
        helpbox.configure(text = helpbox1)
    #global rfrunning
    Queue.reg()
    rfrunning = False
    blackoutgetter()
    trainthread()
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # grayscale
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids

def train():
    #if tagaloglang == True:
    #    helpbox.configure(text = helpbox4fil)
    #elif tagaloglang == False:
    #    helpbox.configure(text = helpbox4)
    print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces,ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))
    # Save the model into trainer/trainer.yml
    recognizer.write('trainer/trainer.yml') 
    # Print the numer of faces trained and end program
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
    #Queue.reg()
    #root.after(10000, train)

def cfrfchecker():
    global cfrunning, rfrunning
    cfrunning = False
    rfrunning = False
    root.after(10000, cfrfchecker)
cfrfchecker()

def trainthread():
    tt = threading.Thread(target=train, daemon=True)
    tt.start()
    

def dequethread():
    global cfrunning
    t1 = threading.Thread(target=claim_face, daemon=True)
    if cfrunning == False:
        t1.start()
    else:
        print("cf already running")

def enquethread():
    global rfrunning
    t2 = threading.Thread(target=register_face, daemon=True)
    if rfrunning == False:
        t2.start()
    else:
        print("already running")
        

def checkcams():
    frontcam = cv2.VideoCapture(0)
    frontcam.set(3, 380) # set video width
    frontcam.set(4, 270) # set video height
    emptyface = cv2.imread("assets/facehollow.png")
    size = 420
    emptyface = cv2.resize(emptyface, (size, size))
    
    #mask
    img2gray = cv2.cvtColor(emptyface, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    if tagaloglang == True:
        helpbox.configure(text = helpbox6fil)
    elif tagaloglang == False:
        helpbox.configure(text = helpbox6)
    #backcam = cv2.VideoCapture(1)
    t_end = time.time() + 10
    while time.time() < t_end:
        ret, frame = frontcam.read()
        roi = frame[-size-30:-30, -size-130:-130]
        #ret, frame2 = backcam.read() 
        #frame2 = cv2.flip(frame2, 1)
        roi[np.where(mask)] = 0
        roi += emptyface
        frame = cv2.flip(frame,1)
                
        cv2.imshow('Register Camera',frame)
        cv2.moveWindow('Register Camera', 0, 200)
        #cv2.imshow('framezkie',frame2)
#         registerbutton.when_pressed = enquethread
        if cv2.waitKey(1) & registerbutton.is_pressed:
            frontcam.release()
            #backcam.release()
            cv2.destroyAllWindows()
            enquethread()
            break
        
    if tagaloglang == True:
        helpbox.configure(text = helpbox8fil)
    elif tagaloglang == False:
        helpbox.configure(text = helpbox8)
    time.sleep(5)
    if tagaloglang == True:
        helpbox.configure(text = helpbox1fil)
    elif tagaloglang == False:
        helpbox.configure(text = helpbox1)   
    frontcam.release()
    cv2.destroyAllWindows()
    
    
        
def deleteface():
    filelist = [ f for f in os.listdir(mydir) if f.startswith("User") ]
    for f in filelist:
        os.remove(os.path.join(mydir, f))


def simulationclaim():
    global missedlistarray, missinfo,id,imgvar
    firstq = str(slot1.get())
    if firstq == "EMPTY SLOT":
        pass
    elif firstq != "EMPTY SLOT":
        imgvar = ("simulationpic/" + str(id) + ".png")
    
    Queue.deq()
    simulationservestart()


mclaim = False
def simulationserve():
    if mclaim == False:
        global simid
        #timthr = threading.Thread(target=runtimer, daemon = True)
        #timthr.start()

        simidminus1 = int(slot1.get())
        simidminus1 -= 1
        simid = str(simidminus1)
        imgvar = ("simulationpic/" + simid + ".png")
        openimg = Image.open(imgvar)
        resizedimg = openimg.resize((300, 300))#width height
        userimg = ImageTk.PhotoImage (resizedimg)
    
        imglbl.configure(image = userimg)
        imglbl.image = userimg
        print("nowserving opened")
        que = ("QUEUE ID: " + simid)
        queidnow.set(que)
        print(imgvar)

        #text to speech
        engine = pyttsx3.init()
        engine.stop()
       
        if timerrunning == False:
            voices= engine.getProperty("voices")
            engine.setProperty("rate",100)
            tts = ("We are now serving queue ID number,"+simid)
            engine.say(tts)
            engine.runAndWait()
            print(tts)
        runtimer()
    elif mclaim == True:
        simid = str(misimid)
        imgvar = ("simulationpic/" + simid + ".png")
        openimg = Image.open(imgvar)
        resizedimg = openimg.resize((300, 300))#width height
        userimg = ImageTk.PhotoImage (resizedimg)
    
        imglbl.configure(image = userimg)
        imglbl.image = userimg
        print("nowserving opened")
        que = ("QUEUE ID: " + simid)
        queidnow.set(que)
        print(imgvar)

        #text to speech
        engine = pyttsx3.init()
        voices= engine.getProperty("voices")
        engine.setProperty("rate",100)
        
        if timerrunning == False:
            engine.stop()
            tts = ("We are now serving queue ID number,"+simid)
            engine.say(tts)
            engine.runAndWait()
            print(tts)
        runtimer()


def simulationservestart():
    st = threading.Thread(target=simulationserve, daemon = True)
    st.start()

def unknownclaim():
    warning2()

def notyourturnclaim():
    global warningquetxt, warningquetxt1
    warningbox()
    warningtxt1 = ("You're not next in queue\nYour queue number is: ")
    warningtxt.set(warningtxt1)
    warningquetxt1 = 13
    warningquetxt.set(warningquetxt1)



def missclaim():
    global missedlistarray, misimid,mclaim
    misimid = 3
    mclaim = True
    if misimid in missedlistarray:
        missedlistarray = np.delete(missedlistarray, np.where(missedlistarray == misimid))
        print(missedlistarray)

        missinfo.configure(state="normal")
        missinfo.delete('1.0', END)
        #missedlistarraytext = missedlistarray.tostring()
        arraytxt = str(missedlistarray)
        misimidstr=str(misimid)
        cleantxt = arraytxt.replace('[', '').replace(']','').replace('.','|').replace(misimidstr,'')
        missinfo.insert(END, cleantxt)
        missinfo.configure(state="disabled")
        simulationservestart()


def simulation1():
    global rid, qid, issimul
    issimul = True
    rid = 15
    qid = 15

    #button33 = tk.Button(root)
    #button33.configure(text='Simulation Claim', command =simulationclaim)
    #button33.place(anchor="nw", relx=0.015, rely=0.893, x=150, y=30)

    #button34 = tk.Button(root)
    #button34.configure(text='Unknown Claim', command =unknownclaim)
    #button34.place(anchor="nw", relx=0.015, rely=0.893, x=0, y=0)

    #button35 = tk.Button(root)
    #button35.configure(text='Not your turn Claim', command =notyourturnclaim)
    #button35.place(anchor="nw", relx=0.015, rely=0.893, x=0, y=30)

    #button36 = tk.Button(root)
    #button36.configure(text='M Claim', command =missclaim)
    #button36.place(anchor="nw", relx=0.015, rely=0.893, x=220, y=0)

    slot1.set("1")
    slot2.set("2")
    slot3.set("3")
    slot4.set("4")
    slot5.set("5")
    slot6.set("6")
    slot7.set("7")
    slot8.set("8")
    slot9.set("9")
    slot10.set("10")
    slot11.set("11")
    slot12.set("12")
    slot13.set("13")
    slot14.set("14")
    slot15.set("15")
    nextpic()


def callfirst():
    if str(slot1.get()) != "EMPTY SLOT":
        engine = pyttsx3.init()
        voices= engine.getProperty("voices")
        engine.setProperty("rate",100)
        tts = ("Calling Queue I dee number" + str(slot1.get()))
        engine.say(tts)
        engine.runAndWait()
    else:
        pass
    
def callheadlist():
    engine = pyttsx3.init()
    
    callinline()
    if str(slot1.get()) != "EMPTY SLOT" and str(slot2.get()) != "EMPTY SLOT":
            #print(timerrunning)
            engine.stop()
            print("tinawag aq 3")
            engine.setProperty("rate",100)
            tts = ("Calling Queue I dees" + firstinque + "to" + lastinque + "to get ready.")
            engine.say(tts)
            engine.runAndWait()
    else:
        pass


def callfirstthr():
     callerfirst = threading.Thread(target=callfirst, daemon = True)
     callerfirst.start()
callfirstthr()

def callheadlistthr():
     callerhead = threading.Thread(target=callheadlist, daemon = True)
     callerhead.start()
callfirstthr()

def langswitch():
    global tagaloglang
    tagaloglang = True
    helpbox.configure(text = helpbox1fil)
    print(tagaloglang)
    time.sleep(1)
    if langbutton.is_pressed:
        print("english ulet")
        helpbox.configure(text = helpbox1)
        tagaloglang = False




#TESUTO
def testreg():
    Queue.reg()
def testdeq():
    Queue.deq()
def approve():
    Queue.deq()
    nowservingthread()
    
#REMOTE DEFZ
#conn = RawConnection()
def remoteconnect():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if (device.name == "gpio_ir_recv"):
            print(device.path)
            return device
    print("no remote found")
#remoteconnect()
    

dev = remoteconnect()
def remote():
    while(True):
        #time.sleep(5)
        event = dev.read_one()
        if (event):
            print(event.value)
            if event.value == 460548:#1
                simulation1()
            elif event.value == 460549:#2
                simulationclaim()
            elif event.value == 460550:#3
                missclaim()
            elif event.value == 460552:#4
                unknownclaim()
            elif event.value == 460553:#5
                notyourturnclaim()
            elif event.value == 460652:#red
                next()
            elif event.value == 460566:#blue
                callfirstthr()
            elif event.value == 460565:#yellow
                callheadlistthr()
            elif event.value == 460632:#return
                callpeople()
            elif event.value == 460589:#exit
                pausetimer()
            elif event.value == 460616:#last
                testreg()
            elif event.value == 460618:#2nd to last
                testdeq()
            elif event.value == 460648:#enter
                approve()
                     
            
def remotestart():
    while True:
        remote()
        
def remotethread():
    rem = threading.Thread(target=remotestart, daemon=True)
    rem.start()
    os.system('sudo ir-keytable -p all')
    os.system('sudo ir-keytable -D 500 -P 250')
remotethread()

def blackout():
    global oobqueue, rid, qid

    sl1 = slot1.get()
    sl2 = slot2.get()
    sl3 = slot3.get()
    sl4 = slot4.get()
    sl5 = slot5.get()
    sl6 = slot6.get()
    sl7 = slot7.get()
    sl8 = slot8.get()
    sl9 = slot9.get()
    sl10 = slot10.get()
    sl11= slot11.get()
    sl12= slot12.get()
    sl13 = slot13.get()
    sl14 = slot14.get()
    sl15 = slot15.get()
    sl16 = slot16.get()
    sl17 = slot17.get()
    sl18 = slot18.get()
    sl19 = slot19.get()
    sl20 = slot20.get()
    
    izempty = str(slot1.get())
    firstque = str(slot1.get())
    if izempty != "EMPTY SLOT":
        lastque = str(qid)
    else:
        firstque = "None"

    file = open("blackoutdata.txt","w")
    
    file.write(str(sl1))
    file.write("\n"+str(sl2))
    file.write("\n"+str(sl3))
    file.write("\n"+str(sl4))
    file.write("\n"+str(sl5))
    file.write("\n"+str(sl6))
    file.write("\n"+str(sl7))
    file.write("\n"+str(sl8))
    file.write("\n"+str(sl9))
    file.write("\n"+str(sl10))
    file.write("\n"+str(sl11))
    file.write("\n"+str(sl12))
    file.write("\n"+str(sl13))
    file.write("\n"+str(sl14))
    file.write("\n"+str(sl15))
    file.write("\n"+str(sl16))
    file.write("\n"+str(sl17))
    file.write("\n"+str(sl18))
    file.write("\n"+str(sl19))
    file.write("\n"+str(sl20))
    file.write("\nQID AND RID")
    file.write("\n"+str(qid))
    file.write("\n"+str(rid))
    file.write("\n"+str(oobqueue))
    #file.write("\n"+lastque)
    #file.write("\n"+str(averagetime))
    file.close()
    
def blackoutgetter():
    blackout()
    root.after(1000, blackoutgetter)


def getslotsbo():
    print("hi")
    global rid, qid, oobqueue
    with open('blackoutdata.txt') as f:
        data = f.readlines()
        qid = int(data[21])
        rid = int(data[22])
        
        if oobqueue:
            oobq = data[23].replace("[", ",").replace("]", ",")(" ", ",").strip()
            oobq2 = oobq.split(",")
            oobqueue = oobq2
            print(oobqueue)
        
        slot1.set(data[0].rstrip("\n"))
        slot2.set(data[1].rstrip("\n"))
        slot3.set(data[2].rstrip("\n"))
        slot4.set(data[3].rstrip("\n"))
        slot5.set(data[4].rstrip("\n"))
        slot6.set(data[5].rstrip("\n"))
        slot7.set(data[6].rstrip("\n"))
        slot8.set(data[7].rstrip("\n"))
        slot9.set(data[8].rstrip("\n"))
        slot10.set(data[9].rstrip("\n"))
        slot11.set(data[10].rstrip("\n"))
        slot12.set(data[11].rstrip("\n"))
        slot13.set(data[12].rstrip("\n"))
        slot14.set(data[13].rstrip("\n"))
        slot15.set(data[14].rstrip("\n"))
        slot16.set(data[15].rstrip("\n"))
        slot17.set(data[16].rstrip("\n"))
        slot18.set(data[17].rstrip("\n"))
        slot19.set(data[18].rstrip("\n"))
        slot20.set(data[19].rstrip("\n"))

#button variables
registerbutton = Button(26)
claimbutton = Button(22)
langbutton = Button(6)
bobutton = Button(16)
def realbuttons():
    registerbutton.when_pressed = checkcams
    claimbutton.when_pressed = dequethread
    langbutton.when_pressed = langswitch
    bobutton.when_pressed = getslotsbo
realbuttons()

def dqbutton():
    global button3
    button3 = tk.Button(root)
    button3.configure(text='nag blackout huhu', command =getslotsbo)
    button3.place(anchor="nw", relx=0.015, rely=0.893, x=300, y=0)
    
    button4 = tk.Button(root)
    button4.configure(text='Delete Face Data', command =deleteface)
    button4.place(anchor="nw", relx=0.015, rely=0.893, x=400, y=0)

    button5 = tk.Button(root)
    button5.configure(text='Call People', command =callpeople)
    button5.place(anchor="nw", relx=0.015, rely=0.893, x=500, y=0)

    button6 = tk.Button(root)
    button6.configure(text='Auto Pause', command =pausetimer)
    button6.place(anchor="nw", relx=0.015, rely=0.893, x=500, y=30)

    button7 = tk.Button(root)
    button7.configure(text='Auto Play', command =unpausetimer)
    button7.place(anchor="nw", relx=0.015, rely=0.893, x=400, y=30)

    button8 = tk.Button(root)
    button8.configure(text='Next', command =next)
    button8.place(anchor="nw", relx=0.015, rely=0.893, x=300, y=30)

    button9 = tk.Button(root)
    button9.configure(text='Simulation', command =simulation1)
    button9.place(anchor="nw", relx=0.015, rely=0.893, x=150, y=0)

    button99 = tk.Button(root)
    button99.configure(text='Check Cam', command =checkcams)
    button99.place(anchor="nw", relx=0.015, rely=0.893, x=150, y=30)

    ##remotes
    call1 = tk.Button(root)
    call1.configure(text='Call First', command= callfirst)
    call1.place(anchor="nw", relx= 0.015, rely=0.893, x=500, y = -30)

    #callhead



def backscreen():
    backwindow = tk.Tk()
    backwindow.title("Que'er Bot Registering Window")
    backwindow.geometry("600x900+680+50")

    #backtitle = tk.Message(backwindow)
    #backtitle.configure(
    #    background="#06304b",
    #    font=("TkMenuFont", 18, "bold"),
    #    justify="center",
    #    text='Registering Window',
    #    width= 300)
    #backtitle.place(relwidth=1)
    
    global helpbox
    helpbox = tk.Message(backwindow)
    helpbox.configure(font=("Helvetica", 26, "bold"), width=500,justify="center")
    helpbox.configure(
        text= helpbox1)
    helpbox.place(x=300,y=350,relwidth=0.9, relheight=1, anchor=CENTER)


    #button = tk.Button(backwindow)
   # button.configure(text='"RED BUTTON"', command =enquethread)
    #button.place(x=300, y=590,anchor=S)
    backwindow.mainloop()
backscreen()


root.mainloop()
