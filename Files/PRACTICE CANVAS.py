from tkinter import*
import time
root=Tk()
root.geometry("1366x769+0+0")
root.title("PLASMA'Z software")
frame=Canvas(root,bg="green",width=1366,height=769)
frame.place(x=0,y=0)
p=Label(root,text=" ",bg="yellow",fg="red")
p.place(x=250,y=200)
p.config(font=("helvetica",40))
x=Canvas(root,bg="blue4",width=500,height=500)
x.place(x=100,y=150)
b5=x.create_line(100,20,100,500,fill="black",width=15)
b6=x.create_line(50,100,200,100,fill="black",width=15)


root.mainloop()
