from tkinter import*
sqr=Tk()
sqr.title("SECURITY QUESTION")
sqr.geometry("480x300+50+150")
sqr.resizable(0,0)
steve=Canvas(sqr,width=1366,height=769,bg="black")
steve.place(x=0,y=0)                              ######################################  pyimag6 doesn't exist.FIND THE WAY TO USE ANOTHER IMAGE IN ANOTHER TKINTER WINDOW
lab1=Label(steve,text="PLEASE SELECT THE SECURITY QUESTIONS",bg="black",fg="yellow")
lab1.place(x=40,y=5)  
lab1.config(font=("Algerian",15))
steve.create_line(90,40,400,40,fill="yellow")
steve.create_line(130,44,360,44,fill="yellow")
steve.create_line(30,0,30,40,fill="yellow")
steve.create_line(450,0,450,44,fill="yellow")
options=["What is your favorite place?","What is your favorite movie?","Who is your favorite author?","Which car is your favorite?","What was the make of your first motorcycle?"]
po=StringVar()
po.set("1.Question")
op=OptionMenu(sqr,po,*options)
op.place(x=30,y=60)
op.config(font=("Algerian",15))                
sqr.mainloop()