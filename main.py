from tkinter import *
from tkinter.ttk import *
import requests
import json

def data_src():
    req = requests.get("https://covid19-mohfw.herokuapp.com/")
    data = json.loads(req.content)

    total = data['totals']
    tc['text'] = total['total']
    ac['text'] = total['cases']
    rc['text'] = total['recoveries']
    dc['text'] = total['deaths']

    
root = Tk()
root.geometry('720x480')
root.resizable(False,False)
root.configure(background="#ffffff")
root.title("India COVID-19 Tracker")

style = Style()
style.configure("TLabel", foreground="#000", background="#fff")


Label(root, text="COVID-19 TRACKER - INDIA", font = ("Tahoma",12,"bold"),background="#fdf").place(x=240,y=10)


Label(root, text="Total Cases", font = ("Calibri",12)).place(x=10,y=50)
Label(root, text="Active Cases", font = ("Calibri",12)).place(x=175,y=50)
Label(root, text="Recovered Cases", font = ("Calibri",12)).place(x=350,y=50)
Label(root, text="Total Deaths", font = ("Calibri",12)).place(x=525,y=50)


tc = Label(root, text = "-", font = ("Tahoma",16,"bold"),foreground="#fa0")
tc.place(x=20,y=90)
ac = Label(root, text = "-", font = ("Tahoma",16,"bold"),foreground="#f00")
ac.place(x=185,y=90)
rc = Label(root, text = "-", font = ("Tahoma",16,"bold"),foreground="#0a0")
rc.place(x=360,y=90)
dc = Label(root, text = "-", font = ("Tahoma",16,"bold"),foreground="#666")
dc.place(x=535,y=90)

data_src();

root.mainloop()
