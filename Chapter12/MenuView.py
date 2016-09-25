import tkinter, time
from tkinter import messagebox
from Model import window
from Model import EventHandler

handler = EventHandler()

def showTime():
    messagebox.showinfo("Current Time", "Today is {0}\nCurrent time is {1}".format(time.strftime("%Y/%m/%d", time.localtime()), time.strftime("%H:%M:%S", time.localtime())))

def copying(event=None):
    window.clipboard_clear()
    window.clipboard_append(handler.numberDisplaying)

def pasting(event=None):
    
    handler.handle(window.clipboard_get())

fixedMenu = tkinter.Menu(window)

actionMenu = tkinter.Menu(fixedMenu, tearoff=0)
actionMenu.add_command(label="Time", command=showTime)
actionMenu.add_separator()
actionMenu.add_command(label="Quit", command=exit)
fixedMenu.add_cascade(label="Action", menu=actionMenu)
window.config(menu=fixedMenu)

rightClickMenu = tkinter.Menu(window)
rightClickMenu.add_command(label="Copy Result", command=copying)
rightClickMenu.add_command(label="Paste", command=pasting)

# right click menu
def rightClicking(event):
	rightClickMenu.post(event.x_root, event.y_root)
window.bind("<Button-2>", rightClicking)
window.bind("<Button-3>", rightClicking)

window.bind("<Shift-KeyPress-Q>", exit)
window.bind("<Shift-KeyPress-C>", copying)
window.bind("<Shift-KeyPress-V>", pasting)
