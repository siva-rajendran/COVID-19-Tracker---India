import json
from tkinter import *
from tkinter.ttk import *

import threading

import requests


def data_src():
    req = requests.get("https://covid19-mohfw.herokuapp.com/")
    data = json.loads(req.content)

    total = data['totals']
    tc['text'] = total['total']
    ac['text'] = total['cases']
    rc['text'] = total['recoveries']
    dc['text'] = total['deaths']

def statedata(name):
    req = requests.get("https://covid19-mohfw.herokuapp.com/")
    data = json.loads(req.content)
    for state in data['states']:
        #print(state['state'])
        if state['state'] == name:
            statenametext['text'] = state['state']
            activecasestext['text'] = state['cases']
            recoveredcasestext['text'] = state['recoveries']
            deathcasestext['text'] = state['deaths']
            totalcasestext['text'] = state['total']

            rawdatatext.delete('1.0', END)
            rawdatatext.insert(INSERT, json.dumps(state, indent=1))
    
root = Tk()
root.geometry('720x480')
root.resizable(False,False)
root.configure(background="#ffffff")
root.title("India COVID-19 Tracker")

style = Style()
style.configure("TLabel", foreground="#000", background="#fff")


Label(root, text="COVID-19 TRACKER - INDIA", font = ("Tahoma",12,"bold"),foreground="#9C27B0").place(x=20,y=10)


Label(root, text="Total Cases", font = ("Calibri",12,"bold")).place(x=20,y=50)
Label(root, text="Active Cases", font = ("Calibri",12,"bold")).place(x=185,y=50)
Label(root, text="Recovered Cases", font = ("Calibri",12,"bold")).place(x=360,y=50)
Label(root, text="Total Deaths", font = ("Calibri",12,"bold")).place(x=535,y=50)


tc = Label(root, text = "-", font = ("Tahoma",16,"bold"),foreground="#FF9800")
tc.place(x=20,y=90)
ac = Label(root, text = "-", font = ("Tahoma",16,"bold"),foreground="#F44336")
ac.place(x=185,y=90)
rc = Label(root, text = "-", font = ("Tahoma",16,"bold"),foreground="#4CAF50")
rc.place(x=360,y=90)
dc = Label(root, text = "-", font = ("Tahoma",16,"bold"),foreground="#607D8B")
dc.place(x=535,y=90)


Label(root, text="Select your State to View COVID-19 Cases",font=("Calibri",12,"bold")).place(x=20, y=150)
statename = StringVar()
statechooser = Combobox(root, width=40, textvariable=statename)
statechooser['values'] = ('Andaman and Nicobar Islands', 'Andhra Pradesh','Arunachal Pradesh', 'Assam','Bihar', 'Chandigarh',
'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu','Delhi', 'Goa','Gujarat', 'Haryana','Himachal Pradesh', 'Jammu and Kashmir',
'Jharkhand', 'Karnataka','Kerala', 'Ladakh','Madhya Pradesh', 'Maharashtra','Manipur', 'Meghalaya','Mizoram', 'Nagaland','Odisha', 
'Puducherry','Punjab', 'Rajasthan','Sikkim', 'Tamil Nadu','Telangana', 'Tripura','Uttar Pradesh', 'Uttarakhand','West Bengal')
statechooser.current(0)
statechooser.place(x=20, y=190)

statebtn = Button(root, text="FETCH DATA", command=lambda:statedata(statename.get()))
statebtn.place(x=290,y=188)

statenamelabel = Label(root, text="State Name   : ",font=("Calibri",12)).place(x=20, y=240)
statenametext = Label(root, text="-",font=("Calibri",12,"bold"),foreground="#3F51B5")
statenametext.place(x=130, y=240)

activecaseslabel = Label(root, text="Active Cases : ",font=("Calibri",12)).place(x=20, y=280)
activecasestext = Label(root, text="-",font=("Calibri",12,"bold"),foreground="#F44336")
activecasestext.place(x=130, y=280)

recoveredcaseslabel = Label(root, text="Recoveries    : ",font=("Calibri",12)).place(x=20, y=320)
recoveredcasestext = Label(root, text="-",font=("Calibri",12,"bold"),foreground="#4CAF50")
recoveredcasestext.place(x=130, y=320)

deathcaseslabel = Label(root, text="Total Deaths : ",font=("Calibri",12)).place(x=20, y=360)
deathcasestext = Label(root, text="-",font=("Calibri",12,"bold"),foreground="#607D8B")
deathcasestext.place(x=130, y=360)

totalcaseslabel = Label(root, text="Total Cases   : ",font=("Calibri",12)).place(x=20, y=400)
totalcasestext = Label(root, text="-",font=("Calibri",12,"bold"),foreground="#FF9800")
totalcasestext.place(x=130, y=400)

##### RAW DATA PART #####

rawdatalabel = Label(root, text="Raw JSON Data(API Source)",font=("Calibri",12,"bold")).place(x=450, y=150)
rawdatatext = Text(root,font=("consolas",10), width=35, height=20,relief=FLAT,bg="#f2f2f2", fg="#16161d")
rawdatatext.place(x=450, y=188)

Label(root, text="Source : MOHFW.GOV.IN  | API : https://covid19-mohfw.herokuapp.com | https://github.com/vaibhavpandeyvpz/covid19-mohfw",font=("Calibri",10)).place(x=5, y=460)
data_src()
root.mainloop()
