import time # we import the library responsible for the live time preview

def clock():
    hr = str(time.strftime("%H")) # this is the variable representing hour for time
    mn = str(time.strftime("%M")) # this is the variable representing minutes for time
    sc = str(time.strftime("%S")) # this is the variable representing seconds for time

    if int(hr)>12 and int(mn)>0: # this is the conditional responsible for determining the AM and PM
        lb_dn.config(text="PM")
    if int(hr)>12:
        hr=str(int(int(hr)-12))