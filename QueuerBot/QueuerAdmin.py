import tkinter as tk
from tkinter import messagebox
import os
import cv2
import threading
import tkthread; tkthread.patch() 

facedata="/home/zhed/Desktop/QueuerBot/dataset"

root = tk.Tk()
#root.geometry("1280x700+1500+30") #for second screen
root.geometry("400x400")
root.title("Que'er Bot Admin")

def dataget():
    global totalserve,totalpeople,last,missed
    with open('admindata.txt') as f:
        data = f.readlines()
        totalserve = data[0].rstrip("\n")
        totalpeople = data[1].rstrip("\n")
        last = data[2].rstrip("\n")
        missed = data[3].rstrip("\n")
dataget()

def retrieve():
    os.system("pcmanfm \"%s\"" % facedata)

def reset():
    res = messagebox.askquestion("Are you sure?", "This will delete all face data, please backup or retrieve face data first before resetting. Reset Que'uer Bot?")
    if res == 'yes':
        filelist = [ f for f in os.listdir(facedata) if f.startswith("User") ]
        for f in filelist:
            os.remove(os.path.join(facedata, f))
        
        messagebox.showinfo("Success", "Que'er Bot Reset Successfully")

def checkcam1():
    backcam = cv2.VideoCapture(0)
    
    while True:
        #ret, frame = frontcam.read()
        ret, frame2 = backcam.read()
        #frame = cv2.flip(frame, 1) 
        frame2 = cv2.flip(frame2, 1)

        #cv2.imshow('press q to exit',frame)
        cv2.imshow('BACK(press "q" to next)',frame2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(1) & 0xFF == ord('Q'):
            break
        
    #frontcam.release()
    backcam.release()
    cv2.destroyAllWindows()
    
    frontcam = cv2.VideoCapture(3)
    while True:
        ret, frame = frontcam.read()
        #ret, frame2 = backcam.read()
        frame = cv2.flip(frame, 1) 
        #frame2 = cv2.flip(frame2, 1)

        cv2.imshow('FRONT(press "q" to exit',frame)
        #cv2.imshow('press q to exit',frame2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(1) & 0xFF == ord('Q'):
            break
        
    frontcam.release()
    #backcam.release()
    cv2.destroyAllWindows()
    
    messagebox.showinfo("Success", "Camera Check Successful")
    

def camsthr():
    cam1 = threading.Thread(target=checkcam1, daemon= True)
    cam1.start()
    
def resetremote():
    os.system('sudo ir-keytable -p all')
    
    
text1 = tk.Message(root)
text1.configure(font=("Helvetica", 14, "bold"), width=500)
text1.configure(
    text= "Total Number of People: "+str(totalpeople))
text1.place(x=10,y=10)

text2 = tk.Message(root)
text2.configure(font=("Helvetica", 14, "bold"), width=500)
text2.configure(
    text= "Total People Served: "+str(totalserve))
text2.place(x=10,y=30)

text3 = tk.Message(root)
text3.configure(font=("Helvetica", 14, "bold"), width=500)
text3.configure(
    text= "Last Person Served: "+str(last))
text3.place(x=10,y=50)

text4 = tk.Message(root)
text4.configure(font=("Helvetica", 14, "bold"), width=500)
text4.configure(
    text= "Missing List: "+str(missed))
text4.place(x=10,y=70)


button = tk.Button(root)
button.configure(text="Retrieve Face Data", command=retrieve)
button.place(x=10, y=150)

button = tk.Button(root)
button.configure(text="Reset Que'er Bot", command =reset)
button.place(x=200, y=150)

button = tk.Button(root)
button.configure(text="Check Cameras", command = camsthr)
button.place(x=10, y=200)

button = tk.Button(root)
button.configure(text="Reset Remote", command = resetremote)
button.place(x=200, y=200)


text1 = tk.Message(root)
text1.configure(font=("Helvetica", 14, "bold"), width=500)
text1.configure(
    text= "If theres something with the QMS\nPlease contact: 09454680356 or \nEmail us at serumisama@gmail.com")
text1.place(x=10,y=300)

root.mainloop()