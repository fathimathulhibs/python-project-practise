from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
from PIL import Image,ImageTk
import time
from tkinter import messagebox
root=Tk()
root.title("Transly")
root.geometry("650x650")
root.maxsize(650,650)
root.minsize(650,650)
root.configure(bg="seagreen")

head=Label(root,text="Transly",font=("Tahoma",30,'bold'),bg="pale violet red",fg="#1F2937")
head.place(relx=0.5,rely=0.1,anchor=CENTER)

sw= ImageTk.PhotoImage(Image.open ("switch.png"))

Langer=["Detect Language"]
Langer.extend(list(LANGUAGES.values()))
Lang=[]

for i in Langer:
    Lang.append(i.capitalize())
langer=list(LANGUAGES.values())
lang=[]
for i in langer:
    lang.append(i.capitalize())

drop1=ttk.Combobox(root,state="readonly",values=Lang,width=25)
drop1.place(relx=0.2,rely=0.2,anchor=CENTER)    
drop1.set("Detect Language")

drop2=ttk.Combobox(root,state="readonly",values=lang,width=25)
drop2.place(relx=0.8,rely=0.2,anchor=CENTER)
drop2.set("English")

text1=Text(root,bg="#3B82F6",padx=10,pady=10, wrap=WORD,bd=0,font=("Helvectica",16))
text1.place(relx=0.02,rely=0.6,anchor=W,width=300,height=400)

text2=Text(root,bg="#3B82F6",width=35,padx=10,pady=10, wrap=WORD,bd=0,font=("Helvectica",16))
text2.place(relx=0.98,rely=0.6,anchor=E,width=300,height=400)

def Translate():
    try:
        if(drop1.get()=="Detect Language"):
            Trans=Translator()
            translated=Trans.translate(text=text1.get(1.0,END),dest=drop2.get())
            text2.delete(1.0,END)
            text2.insert(END,translated.text)
        else:
            Trans=Translator()
            translated=Trans.translate(text=text1.get(1.0,END),src=drop1.get(),dest=drop2.get())
            text2.delete(1.0,END)
            text2.insert(END,translated.text)
    except:
        time.sleep(0.1)
    root.after(1000,Translate)
def switch():        
    lang1=drop1.get()
    lang2=drop2.get()
    if(lang1!="Detect Language"):
        info1=text1.get(1.0,END)
        info2=text2.get(1.0,END)
        lang1,lang2=lang2,lang1
        info1,info2=info2,info1
        text1.delete(1.0,END)
        text2.delete(1.0,END)
        text1.insert(END,info1)
        text2.insert(END,info2)
        drop1.set(lang1)
        drop2.set(lang2)
    else:
        messagebox.showinfo("Error","Languages cannot be switched if 'Detect Language' is chosen")
Translate()
switch=Button(root,image=sw,command=switch)
switch.place(relx=0.5,rely=0.2,anchor=CENTER)
root.mainloop()                 