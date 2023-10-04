import tkinter
from tkinter import*
root=Tk()
root.title("Simple Caluclator")
root.geometry("370x400")
root.configure(bg='black')
label1=Label(root,text="CALCULATOR",bg="black",fg="white",font=("bold",30,'italic'))
label1.pack(side=TOP)
textin=StringVar()
operator=""
def clickbut(number):     #lambda:clickbut(1)
    global operator
    operator=operator+str(number)
    textin.set(operator)
def equalbutt():
    global operator
    add=str(eval(operator))     
    textin.set(add)
    operator=''
def equalbutt():
    global operator
    sub=str(eval(operator)) 
    textin.set(sub)
    operator=''
def equalbutt():
    global operator
    mul=str(eval(operator)) 
    textin.set(mul)
    operator=''
def equalbutt():
    global operator
    div=str(eval(operator)) 
    textin.set(div)
    operator='' 
def clrbut():
    textin.set('')
text=Entry(root,font=("times",12,'bold'),textvar=textin,width=50,bd=5,bg='white')
text.pack()
but1=Button(root,padx=17,pady=14,bd=4,bg='lightblue',command=lambda:clickbut(1),text="1",font=("Europian",16,'bold'))
but1.place(x=10,y=240)
but2=Button(root,padx=17,pady=14,bd=4,bg='lightblue',command=lambda:clickbut(2),text="2",font=("Europian",16,'bold'))
but2.place(x=75,y=240)
but3=Button(root,padx=17,pady=14,bd=4,bg='lightblue',command=lambda:clickbut(3),text="3",font=("Europian",16,'bold'))
but3.place(x=140,y=240)
but4=Button(root,padx=17,pady=14,bd=4,bg='lightblue',command=lambda:clickbut(4),text="4",font=("Europian",16,'bold'))
but4.place(x=10,y=170)
but5=Button(root,padx=17,pady=14,bd=4,bg='lightblue',command=lambda:clickbut(5),text="5",font=("Europian",16,'bold'))
but5.place(x=75,y=170)
but6=Button(root,padx=17,pady=14,bd=4,bg='lightblue',command=lambda:clickbut(6),text="6",font=("Europian",16,'bold'))
but6.place(x=140,y=170)
but7=Button(root,padx=17,pady=14,bd=4,bg='lightblue',command=lambda:clickbut(7),text="7",font=("Europian",16,'bold'))
but7.place(x=10,y=100)
but8=Button(root,padx=17,pady=14,bd=4,bg='lightblue',command=lambda:clickbut(8),text="8",font=("Europian",16,'bold'))
but8.place(x=75,y=100)
but9=Button(root,padx=17,pady=14,bd=4,bg='lightblue',command=lambda:clickbut(9),text="9",font=("Europian",16,'bold'))
but9.place(x=140,y=100)
but0=Button(root,padx=17,pady=14,bd=4,bg='lightblue',command=lambda:clickbut(0),text="0",font=("Europian",16,'bold'))
but0.place(x=75,y=310)
butdot=Button(root,padx=20,pady=14,bd=4,bg='lightblue',command=lambda:clickbut("."),text=".",font=("Times",16,'bold'))
butdot.place(x=10,y=310)
butp1=Button(root,padx=16.6,pady=14,bd=4,bg='lightblue',command=lambda:clickbut("+"),text="+",font=("Times",16,'bold'))
butp1.place(x=205,y=100)
butsub=Button(root,padx=17,pady=14,bd=4,bg='lightblue',command=lambda:clickbut("-"),text=" -",font=("Times",16,'bold'))
butsub.place(x=205,y=170)
butmul=Button(root,padx=16.6,pady=14,bd=4,bg='lightblue',command=lambda:clickbut("*"),text="*",font=("Times",16,'bold'))
butmul.place(x=205,y=240)
butdiv=Button(root,padx=14,pady=14,bd=4,bg='lightblue',command=lambda:clickbut("/"),text=" / ",font=("Times",16,'bold'))
butdiv.place(x=205,y=310)
butclear=Button(root,padx=14,pady=119,bd=4,bg='lightblue',command=clrbut,text="CE",font=("Times",16,'bold'))
butclear.place(x=270,y=100)
buteqql=Button(root,padx=17,pady=14,bd=4,bg='lightblue',command=equalbutt,text="=",font=("Times",16,'bold'))
buteqql.place(x=140,y=310)
root.mainloop()
