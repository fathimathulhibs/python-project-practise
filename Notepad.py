from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from tkinter import messagebox 
import webbrowser
from tkinter import ttk
from tkinter import font
import time
root = Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.title('Untitled.txt \t \t \t \t Super Notepad')
root.configure(bg="black")

open_img = ImageTk.PhotoImage(Image.open ("open.png"))
save_img = ImageTk.PhotoImage(Image.open ("save.png"))
exit_img = ImageTk.PhotoImage(Image.open ("exit.jpg"))
run_img = ImageTk.PhotoImage(Image.open ("run.png"))
b= ImageTk.PhotoImage(Image.open ("bold.jpg"))
i = ImageTk.PhotoImage(Image.open ("italic.jpg"))
s = ImageTk.PhotoImage(Image.open ("strikethrough.jpg"))
u = ImageTk.PhotoImage(Image.open ("underline.jpg"))

family=""
size=""
def styling(*args):
    global fontes
    family=dropdown.get()
    size=str(number.get())
    if(size==""):
        size='12'
    if(family==""):
        family="Arial"
    if(size.isdigit()==True):
        fontes.configure(family=family,size=size)
    else:
        messagebox.showinfo("Error","Please enter integer values.")
fontes=font.Font(weight="normal",slant="roman",underline=0,overstrike=0)
def bold():
    global fontes
    fontes.configure(weight="bold" if fontes.cget("weight")=="normal" else "normal")
def under():
    global fontes
    fontes.configure(underline=1 if fontes.cget("underline")==0 else 0)
def over():
    global fontes
    fontes.configure(overstrike=1 if fontes.cget("overstrike")==0 else 0)
def italic():
    global fontes
    fontes.configure(slant="italic" if fontes.cget("slant")=="roman" else "roman")
hr=Label(root,width=91,height=3,bg="dodgerblue")
hr.place(relx=0.5,rely=0.1,anchor=CENTER)
my_text= Text(root)
my_text.place(relx=0.5,rely=0.63,width=645,height=490,anchor= CENTER)

style= Label(root,text="Styling Tab",height=1,width=53,bg="tomato",font=("Helvetica",15,"bold"))
style.place(relx=0.5,rely=0.03,anchor= CENTER)

fonts=["Arial", "Verdana", "Segoe UI", "Tahoma","Calibri", "Times New Roman", "Georgia", "Garamond", "Palatino","Palatino Linotype", "Courier New", "Consolas", "Lucida Console", "Impact","Jokerman", "Franklin Gothic Medium","Trebuchet MS"]
dropdown=ttk.Combobox(root,values=fonts,state="readonly",width=10)
dropdown.place(relx=0.2,rely=0.1, anchor=CENTER)
dropdown.set("Arial")
drop_label=Label(root,text="Font Family",font=("Verdana",8),bg="orangered")
drop_label.place(relx=0.07,rely=0.1,anchor=CENTER)
dropdown.bind("<<ComboboxSelected>>",styling)

fonter=StringVar()
fonter.trace_add("write",styling)
number=Entry(root,textvariable=fonter,width=10)
number.place(relx=0.45,rely=0.1, anchor=CENTER)
number.insert(0,12)
num_label=Label(root,text="Font Size",font=("Verdana",8),bg="orangered")
num_label.place(relx=0.34   ,rely=0.1,anchor=CENTER)
number.configure(relief='raised')

name = ""
text_file=''
opene=0
checker=BooleanVar()
saver=BooleanVar()
checked=0
def openFile():
    global checked
    global text_file
    global name
    global opene
    my_text.delete(1.0, END)
    if(checked==False):
        root.title("Untitled. txt \t \t \t \t Super Notepad")
        text_file = filedialog.askopenfilename(title=" Open Text File", filetypes=(("Text Files", "*. txt \t \t \t \t Super Notepad"),))
    else:
        root.title("Untitled. html \t \t \t \t Super Notepad")
        text_file = filedialog.askopenfilename(title=" Open HTML File", filetypes=(("HTML Files", "*.html"),))
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    if(name!=""):
        opene=1
        root.title(name+" \t \t \t \t Super Notepad")
    else:
        opene=0
    file=open(text_file,'r')
    paragraph=file.read()
    my_text.insert(END,paragraph)
    file.close()

