from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_Ramen.delete(0,END)
    entry_Pizza.delete(0,END)
    entry_Burger.delete(0,END)
    entry_Spagetti.delete(0,END)
    entry_Tacos.delete(0,END)
    entry_Milkshake.delete(0,END)
    entry_Soda.delete(0,END)
    entry_Water.delete(0,END)

def Total():


    try:a1=int(Ramen.get())
    except: a1=0

    try:a2=int(Pizza.get())
    except: a2=0

    try:a3=int(Burger.get())
    except: a3=0

    try:a4=int(Spagetti.get())
    except: a4=0

    try:a5=int(Tacos.get())
    except: a5=0

    try:a6=int(Milkshake.get())
    except: a6=0

    try:a7=int(Soda.get())
    except: a7=0

    try:a8=int(Water.get())
    except: a8=0

    #define cost of each item per quantity
    c1=5.40*a1
    c2=5.00*a2
    c3=4.50*a3
    c4=5.60*a4
    c5=2.30*a5
    c6=1.60*a6
    c7=1.20*a7
    c8=0.80*a8

    lbl_total=Label(f2,font=("aria",20,"bold"),text='TOTAL',width=16,fg="lightblue",bg="black")
    lbl_total.place(x=10,y=70)
    

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg='white')
    entry_total.place(x=20,y=120)

    totalcost=c1+c2+c3+c4+c5+c6+c7+c8
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)

Label(text="ONLINE BILLING SYSTEM",bg="darkblue",fg="white",font=("Gabriola",45),width="300",height="1").pack()

#MENU FOOD AND DRINKS
f=Frame(root,bg="white",highlightbackground="lightblue",highlightthickness=3,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="FOOD & DRINKS",font=("Gabriola",30,"bold"),fg="black",bg="white").place(x=35,y=0)

Label(f,font=("Lucida Calligraphy",12,"bold"),text="1.Ramen................... 5.40$",fg="black",bg="white").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",12,"bold"),text="2.Pizza.................... 5.00$",fg="black",bg="white").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",12,"bold"),text="3.Burger................... 4.50$",fg="black",bg="white").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",12,"bold"),text="4.Spagetti .............. 5.60$",fg="black",bg="white").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",12,"bold"),text="5.Tacos.................... 2.30$",fg="black",bg="white").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",12,"bold"),text="6.Milkshake............. 1.60$",fg="black",bg="white").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",12,"bold"),text="7.Soda..................... 1.20$",fg="black",bg="white").place(x=10,y=260)
Label(f,font=("Lucida Calligraphy",12,"bold"),text="8.Water.................. 0.80$",fg="black",bg="white").place(x=10,y=290)

#BILL
f2=Frame(root,bg="white",highlightbackground='lightblue',highlightthickness=3,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="BILL",font=("Lucida Calligraphy",25),bg="white")
Bill.place(x=100,y=10)

HAGD=Label(f2,text='HAVE A GOOD DAY, THX YOU VERY MUCH',font=("Lucida Calligraphy",8),bg="white")
HAGD.place(x=1,y=300)

#ENTRY WORK
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Ramen=StringVar()
Pizza=StringVar()
Burger=StringVar()
Spagetti=StringVar()
Tacos=StringVar()
Milkshake=StringVar()
Soda=StringVar()
Water=StringVar()
Total_bill=StringVar()

#Label
lbl_Ramen=Label(f1,font=("aria",19,"bold"),text="Ramen",width=12,fg="blue4")
lbl_Pizza=Label(f1,font=("aria",19,"bold"),text="Pizza",width=12,fg="blue4")
lbl_Burger=Label(f1,font=("aria",19,"bold"),text="Burger",width=12,fg="blue4")
lbl_Spagetti=Label(f1,font=("aria",19,"bold"),text="Spagetti",width=12,fg="blue4")
lbl_Tacos=Label(f1,font=("aria",19,"bold"),text="Tacos",width=12,fg="blue4")
lbl_Milkshake=Label(f1,font=("aria",19,"bold"),text="Milkshake",width=12,fg="blue4")
lbl_Soda=Label(f1,font=("aria",19,"bold"),text="Soda",width=12,fg="blue4")
lbl_Water=Label(f1,font=("aria",19,"bold"),text="Water",width=12,fg="blue4")
lbl_Ramen.grid(row=1,column=0)
lbl_Pizza.grid(row=2,column=0)
lbl_Burger.grid(row=3,column=0)
lbl_Spagetti.grid(row=4,column=0)
lbl_Tacos.grid(row=5,column=0)
lbl_Milkshake.grid(row=6,column=0)
lbl_Soda.grid(row=7,column=0)
lbl_Water.grid(row=8,column=0)

#ENTRY
entry_Ramen=Entry(f1,font=("aria",15,"bold"),textvariable=Ramen,bd=6,width=8,bg="lightblue")
entry_Pizza=Entry(f1,font=("aria",15,"bold"),textvariable=Pizza,bd=6,width=8,bg="lightblue")
entry_Burger=Entry(f1,font=("aria",15,"bold"),textvariable=Burger,bd=6,width=8,bg="lightblue")
entry_Spagetti=Entry(f1,font=("aria",15,"bold"),textvariable=Spagetti,bd=6,width=8,bg="lightblue")
entry_Tacos=Entry(f1,font=("aria",15,"bold"),textvariable=Tacos,bd=6,width=8,bg="lightblue")
entry_Milkshake=Entry(f1,font=("aria",15,"bold"),textvariable=Milkshake,bd=6,width=8,bg="lightblue")
entry_Soda=Entry(f1,font=("aria",15,"bold"),textvariable=Soda,bd=6,width=8,bg="lightblue")
entry_Water=Entry(f1,font=("aria",15,"bold"),textvariable=Water,bd=6,width=8,bg="lightblue")
entry_Ramen.grid(row=1,column=1)
entry_Pizza.grid(row=2,column=1)
entry_Burger.grid(row=3,column=1)
entry_Spagetti.grid(row=4,column=1)
entry_Tacos.grid(row=5,column=1)
entry_Milkshake.grid(row=6,column=1)
entry_Soda.grid(row=7,column=1)
entry_Water.grid(row=8,column=1)



#Button
btn_reset=Button(f1,bd=5,fg="black",bg="lightgrey",font=("ariel",16,'bold'),width=10,text="RESET",command=Reset)
btn_reset.grid(row=9,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightgrey",font=("ariel",16,'bold'),width=10,text="TOTAL",command=Total)
btn_total.grid(row=9,column=1)












root.mainloop()
