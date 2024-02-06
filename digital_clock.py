from tkinter import * # this is were we import the library responsible for the functioning of the application
import time # we import the library responsible for the live time preview
clk = Tk() # this is the creation and start of the program
clk.title("the clock") # this is the name of the application
clk.geometry("1350x700+0+0") # width, height, x-axis, y-axis, we have kept 0 because we will start form left top corner
clk.config(bg = "#ab245f") # you can give ny color you want

def clock():
    hr = str(time.strftime("%H")) # this is the variable representing hour for time
    mn = str(time.strftime("%M")) # this is the variable representing minutes for time
    sc = str(time.strftime("%S")) # this is the variable representing seconds for time

    if int(hr)>12 and int(mn)>0: # this is the conditional responsible for determining the AM and PM
        lb_dn.config(text="PM")
    if int(hr)>12:
        hr=str(int(int(hr)-12))

    lb_hr.config(text = hr ) # responsible for updating the value of this variable
    lb_mn.config(text = mn ) # responsible for updating the value of this variable
    lb_sc.config(text = sc ) # responsible for updating the value of this variable

    lb_hr.after(200, clock) # responsible for updating the values for time in realtime, live on the program


lb_hr = Label(clk,text= "12", font=("Times 20 bold", 75, "bold"),bg = "#087507",fg="white" ) # variable responsible for the font and display of the HOUR
lb_hr.place(x=350,y=200,width=150,height=150) # variable responsible for the font and display of the HOUR position

lb_hr_txt = Label(clk, text="HOUR",font=("Times 20 bold",20,"bold"),bg="#087507", fg="white") # variable responsible for the font and display of the HOUR TEXT
lb_hr_txt.place(x=350,y=360,width=150,height=50) # variable responsible for the font and display of the HOUR TEXT position

lb_mn = Label(clk,text= "12", font=("Times 20 bold", 75, "bold"),bg = "#00bea4",fg="white" ) # variable responsible for the font and display of the MINUTE
lb_mn.place(x=520,y=200,width=150,height=150) # variable responsible for the font and display of the MINUTE position

lb_mn_txt = Label(clk, text="MINUTE",font=("Times 20 bold",20,"bold"),bg="#00bea4", fg="white") # variable responsible for the font and display of the MINUTE TEXT
lb_mn_txt.place(x=520,y=360,width=150,height=50) # variable responsible for the font and display of the  MINUTE TEXT position

lb_sc = Label(clk,text= "12", font=("Times 20 bold", 75, "bold"),bg = "#06b488",fg="white" ) # variable responsible for the font and display of the SECONDS
lb_sc.place(x=690,y=200,width=150,height=150) # variable responsible for the font and display of the SECONDS position

lb_sc_txt = Label(clk, text="SECONDS",font=("Times 20 bold",20,"bold"),bg="#06b488", fg="white") # variable responsible for the font and display of the SECONDS TEXT
lb_sc_txt.place(x=690,y=360,width=150,height=50) # variable responsible for the font and display of the SECONDS TEXT position

lb_dn = Label(clk,text= "AM", font=("Times 20 bold", 70, "bold"),bg = "#9f0646",fg="white" ) # variable responsible for the font and display of the AM and PM
lb_dn.place(x=860,y=200,width=150,height=150) # variable responsible for the font and display of the AM and PM position

lb_dn_txt = Label(clk, text="NOON",font=("Times 20 bold",20,"bold"),bg="#9f0646", fg="white") # variable responsible for the font and display of the AM and PM TEXT
lb_dn_txt.place(x=860,y=360,width=150,height=50) # variable responsible for the font and display of the AM and PM TEXT position

clock() # this is to run the clock function defined above
clk.mainloop() # this is the end of the application
