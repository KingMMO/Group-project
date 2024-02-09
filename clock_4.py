from tkinter import * # this is were we import the library responsible for the functioning of the application
clk = Tk() # this is the creation and start of the program

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