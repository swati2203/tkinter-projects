# from playsound import playsound
from tkinter import LEFT, RIGHT, TOP, Button, Entry, Frame, Label, OptionMenu, PhotoImage, StringVar, Tk
import datetime
import time
from playsound import playsound
clock=Tk()
clock.title("ALARM CLOCK")
clock.geometry("500x500")
def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{min.get()}:{sec.get()}"
        time.sleep(1)
 
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
 
        if current_time == set_alarm_time:
            print("Time to Wake up")
            playsound("Believer.mp3")
            print("alarm time")
            break
icon=PhotoImage(file="4341025.png")
abel1 = Label( clock, image = icon).place(x=0,y=0)
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Button(clock,text="Set your alarm",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=30)
hour=StringVar()
min = StringVar()
sec = StringVar()
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15,).place(x=120,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command=alarm).place(x =110,y=70)
 
clock.mainloop()
