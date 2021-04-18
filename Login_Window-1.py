from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Login Window")

def SubMit():
    if E1.get() == "Shubham" and E2.get() == "1234" :
        print("Login successful !")
        E1.delete(0,END)
        E2.delete(0,END)
    else  :
        print("Login Failed !")

def ForGot_L():
    Q = "Nashik"

    for S in Q :
        S = input("Your first city name ? ")
        if S == Q :
            print("Your Login Id is - Shubham")
            break
        if S != Q :
            print("Please re-try !")
            continue

def ForGot_P():
    P = "Cricket"
    
    for S in P :
        S = input("What is your favourite sport ?")
        if S == P :
            print("Your Password is - 1234")
            break
        if S != P :
            print("Please re-try !")
            continue
 
L1 = Label(root,text="Login Id :",bg="lightyellow",fg="indian red",width=15,relief=RAISED)
L1.grid(row=0,column=0)
E1 = Entry(root,bg="lightgreen",width=15,relief=SUNKEN)
E1.grid(row=0,column =1)
L2 = Label(root,text="Password :",bg="lightyellow",fg="indian red",width=15,relief=RAISED)
L2.grid(row=1,column=0)
E2 = Entry(root,bg="lightgreen",width=15,relief=SUNKEN)
E2.grid(row=1,column =1)
E2.config(show="*")
B1 = Button(root,text="Submit",command=SubMit,width=15)
B1.grid(row=2,column=0,padx=10,pady=10)
B2 = Button(root,text="Quit",command=root.quit,width=15)
B2.grid(row=2,column=1,padx=10,pady=10)
L3 = Button(root,text="Forgot Login Id ? ",width=15,command=ForGot_L)
L3.grid(row=4,column=0,padx=10,pady=10)
L4 = Button(root,text="Forgot Password ? ",width=15,command=ForGot_P)
L4.grid(row=4,column=1,padx=10,pady=10)
C1= Checkbutton(root,text="Remember Password",width=15)
C1.grid(row=3,column=0,columnspan=2)

root.mainloop()
