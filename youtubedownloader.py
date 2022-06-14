from curses import window
from tkinter import Button, Entry, Label, StringVar, Tk
from pytube import YouTube


download=Tk()
download.title("Youtube downloader")
download.geometry("500x300")
label=Label(download,text="Youtube video downloader",fg="black",font="arial 20 bold").pack()
link=StringVar()
label1=Label(download,text="Paste link here",font="calibri 15").pack()
url=Entry(download,textvariable=link,fg="pink",width=25).place(x=140,y=80)
def downloader():
    url1=YouTube(str(link.get()))
    video = url1.streams.get_highest_resolution()
    video.download()
    Label(download, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
Button(download,text="download",fg="white",bg="black",command=downloader).place(x=180,y=120)  
download.mainloop()