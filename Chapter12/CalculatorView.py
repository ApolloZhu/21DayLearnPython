import tkinter
from Model import window
from Model import Button
from Model import EventHandler

handler = EventHandler()

buttons = [
    Button("log",0,1),Button("exp",1,1),Button("C",2,1),Button("%",3,1),Button("+/-",4,1),Button("/",5,1),
    Button("acos",0,2),Button("cos",1,2),Button("7",2,2),Button("8",3,2),Button("9",4,2),Button("*",5,2),
    Button("asin",0,3),Button("sin",1,3),Button("4",2,3),Button("5",3,3),Button("6",4,3),Button("-",5,3),
    Button("atan",0,4),Button("tan",1,4),Button("1",2,4),Button("2",3,4),Button("3",4,4),Button("+",5,4),
    Button("pow",0,5),Button("sqrt",1,5),Button("0",2,5,width=2),Button(".",4,5),Button("=",5,5)
]

__displayVal = tkinter.StringVar()

def load():
    layoutLabel(window)
    layoutButtons(window)
    window.bind("<Return>", enter)

def layoutLabel(root):
    __displayVal.set("0")
    tkinter.Label(root, textvariable=__displayVal).grid(row=0,column=0,columnspan=6,sticky=tkinter.E)

def layoutButtons(root):
    for button in buttons:
        real = tkinter.Button(root, text=button.title)
        real.bind("<Button-1>", sendEvent)
        real.grid(column=button.x,row=button.y,columnspan=button.w, rowspan=button.h, sticky=tkinter.W+tkinter.E)

def sendEvent(event):
    handler.handle(event.widget['text'])

def enter(event):
    handler.handle('=')

def setDisplay(val):
    __displayVal.set(str(val))
