from curses import window
from tkinter import *
from tkinter import font
window = Tk()
my_label=Label(text="welcome to regal resturant",font=("Aerial Bold",25),fg="dark green",bg="lavender")
my_label.pack()
def send():
    send="You :"+e.get()
    # a=Entry(window,width=90)
    txt.insert(END,"\n"+send)
    if e.get()=="hello" or e.get()=="hii":
        txt.insert(END,"\n"+'''assistant: hii!welcome to regal resturant :-1.Dining,2.homedelivery''')
    elif (e.get()=="1"):
        txt.insert(END,"\n"+"assistant:so should we book your table:-yes or no")
    elif (e.get()=="No"):
        txt.insert(END,"\n"+"ok thank you!Share your feedback")
    elif(e.get()=="Good" or e.get()=="excellent"):
        txt.insert(END,"\n"+"thanks for your valuable feedback")
    elif (e.get()=="yes"):
        txt.insert(END,"\n"+"ok your table is booked ")
    elif (e.get()=="2"):
        txt.insert(END,"\n"+'''check out the menu:-1.Hot Beverages:-
        coffe-20
        tea-15
        chocolate shake-30
        nescafe-28 
        2.sandwiches:-
        veg sandwiches-45
        chesse sandwiches-70
        Italian sandwich-76
        club sandwich-100
        3.Puri bhaji:-
        chole bhature-90
        puri sabji-50
        shrikhand puri-68
        potato bhaji-25
        call us to order!''')
    else:
        txt.insert(END,"\n"+"assistant: sorry i didn't get it ")
    e.delete(0,END)
txt=Text(window)
txt.pack(padx=60,pady=20)
e=Entry(window,width=50,font=("Helvetica",25))
send=Button(window,text="Send",fg="green",command=send).pack(side="right")
e.pack(side="right")
window.title("CHATBOT")
window.mainloop() 