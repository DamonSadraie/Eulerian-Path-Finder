from tkinter import *
from maincode import *
import subprocess

root = Tk()
root.geometry("840x400")
def shutgun():
    try:
        inputk=int(e2.get())
        inputtext=e1.get()
        #L3=Label(root,text=getkmers(userinput,4)).grid(row=4,column=0)
        B=str(getkmers(inputtext,inputk))
        e3["state"]="normal"
        e3.delete(0,"end")
        e3.insert(0,B)
        e3["state"]="readonly"
        but2["state"]="normal"
        but3["state"]="normal"
    except ValueError:
        L2.config(text="Set The Length Of Kmers. That's Not A Number.")
    return
def copy2clip():
    txt=e3.get()
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
def copyShutgun():
    if e4.get() == "":
        e3["state"]="normal"
        e4.insert(0,e3.get())
        e3["state"]="readonly"
    else:
        but3.config(text="Previous Shotgun\nClear Box First")
    return
def reconstruct():
    e5["state"]="normal"
    e5.delete(0,END)
    str1=e4.get()
    list1=stringToList(e4.get())
    list2=program(list1)
    e5.insert(0,list2[1])
    e5["state"]="readonly"
    but5["state"]="normal"
    L4.config(text=list2[0])
    return
def copy2clip2():
    e5["state"]="normal"
    txt=e5.get()
    e5["state"]="readonly"
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

L1=Label(root,text="Enter Text Below To Shotgun")
L2=Label(root,text="Set The Length Of Kmers.                     ")
L3=Label(root,text="Reconstruct Text. Enter List of Kmers Below:")
L4=Label(root,text="")
L1.grid(row=0,column=0)
L2.grid(row=0,column=1)
L3.grid(row=5,column=0)
L4.grid(row=9,column=0)


e1=Entry(root,width=100)
e2=Entry(root,width=30)
e3=Entry(root,width=100,state="readonly")
e4=Entry(root,width=100)
e5=Entry(root,width=100,state="readonly")
e1.grid(row=1,column=0)
e2.grid(row=1,column=1)
e3.grid(row=3,column=0)
e4.grid(row=6,column=0)
e5.grid(row=8,column=0,columnspan = 2)

but1=Button(root,text="ok",padx=350,pady=10,command=shutgun,fg="blue",bg="grey")
but2=Button(root,text="copy",padx=70,pady=2,command=copy2clip,fg="blue",bg="grey",state=DISABLED)
but3=Button(root,text="Previous Shotgun",state=DISABLED,padx=20,pady=10,command=copyShutgun,fg="blue",bg="grey")
but4=Button(root,text="Reconstruct",padx=20,pady=10,command=reconstruct,fg="blue",bg="grey")
but5=Button(root,text="copy",padx=70,pady=2,command=copy2clip2,fg="blue",bg="grey",state=DISABLED)
but1.grid(row=4,column=0,columnspan = 2)
but2.grid(row=3,column=1)
but3.grid(row=6,column=1)
but4.grid(row=7,column=0,columnspan = 2)
but5.grid(row=9,column=1)


root.mainloop()