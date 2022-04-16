from tkinter import*
can_wd=500
can_ht=150
def paint(event):
    python_green="#478487"
    x1,y1=(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)
    w.create_oval(x1,y1,x2,y2,fill=python_green)
root=Tk()
root.title("painting using ovals")
w=Canvas(root,width=can_wd,height=can_ht)
w.pack(expand=YES,fill=BOTH)
w.bind("<B1-Motion>",paint)
message=Label(root,text="press and drag the mouse to draw")
message.pack(side=BOTTOM)
mainloop()
