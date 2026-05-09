from tkinter import *
import requests
import json
from tkinter import messagebox
from PIL import ImageTk,Image
import time
sky="lightblue3"
root=Tk()
root.title("SkyWatch")
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background=sky)

a01d= ImageTk.PhotoImage(Image.open ("01d.jpg"))
a02d= ImageTk.PhotoImage(Image.open ("02d.jpg"))
a03d= ImageTk.PhotoImage(Image.open ("03d.jpg"))
a04d= ImageTk.PhotoImage(Image.open ("04d.jpg"))
a09d= ImageTk.PhotoImage(Image.open ("09d.jpg"))
a10d= ImageTk.PhotoImage(Image.open ("10d.jpg"))
a11d= ImageTk.PhotoImage(Image.open ("11d.jpg"))
a13d= ImageTk.PhotoImage(Image.open ("13d.jpg"))
a50d= ImageTk.PhotoImage(Image.open ("50d.jpg"))

a01n= ImageTk.PhotoImage(Image.open ("01n.jpg"))
a02n= ImageTk.PhotoImage(Image.open ("02n.jpg"))
a03n= ImageTk.PhotoImage(Image.open ("03n.jpg"))
a04n= ImageTk.PhotoImage(Image.open ("04n.jpg"))
a09n= ImageTk.PhotoImage(Image.open ("09n.jpg"))
a10n= ImageTk.PhotoImage(Image.open ("10n.jpg"))
a11n= ImageTk.PhotoImage(Image.open ("11n.jpg"))
a13n= ImageTk.PhotoImage(Image.open ("13n.jpg"))
a50n= ImageTk.PhotoImage(Image.open ("50n.jpg"))


old_city="Dubai"
city="Dubai"
rawcity="Dubai"

image= Label(root)
image.place(relx=0.5,rely=0.35,anchor=CENTER,width=200,height=200)   
cityentry=Entry(root)
weather_info_label = Label(root, bg=sky,font=("Arial",20,"bold"))
weather_info_label.place(relx=0.5,rely=0.5,anchor=CENTER) 


humidity_info_label = Label(root,text="Humidity: ", bg="lightblue3", font=("Calibri",16)) 
humidity_info_label.place(relx=0.22,rely=0.55) 

feel_info_label = Label(root,text="Feels Like: ", bg="lightblue3", font=("Calibri",16)) 
feel_info_label.place(relx=0.22,rely=0.62) 

press_info_label = Label(root,text="Pressure: ", bg="lightblue3", font=("Calibri",16)) 
press_info_label.place(relx=0.22,rely=0.7) 

speed_info_label = Label(root,text="Wind Speed:", bg="lightblue3", font=("Calibri",16)) 
speed_info_label.place(relx=0.22,rely=0.77) 

temp_info_label = Label(root, bg=sky, fg="goldenrod4",font=( "bold",27)) 
temp_info_label.place(relx=0.5,rely=0.18,anchor=CENTER) 

def place():    
    temp_info_label.place_forget()
    cityentry.place(relx=0.5,rely=0.17,anchor=CENTER)
    entrybut.place(relx=0.5,rely=0.22,anchor=CENTER)
def weather():
    global city
    global old_city
    global rawcity
    try:
        api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" +city+ "&appid=21cab08deb7b27f4c2b55f3e2df28ea4")
        api_output_json=json.loads(api_request.content)
        weather_info=api_output_json['weather'][0]["description"] 
        humidity=api_output_json['main']['humidity'] 
        temp=round(api_output_json['main']['temp']-273)    
        feels=round(api_output_json['main']['feels_like']-273)
        press=round(api_output_json['main']['pressure'])
        wind=round(api_output_json['wind']['speed'],1)
        icon=api_output_json['weather'][0]['icon']
        weather_info_label['text']=str(weather_info)
        humidity_info_label['text']="Humidity: "+str(humidity)+"%"
        feel_info_label['text']="Feels like: "+str(feels)+"°C"
        press_info_label['text']="Pressure: "+str(press)+" hPa"
        speed_info_label['text']="Wind speed: "+str(wind)+"m/s"
        temp_info_label['text']=str(temp)+"°C"
        print("Temperature")
        if(icon=="01d"):
            image['image']=a01d
            sky="lightblue3"
        if(icon=="02d"):
            image['image']=a02d
            sky="lightblue3"
        if(icon=="03d"):
            image['image']=a03d
            sky="lightblue3"
        if(icon=="04d"):
            image['image']=a04d
            sky="lightblue3"
        if(icon=="09d"):
            image['image']=a09d
            sky="lightblue3"
        if(icon=="10d"):
            image['image']=a10d
            sky="lightblue3"
        if(icon=="11d"):
            image['image']=a11d
            sky="lightblue3"
        if(icon=="13d"):
            image['image']=a13d
            sky="lightblue3"
        if(icon=="50d"):
            image['image']=a50d
            sky="lightblue3"
        if(icon=="01n"):
            image['image']=a01n
            sky="#2625a4"
        if(icon=="02n"):
            image['image']=a02n
            sky="#2625a4"
        if(icon=="03n"):
            image['image']=a03n
            sky="#2625a4"
        if(icon=="04n"):
            image['image']=a04n
            sky="#2625a4"
        if(icon=="09n"):
            image['image']=a09n
            sky="#2625a4"
        if(icon=="10n"):
            image['image']=a10n
            sky="#2625a4"
        if(icon=="11n"):
            image['image']=a11n
            sky="#2625a4"
        if(icon=="13n"):
            image['image']=a13n
            sky="#2625a4"
        if(icon=="50n"):
            image['image']=a50n
            sky="#2625a4"        
        root.configure(background=sky)
        city_name.configure(bg=sky)
        weather_info_label.configure(bg=sky)
        temp_info_label.configure(bg=sky)
    except:
        rawcity=old_city
        city_name['text']=rawcity.capitalize()
        messagebox.showinfo("Error","City not found")
def change():
    global city 
    global old_city
    global rawcity
    old_city=rawcity
    rawcity=cityentry.get()
    city_name['text']=rawcity.capitalize()
    city=""
    for i in rawcity:
        if(i==" "):
            city+="%20"
        else:
            city+=i
    cityentry.delete(0,END)
    cityentry.place_forget()
    entrybut.place_forget()
    temp_info_label.place(relx=0.5,rely=0.18,anchor=CENTER) 
    weather()
entrybut=Button(root,text="Change City",command=change)
city_name=Label(root, text=city,font=("Impact", 30,'bold'),bg=sky)
refresh=Button(root,text="Refresh Weather",command=weather)
refresh.place(relx=0.5,rely=0.9,anchor=CENTER)
city_name=Button(root, text=city,font=("Impact", 30,'bold'),bg=sky,command=place,relief=FLAT)
city_name.place(relx=0.5,rely=0.05,anchor=CENTER)
info= Button(root,text="Click here to change city",bg="indianred3",font=("Arial",10,"bold"),command=place)
info.place(relx=0.5,rely=0.13,anchor=CENTER) 
weather()
root.mainloop()