import pyqrcode
import os
import png
from tkinter import*
root=Tk()
root.title("QR Code generator")
root.geometry("600x150")
root.resizable(0,0)
path=os.path.dirname(os.path.realpath('QR Code '))

cn=Canvas(root,bg="black",width=600,height=150)
cn.place(x=0,y=0)

lb1=Label(root,text="Enter  Link :",width=20,bg="black",fg="yellow")
lb1.place(x=10,y=10)
lb1.config(font=("Corbel",18))
lb2=Label(root,
text="( EX :-- www.python.org.  Please Enter a valid link )",
bg="black",fg="yellow")
lb2.place(x=240,y=45)

def fetch():
    s=entry.get()
    qr=pyqrcode.create(s)
    qr.png('{}\\myqr5.png'.format(path),scale=6)
    root.destroy()
    
    wn=Tk()
    wn.title("QR Code")
    wn.geometry("400x400")
    wn.resizable(0,0)
    cn1=Canvas(wn,bg="black",width=400,height=400)
    cn1.place(x=0,y=0)
    qr_photo=PhotoImage(file="{}\\myqr5.png".format(path))
    cn1.create_image(205,80,anchor=N,image=qr_photo) 
    wn.mainloop()
    
but_1=Button(root,text="GENERATE",width=25,bg="gray63",bd=5,command=fetch)
but_1.place(x=240,y=70)
but_1.config(font=("Corbel",15))

entry=Entry(root,width=27)
entry.place(x=240,y=10)
entry.config(font=("Corbel",19))
entry.focus()




