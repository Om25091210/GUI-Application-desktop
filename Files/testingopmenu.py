from tkinter import*
root=Tk()
def oio():
    print(c.get())
options=["6th","7th","8th","9th","10th","11th","12th"]
c=StringVar()
c.set("CLASS")
o=OptionMenu(root,c,*options)
o.pack()
print(c.get())
sa=Button(root,text="SUBMIT",command=oio)
sa.place(x=50,y=50)
root.mainloop()
