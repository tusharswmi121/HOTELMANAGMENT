from tkinter import*
root=Tk()
root.title("Genesis")
root.geometry("800x400")
BLUE = "#152bd1"
root.config(bg = BLUE)
mylabel=Label(root,text='HOTEL MANAGMENT',bg='white',fg='black',font=(None,30)).pack()
e=Entry(root,bg='blue',width=67)
e.pack()
def func1():
    global root1,f11
    root1=Tk()
    root1.geometry("900x600")    
    l11=Label(root1,text="enter your name=",fg='black',font=(None,15),padx=20,pady=40).grid(row=2,column=2)
    f11=Entry(root1,width=40,borderwidth=10).grid(row=2,column=4)
    l12=Label(root1,text="enter your address=",fg='black',font=(None,15),padx=20,pady=40).grid(row=4,column=2)
    f12=Entry(root1,width=40,borderwidth=10).grid(row=4,column=4)
    l13=Label(root1,text="enter your phone number=",fg='black',font=(None,15),padx=20,pady=40).grid(row=6,column=2)
    f13=Entry(root1,width=40,borderwidth=10).grid(row=6,column=4)
    l14=Label(root1,text="choose room:",fg='black',font=(None,20)).grid(row=8,column=2)
    Variable=StringVar(root1)
    Variable.set("option")
    f14=OptionMenu(root1,Variable,'normal room','loby room','luxiries room')
    f14.grid(row=9,column=2)
    l15=Label(root1,text="choose payment mode:",padx=40,pady=20,fg='black',font=(None,20)).grid(row=11,column=2)
    Variable1=StringVar(root1)
    Variable1.set("option")
    f15=OptionMenu(root1,Variable1,'online','debit card','cash')
    f15.grid(row=12,column=2) 
    def f113():
        global root12
        root12=Tk()
        root12.geometry("550x150")
        root12.config(bg='#302b2b')
        l111=Label(root12,text="your information is submitted suceesfully",padx=40,pady=20,font=(None,20)).grid(row=4,column=4)   
        root1.destroy()  
        root12.mainloop()
    b13=Button(root1,text="submit",padx=40,pady=8,command=f113,bg='blue',fg='white').grid(row=16,column=10)
    root1.mainloop()
    
b1=Button(root,text="check in",padx=201,pady=10,command=func1,fg="black",bg="white").pack()
e=Entry(root,bg='blue',width=75)
e.pack()
def func2():
    global root2 
    root2=Tk()
    root2.config(bg='#a82585')
    root2.geometry("650x250")
    label3=Label(root2,text="ENTER THE ROOM NO :::",padx=15,pady=5,width=20)
    label3.place(x=50,y=10)
    f21=Entry(root2,width=30,borderwidth=10).place(x=250,y=10)
    root2.mainloop()
    def fb23():
        global root21
        root21=Tk()
        root21.geometry("650x250")
        l231=Label(root21,text="-------------------",bg='white',font=(None,30)).grid(row=3,column=4)
        l232=Label(root21,text="you are checked out",padx=70,pady=20,font=(None,30)).grid(row=4,column=4)
        l233=Label(root21,text="-------------------",bg='white',font=(None,30)).grid(row=5,column=4)
    b23=Button(root2,text="CHECK OUT",command=fb23,fg='white',bg='black',padx=30,pady=10).grid(row=12,column=5)
    root21.mainloop()
    
    
b3=Button(root,text='check out',padx=200,pady=10,command=func2,fg='black',bg='white').pack()
e=Entry(root,bg='blue',width=75)
e.pack()
def func3():
    global root3
    root3=Tk()
    root3.geometry("650x250")
    label4=Label(root3,text="you entered show guest list").pack()
    root3.mainloop()
b4=Button(root,text='show guest list',padx=185,pady=10,command=func3,fg='black',bg='white').pack()
e=Entry(root,bg='blue',width=75)
e.pack()
def func4():
    global root4
    root4=Tk()
    root4.geometry("650x250")
    label5=Label(root4,text="GET INFO HERE ..!!",padx=20,pady=8,fg='black',font=(None,20)).grid(row=2,column=4)
    label6=Label(root4,text='ENTER THE ROOM NO ::',padx=10,pady=10).grid(row=5,column=2)
    f41=Entry(root4,width=40,borderwidth=10).grid(row=5,column=4)
    b41=Button(root4,text="SUBMIT",bg='green',fg='white',padx=30,pady=8).grid(row=6,column=5)
    root4.mainloop()
b5=Button(root,text='fetch guest info',command=func4,padx=187,pady=10,fg='black',bg='white').pack()
e=Entry(root,bg='blue',width=75)
e.pack()

b6=Button(root,text='exit',command=root.destroy,padx=100,pady=10,fg='black',bg='red').pack()

root.mainloop()


        

    










