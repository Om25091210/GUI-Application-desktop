from tkinter import*
import math
from tkinter import messagebox
root=Tk()
root.title("CALCULATOR")
root.geometry("440x540")
root.resizable(0,0)
global history
history=[]
li=[]
#1...canvas........................................................###
r=Canvas(root,width=600,height=600,bg="black")
r.place(x=0,y=0)
#2canvas..################################################################
r1=Canvas(root,width=600,height=200,bg="medium turquoise")
r1.place(x=0,y=0)
#3..........entry################################################
var=StringVar()
#3333333
entry=Entry(root,bg="medium turquoise",fg="blue2",width=24,textvariable=var,justify=RIGHT)
entry.place(x=3,y=30)
entry.config(font=("HELVETICA",24))
if entry.get()=="":
    var.set("0")
####################################################################!!!!!!!!!!!!!!!!!!!!!!FUNCTION BLOCKS..
#4..........buttons############################################..BF
def buttons(number):
    global k
    k=entry.get()
    k=k+str(number)
    if k[0]=="0":
        k=k[1:]
    var.set(k)
#history========================================================
def sc():
    global txt
    txt=Tk()
    txt.title("STORE")
    txt.resizable(0,0)
    scroll=Scrollbar(txt)
    scroll.pack(side=RIGHT,fill=Y)
    txt.geometry("400x400+400+150")
    txt1=Text(txt,width=500,height=450,bg="navy",fg="yellow",font="courier",selectbackground="red",yscrollcommand=scroll.set)
    scroll.config(command=txt1.yview)
    txt1.insert(INSERT,"                                    \n")
    txt1.insert(INSERT,"                                    \n")
    txt1.insert(INSERT,"-------------------------------------\n")
    txt1.insert(INSERT,"===============HISTORY===============\n")
    txt1.insert(INSERT,"EXPRESSION            \n")
    try:
       for i in range(0,len(history)):
           txt1.insert(INSERT,"{}:  {}=  {}\n".format(i+1,history[i],li[i]))
           txt1.insert(INSERT,"                        \n")
    except:
        print("")
    def c1():
        history.clear()
        li.clear()
        
    def c2():
        txt.destroy()
    c=Button(txt,width=14,text="Clear",bg="black",fg="yellow",command=c1)
    c.place(x=0,y=0)
    e=Button(txt,width=14,text="Exit",bg="black",fg="yellow",command=c2)
    e.place(x=200,y=0)
    e.config(font=("algerian",17))
    c.config(font=("algerian",17))
    txt1.place(x=0,y=0)
    txt.mainloop()
#==scroll=========================================================================================================
scr=Button(root,text="HISTORY",bg="gray25",fg="white",width=9,command=sc)
scr.place(x=4,y=478)
scr.config(font=("algerian",22))
def sqrt():      
    m=entry.get()
    n=float(m)
    d=n**(1/2)
    o=str(d)
    entry.delete(0,'end')
    entry.insert(0,o)
def power():
    entry.insert(len(entry.get()),'**')
    
def result():
    global res
    w=entry.get()
    history.append(entry.get())
    #double --
    try:
       global res
       res=eval(w)
       li.append(res)
    except:
        messagebox.showwarning('Error',"INVALID INPUT")
    entry.delete(0,'end')
    try:
       var.set(res)
    except:
        print("")
def clear():
    l=len(entry.get())
    if l==1:
        entry.delete(0,"end")
        entry.insert(0,'0')
        var.set("0")
    else:
        entry.delete(l-1,l)
def acclear():
    res=""
    var.set("")
    if entry.get()=="":
       var.set("0")

    
########################################################...EVENTS
def b1(event):
    but1['bg']="gray25"
def b11(event):
    but1['bg']="black"
def b2(event):
    but2['bg']="gray25"
def b22(event):
    but2['bg']="black"
def b3(event):
    but3['bg']="gray25"
def b33(event):
    but3['bg']="black"
def b4(event):
    but4['bg']="gray25"
def b44(event):
    but4['bg']="black"
def b5(event):
    but5['bg']="gray25"
def b55(event):
    but5['bg']="black"
def b6(event):
    but6['bg']="gray25"
def b66(event):
    but6['bg']="black"
def b7(event):
    but7['bg']="gray25"
def b77(event):
    but7['bg']="black"
def b8(event):
    but8['bg']="gray25"
def b88(event):
    but8['bg']="black"
def b9(event):
    but9['bg']="gray25"
def b99(event):
    but9['bg']="black"
def b0(event):
    but0['bg']="gray25"
def b00(event):
    but0['bg']="black"
def bp(event):
    butp['bg']="gray25"
def bpp(event):
    butp['bg']="black"
def be(event):
    bute['bg']="green2"
def bee(event):
    bute['bg']="orange"
def bpl(event):
    butpl['bg']="blue2"
def bplpl(event):
    butpl['bg']="dodger blue"
def bc(event):
    butc['bg']="blue2"
def bcc(event):
    butc['bg']="dodger blue"
######################################OPERATORS BIND EVENTS
def p1(event):
    plus['bg']="gray25"
def p11(event):
    plus['bg']="black"
def m1(event):
    minus['bg']="gray25"
def m11(event):
    minus['bg']="black"
def mul1(event):
    mul['bg']="gray25"
def mul11(event):
    mul['bg']="black"
def div1(event):
    div['bg']="gray25"
def div11(event):
    div['bg']="black"
def sq1(event):
    sq['bg']="gray25"
def sq11(event):
    sq['bg']="black"
def po1(event):
    po['bg']="gray25"
def po11(event):
    po['bg']="black"
