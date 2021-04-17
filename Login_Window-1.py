from tkinter import *

root = Tk()

root.title("Login Window")



def SubMit():
    if E1.get() == "Shubham" and E2.get() == "1234" :
        print("Login successful !")
    else  :
        print("Login Failed !")
    
    

L1 = Label(root,text="Login Id :",bg="lightyellow",fg="indian red",width=15,relief=RAISED)
L1.grid(row=0,column=0)
E1 = Entry(root,bg="lightgreen",width=15,relief=SUNKEN)
E1.grid(row=0,column =1)
L2 = Label(root,text="Password :",bg="lightyellow",fg="indian red",width=15,relief=RAISED)
L2.grid(row=1,column=0)
E2 = Entry(root,bg="lightgreen",width=15,relief=SUNKEN)
E2.grid(row=1,column =1)
B1 = Button(root,text="Submit",command=SubMit,width=15)
B1.grid(row=2,column=0)
B2 = Button(root,text="Quit",command=root.quit,width=15)
B2.grid(row=2,column=1)


root.mainloop()