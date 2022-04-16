from tkinter import*
root=Tk()
root.geometry("1366x766")
maincan=Canvas(root,bg="green",width=1366,height=766)
maincan.pack()
im1=PhotoImage(file="C:\\Users\\MUSTAFA\\Desktop\\bank management\\code-wallpaper-11.gif")
maincan.create_image(0,0,anchor=NW,image=im1)
def can2():
    root=Toplevel()
    root.geometry("1366x766")
    root.title("window2")
    global can2
    can2=Canvas(root,bg="green",width=1366,height=766)
    can2.place(x=0,y=0)
    im2=PhotoImage(file=r"mbsa.png")
    can2.create_image(0,0,anchor=NW,image=im2)
    root.mainloop()
bu1=Button(maincan,text="CLICK ME",bg="red",fg="black",command=can2)
bu1.place(x=50,y=100)
bu1.config(font=("helvetica",45))

root.mainloop()