##############################################################/...............END
but1=Button(root,text="1",width=4,bg="black",fg="white",command=lambda:buttons(1),font=("helvetica",25))
but1.place(x=5,y=205)
#5...event1...........
but1.bind('<Enter>',b1)
but1.bind('<Leave>',b11)

but2=Button(root,text="2",width=4,bg="black",fg="white",command=lambda:buttons(2),font=("helvetica",25))
but2.place(x=91,y=205)
#5...event2...........
but2.bind('<Enter>',b2)
but2.bind('<Leave>',b22)

but3=Button(root,text="3",width=4,bg="black",fg="white",command=lambda:buttons(3),font=("helvetica",25))
but3.place(x=177,y=205)
#5...event3...........
but3.bind('<Enter>',b3)
but3.bind('<Leave>',b33)

but4=Button(root,text="4",width=4,bg="black",fg="white",command=lambda:buttons(4),font=("helvetica",25))
but4.place(x=5,y=272)
#5...event4...........
but4.bind('<Enter>',b4)
but4.bind('<Leave>',b44)

but5=Button(root,text="5",width=4,bg="black",fg="white",command=lambda:buttons(5),font=("helvetica",25))
but5.place(x=91,y=272)
#5...event5...........
but5.bind('<Enter>',b5)
but5.bind('<Leave>',b55)

but6=Button(root,text="6",width=4,bg="black",fg="white",command=lambda:buttons(6),font=("helvetica",25))
but6.place(x=177,y=272)
#5...event6...........
but6.bind('<Enter>',b6)
but6.bind('<Leave>',b66)

but7=Button(root,text="7",width=4,bg="black",fg="white",command=lambda:buttons(7),font=("helvetica",25))
but7.place(x=5,y=339)
#5...event7...........
but7.bind('<Enter>',b7)
but7.bind('<Leave>',b77)

but8=Button(root,text="8",width=4,bg="black",fg="white",command=lambda:buttons(8),font=("helvetica",25))
but8.place(x=91,y=339)
#5...event8...........
but8.bind('<Enter>',b8)
but8.bind('<Leave>',b88)

but9=Button(root,text="9",width=4,bg="black",fg="white",command=lambda:buttons(9),font=("helvetica",25))
but9.place(x=177,y=339)
#5...event9...........
but9.bind('<Enter>',b9)
but9.bind('<Leave>',b99)

but0=Button(root,text="0",width=4,bg="black",fg="white",command=lambda:buttons(0),font=("helvetica",25))
but0.place(x=91,y=406)
#5...event9...........
but0.bind('<Enter>',b0)
but0.bind('<Leave>',b00)
########.....................................................................................
butp=Button(root,text=".",width=4,bg="black",fg="white",command=lambda:buttons("."),font=("helvetica",25))
butp.place(x=177,y=406)
#5...event9...........
butp.bind('<Enter>',bp)
butp.bind('<Leave>',bpp)
#####################################################========================================

bute=Button(root,text="=",width=4,height=4,bg="orange",fg="white",command=result,font=("helvetica",25))
bute.place(x=352,y=354)
#5...event9...........
bute.bind('<Enter>',be)
bute.bind('<Leave>',bee)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.....OPERATORS BUTTON

#@@@@@@@@@@@@@@@@@@@...........................AC........
butpl=Button(root,text="AC",width=4,bg="dodger blue",fg="white",command=acclear,font=("helvetica",25))
butpl.place(x=5,y=406)
#5...event9...........
butpl.bind('<Enter>',bpl)
butpl.bind('<Leave>',bplpl)
#@@@@@@@@@@@@@@@@@@@..........................<--........BACK ONE STEP:::
butc=Button(root,text="<",width=4,height=3,bg="dodger blue",fg="white",command=clear,font=("helvetica",25))
butc.place(x=352,y=209)
#5...event9...........
butc.bind('<Enter>',bc)
butc.bind('<Leave>',bcc)
#########################################
#######################################
####################################################OPERATORS........
#PLUS++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
plus=Button(root,text="+",width=4,bg="black",fg="white",command=lambda:buttons("+"),font=("helvetica",25))
plus.place(x=263,y=205)
#5...event1...........
plus.bind('<Enter>',p1)
plus.bind('<Leave>',p11)
#MINUS--------------------------------------------------------------------
minus=Button(root,text="-",width=4,bg="black",fg="white",command=lambda:buttons("-"),font=("helvetica",25))
minus.place(x=263,y=272)
#5...event1...........
minus.bind('<Enter>',m1)
minus.bind('<Leave>',m11)
#multiply*****************************************************************
mul=Button(root,text="x",width=4,bg="black",fg="white",command=lambda:buttons("*"),font=("helvetica",25))
mul.place(x=263,y=339)
#5...event9...........
mul.bind('<Enter>',mul1)
mul.bind('<Leave>',mul11)
#DIVISION/////////////////////////////////////////////////////////////////
div=Button(root,text="/",width=4,bg="black",fg="white",command=lambda:buttons("/"),font=("helvetica",25))
div.place(x=263,y=406)
#5...event9...........
div.bind('<Enter>',div1)
div.bind('<Leave>',div11)
#SQUARE ROOT##############################################################
sq=Button(root,text="√",width=4,bg="black",fg="white",command=sqrt,font=("helvetica",25))
sq.place(x=264,y=473)
#5...event9...........
sq.bind('<Enter>',sq1)
sq.bind('<Leave>',sq11)
#power_+___+_+____________________________________________________________
po=Button(root,text="x^a",width=4,bg="black",fg="white",command=power,font=("helvetica",25))
po.place(x=178,y=473)
#5...event9...........
po.bind('<Enter>',po1)
po.bind('<Leave>',po11)
#####################################HISTORY

root.mainloop()
