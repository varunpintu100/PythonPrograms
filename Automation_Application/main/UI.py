from tkinter import *
from main.WebDrivers import WebDriver

def clicked():
    Browser_Name = Name.get()
    driver = WebDriver(Browser_Name)
    return driver
if __name__=="__main__":
    App_Name = "Automation_Application"
    window = Tk(className=App_Name)# set window size
    window.geometry("900x600")
    l1=Label(window, text="Enter the Browser you want to invoke : ",font=("Courier",14),fg='Black')
    l1.pack()
    Name=Entry(window,width=45)
    Name.pack()
    bt1=Button(window,text="Select Browser",command=clicked,relief=SOLID,font=("Courier",10))
    bt1.config(height=1,width=15)
    bt1.place(x=350,y=55)
    window.mainloop()