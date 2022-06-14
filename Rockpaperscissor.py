
import random
from tkinter import Button, Entry, Label, StringVar, Tk


Game=Tk()
Game.title("ROCK PAPER SCISSOR")
Game.geometry("500x500")
label=Label(Game,text="Rock,Paper,Scissor",fg="#e71989",bg="#ffe042",font="Helvetica 20 bold italic").pack()
label1=Label(Game,text="").pack()
label2=Label(Game,text=("choose one:Rock,Paper,scissor"),bg="White",fg="Black",font=("calbri",15)).place(x=120,y=70)
user=StringVar()
user_pick=Entry(Game,textvariable=user,font="aerial 15",bg='antiquewhite2').place(x=140,y=100)
com_pick=random.randint(1,3)
if com_pick==1:
    com_pick="Rock"
elif com_pick==2:
    com_pick="Paper"
else:
    com_pick="Scissors"
result=StringVar()
def user_result():
    user_take=user.get()
    if user_take==com_pick:
        result.set("Tie,both select same")
    elif user_take=="Rock" and com_pick=="Paper":
        result.set("You lose,as computer select paper")
    elif user_take=="Rock" and com_pick=="Scissor":
        result.set("You win,computer select Scissor")
    elif user_take=="Paper" and com_pick=="Rock":
        result.set("You win,computer select Rock")
    elif user_take=="Paper" and com_pick=="Scissor":
        result.set("You lose,computer select Scissor")
    elif user_take=="Scissor" and com_pick=="Paper":
        result.set("You win,computer select Paper")
    elif user_take=="Scissor" and com_pick=="Rock":
        result.set("You lose,computer select rock")
    else:
        result.set("invalid,choose any : Rock,Paper,Scissor")
def reset():
    result.set("")
    user.set("")
def exit():
    Game.destroy()
# user_pick=Entry(Game,textvariable=user,font="aerial 15",bg='antiquewhite2').pack()
Result=Entry(Game, font = 'arial 10 bold', textvariable = result, bg ='antiquewhite2',width = 50,).place(x=100, y = 250)
button1=Button(Game, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = user_result).place(x=200,y=190)
button2=Button(Game, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = reset).place(x=120,y=310)
button3=Button(Game, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = exit).place(x=250,y=310)


    

    
Game.mainloop()

