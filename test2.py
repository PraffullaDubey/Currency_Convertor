from tkinter import *
from tkinter.ttk import *
window=Tk()
window.configure(background="lightblue")
window.title("Currency Converter verion 1.0_by :praffulla")
l0=Label(window,text="WELCOME TO CURRENCY CONVERTER",font=("Times new roman",16))
l0.grid(column=1,row=0)
l1=Label(window,text="Enter amount in Dollars $",font=("Times new roman",16))
l1.grid(column=1,row=1)

txt=Entry(window,width=16)
txt.grid(column=1,row=2)
bt1=Button(window,text="Convert to INR")
bt1.grid(column=1,row=4)
l2=Label(window,text="Click on Convert button")
l2.grid(column=1,row=5)
window.geometry("550x400")
window.mainloop()
