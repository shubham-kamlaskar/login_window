from tkinter import *


root = Tk()

root.title("Login Window")
root.resizable(False,False)
#to add backgroud image
filename = PhotoImage(file = "C:\\Users\\shubham\\Downloads\\wp.gif")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def SubMit():
    if E1.get() == "Shubham" and E2.get() == "1234" :
        print(L5.config(text="Login successful !"))
        E1.delete(0,END)
        E2.delete(0,END)
    else  :
        print(L5.config(text="Login Failed !"))
        E1.delete(0,END)
        E2.delete(0,END)

root1= ''

def ForGot_L():
    global B8
    global L9
    root1= Toplevel()
    root1.resizable(False,False)
    root1.title('Forgot Login Id')
    L8 = Label(root1,text="Your first city name ?\n")
    L8.grid(row=1,column=0,columnspan=2)
    B8 = Entry(root1)
    B8.grid(row=2,column=0,columnspan=2)
    B9 = Button(root1,text="Submit",command=Forgot_y)
    B9.grid(row=3,column=0,columnspan=2,pady=5)
    L9 = Label(root1,text="")
    L9.grid(row=4,column=0,columnspan=2)
    root1.mainloop()
    
def Forgot_y():  
    global B8
    Q = "Nashik"
    for S in Q :
        if B8.get() == Q :
            print(L9.config(text="Your Login Id is - Shubham"))
            break
        if B8.get() != Q :
            print(L9.config(text="Please re-try !"))
            continue

def ForGot_P():
    global B82
    global L92
    root2= Toplevel()
    root2.resizable(False,False)
    root2.title('Forgot Password')
    L81 = Label(root2,text="What is your favourite sport ?")
    L81.grid(row=1,column=0,columnspan=2)
    B82 = Entry(root2)
    B82.grid(row=2,column=0,columnspan=2)
    B91 = Button(root2,text="Submit",command=Forgot_Z)
    B91.grid(row=3,column=0,columnspan=2,pady=5)
    L92 = Label(root2,text="")
    L92.grid(row=4,column=0,columnspan=2)
    root2.mainloop()
    

def Forgot_Z(): 
    global B82
    global L92 
    P = "Cricket"  
    for S in P :
        if B82.get() == P :
            print(L92.config(text="Your Password is - 1234"))
            break
        if B82.get() != P :
            print(L92.config(text="Please re-try !"))
            continue

                   
L1 = Label(root,text="Login Id :",bg="lightyellow",fg="indian red",width=15,relief=RAISED)
L1.grid(row=0,column=0)
E1 = Entry(root,width=15,relief=SUNKEN,bg="lightgreen")
E1.grid(row=0,column =1)
L2 = Label(root,text="Password :",bg="lightyellow",fg="indian red",width=15,relief=RAISED)
L2.grid(row=1,column=0)
E2 = Entry(root,bg="lightgreen",width=15,relief=SUNKEN)
E2.grid(row=1,column =1)
E2.config(show="*")
B1 = Button(root,text="Submit",command=SubMit,width=15,bg="sky blue")
B1.grid(row=2,column=0,padx=10,pady=10)
B2 = Button(root,text="Quit",command=root.quit,width=15,bg ="salmon")
B2.grid(row=2,column=1,padx=10,pady=10)
C1= Checkbutton(root,text="Remember Password",width=15)
C1.grid(row=3,column=0,columnspan=2)
L3 = Button(root,text="Forgot Login Id ? ",width=15,command=ForGot_L)
L3.grid(row=4,column=0,padx=10,pady=10)
L4 = Button(root,text="Forgot Password ? ",width=15,command=ForGot_P)
L4.grid(row=4,column=1,padx=10,pady=10)
B3 = Button(root,text="Create new Login ",width=15)
B3.grid(row=5,column=0,padx=10,pady=10,columnspan=2)
L5 = Label(root,text="",width=15,bg="black",fg="white")
L5.grid(row=6,column=0,columnspan=2)


root.mainloop()