def save(): 
    global text_file
    global name
    global opene
    global checked
    if(opene==1):   
        file=open(text_file,'w')
        file.write(my_text.get("1.0",END))
        file.close()
    else:    
        if(checked==False):
            text_file=filedialog.asksaveasfilename(defaultextension=".txt")
        else:    
            text_file=filedialog.asksaveasfilename(defaultextension="*.html")
        file=open(text_file,'w')
        file.write(my_text.get('1.0',END))
        file.close()
        messagebox.showinfo("Saved Successfully","Your File has been saved successfully.")
def close():
    global opene
    global checked
    if(opene==1):   
        ans=messagebox.askyesnocancel("Notepad","Do you want to save changes before leaving?")
        if(ans==True):
            save()
            opene=0        
            my_text.delete(1.0,END)
        if(ans==False):
            opene=0
            my_text.delete(1.0,END)
    else:
        my_text.delete(1.0,END)
def html():
    global checked
    if(opene==0):
        checked=checker.get()
        if(checked==True):
            start.place(relx=0.33,rely=0.17,anchor=CENTER)
            labe.place(relx=0.33,rely=0.22,anchor=CENTER)
            root.title("Untitled. html \t \t \t \t Super Notepad")
        else:
            start.place_forget()
            labe.place_forget()
            root.title("Untitled. txt \t \t \t \t Super Notepad")
    else:
        messagebox.showinfo("ERROR","Mode cannot be changed while a file is opened")
        checkbox.toggle()
        checked=False
def autosave():
    if(opene==1):
        if(saved==1):        
            file=open(text_file,'w')
            file.write(my_text.get("1.0",END))
            file.close()
    root.after(10000,autosave)
def checkboxer():
    global saved
    if(saver.get()==True):
        saved=1
        autosave()
    else:
        saved=0
def starting():
    global text_file
    webbrowser.open(text_file)

my_text= Text(root,font=fontes)
my_text.place(relx=0.5,rely=0.63,width=645,height=490,anchor= CENTER)

open_button=Button(root,image=open_img, command=openFile)
open_button.place(relx=0.05,rely=0.17,anchor=CENTER)
save_button=Button(root, image=save_img, command=save)
save_button.place(relx=0.15,rely=0.17,anchor= CENTER)
exit_button=Button(root,image=exit_img,command=close)
exit_button.place(relx=0.24,rely=0.17,anchor= CENTER)
start=Button(root,image=run_img,command=starting)

open_label=Button(root,text="Open File",command=openFile)
open_label.place(relx=0.05,rely=0.22,anchor=CENTER)
save_label=Button(root,text="Save File",command=save)
save_label.place(relx=0.15,rely=0.22,anchor= CENTER)
exit_label=Button(root,text="Exit File",command=close)
exit_label.place(relx=0.24,rely=0.22,anchor= CENTER)
labe=Button(root,text="Run File",command=starting)

checkbox=Checkbutton(root,text="HTML Mode",variable=checker,command=html)
checkbox.place(relx=0.83, rely=0.15)
autosaver=Checkbutton(root,text="Autosave",variable=saver,command=checkboxer)
autosaver.place(relx=0.83, rely=0.2)

bo=Button(root,image=b, command=bold)
bo.place(relx=0.8,rely=0.1,anchor=CENTER)
it=Button(root, image=i, command=italic)
it.place(relx=0.85,rely=0.1,anchor= CENTER)
ul=Button(root,image=u,command=under)
ul.place(relx=0.9,rely=0.1,anchor= CENTER)
st=Button(root,image=s,command=over)
st.place(relx=0.95,rely=0.1,anchor=CENTER)
root.mainloop() 