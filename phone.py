from tkinter import*
from PIL import ImageTk,Image
import webbrowser
import subprocess
import platform
from datetime import datetime,date
import pytz
import sys
import os
import requests
import json
root=Tk()
root.title("Pro Phone 8")
root.geometry("650x650")
root.minsize(650,650)
root.maxsize(650,650)
root.configure(bg="white")

phone = ImageTk.PhotoImage(Image.open ("phone.png"))
google = ImageTk.PhotoImage(Image.open ("google.png"))
youtube = ImageTk.PhotoImage(Image.open ("youtube.png"))
whatsapp = ImageTk.PhotoImage(Image.open ("whatsapp.png"))
notepad = ImageTk.PhotoImage(Image.open ("notepad.png"))
transly = ImageTk.PhotoImage(Image.open ("transly.png"))
skywatch = ImageTk.PhotoImage(Image.open ("skywatch.png"))
calc = ImageTk.PhotoImage(Image.open ("calc.png"))
gmail = ImageTk.PhotoImage(Image.open ("gmail.png"))
maps = ImageTk.PhotoImage(Image.open ("map.png"))

background=Label(root,image=phone)
background.place(relx=0.5,rely=0.5,anchor=CENTER,width=2000,height=2000)

def runsky():
    subprocess.Popen([sys.executable,os.path.abspath("skywatch.py")])
    
weather_button=Button(root,bg="cornflower blue",command=runsky)
weather_button.place(relx=0.51,rely=0.23,anchor=CENTER,width=298,height=60)

dated=date.today()
link=requests.get("https://api.openweathermap.org/data/2.5/weather?q=Dubai&appid=21cab08deb7b27f4c2b55f3e2df28ea4")
data=json.loads(link.content) 
kelvin=data["main"]["temp"] 
weather=data["weather"][0]["description"].capitalize()
temp=str(round(kelvin-273))+"°C"
temp_label=Label(root,text=temp,bg="cornflowerblue",font=("Arial",14,"bold"))
temp_label.place(relx=0.64,rely=0.21,anchor=CENTER)
city_label=Label(root,text="Dubai",bg="cornflowerblue",font=("Tahoma",12,"bold"))
city_label.place(relx=0.35,rely=0.25,anchor=CENTER)
today=Label(root,text=dated,bg="cornflowerblue",font=("Calibri",12,"bold"))
today.place(relx=0.35,rely=0.21,anchor=CENTER)
description=Label(root,text=weather,bg="cornflowerblue",font=("Helvectica",11))
description.place(relx=0.65,rely=0.25,anchor=CENTER)

def rungoogle():
    webbrowser.open("https://www.google.com/")
def runyoutube():
    webbrowser.open("https://www.youtube.com/")
def runwhatsapp():
    webbrowser.open("https://web.whatsapp.com/")
def rungm():
    webbrowser.open("https://www.gmail.com")
def runmap():
    webbrowser.open("https:/www.google.com/maps/")
def runnotepad():
    subprocess.Popen([sys.executable,os.path.abspath("notepad.py")])
def runtransly():
    subprocess.Popen([sys.executable,os.path.abspath("transly.py")])
def runcalc():
    operating=platform.system()
    try:
        if(operating=="Windows"):
            subprocess.Popen("calc.exe")
        elif(operating=="Darwin"):
            subprocess.Popen(["open","/Applications/Calculator.app"])
        elif(operating=="Windows"):
            subprocess.Popen("calc.exe")
        else:
            messagebox.showinfo("Error","Operating System Not Found")
    except:
        messagebox.showinfo("Error","Cannot find Calculator app")
        
traicon=Button(root, image=transly, command=runtransly,width=50,height=50)
traicon.place(relx=0.33,rely=0.8,anchor= CENTER)
skyicon=Button(root,image=skywatch,command=runsky,width=50,height=50)
skyicon.place(relx=0.67,rely=0.8,anchor= CENTER)
goicon=Button(root,image=google, command=rungoogle,width=50,height=50)
goicon.place(relx=0.33,rely=0.6,anchor=CENTER)
youicon=Button(root, image=youtube, command=runyoutube,width=50,height=50)
youicon.place(relx=0.67,rely=0.6,anchor= CENTER)
whicon=Button(root,image=whatsapp,command=runwhatsapp,width=50,height=50)
whicon.place(relx=0.33,rely=0.4,anchor= CENTER)
noicon=Button(root,image=notepad, command=runnotepad,width=50,height=50)
noicon.place(relx=0.67,rely=0.4,anchor=CENTER)
calcicon=Button(root,image=calc, command=runcalc,width=50,height=50)
calcicon.place(relx=0.5,rely=0.4,anchor=CENTER)
gmicon=Button(root,image=gmail, command=rungm,width=50,height=50)
gmicon.place(relx=0.5,rely=0.6,anchor=CENTER)
mapicon=Button(root,image=maps, command=runmap,bg="white",width=50,height=50)
mapicon.place(relx=0.5,rely=0.8,anchor=CENTER)

tralabel=Label(root,text="Transly")
tralabel.place(relx=0.33,rely=0.88,anchor= CENTER)
skylabel=Label(root,text="Skywatch")
skylabel.place(relx=0.67,rely=0.88,anchor= CENTER)
golabel=Label(root,text="Google")
golabel.place(relx=0.33,rely=0.69,anchor=CENTER)
youlabel=Label(root,text="Youtube")
youlabel.place(relx=0.67,rely=0.69,anchor= CENTER)
whlabel=Label(root,text="Whatsapp")
whlabel.place(relx=0.33,rely=0.48,anchor= CENTER)
nolabel=Label(root,text="Super Notepad")
nolabel.place(relx=0.67,rely=0.48,anchor=CENTER)
calclabel=Label(root,text="Calculator")
calclabel.place(relx=0.5,rely=0.48,anchor=CENTER)
gmlabel=Label(root,text="Gmail")
gmlabel.place(relx=0.5,rely=0.69,anchor=CENTER)
maplabel=Label(root,text="Maps")
maplabel.place(relx=0.5,rely=0.88,anchor=CENTER)

showtime=Label(root,bg="#abbdcc",font=("Arial",12))
showtime.place(relx=0.32,rely=0.04)
def time():
    timezone=pytz.timezone("Asia/Dubai")
    timegot=datetime.now(timezone)
    localtime=timegot.strftime("%H:%M:%S") 
    showtime['text']=localtime
    root.after(1000,time)
time()
root.mainloop()