from tkinter import *
from tkinter import filedialog

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0,END)#line 0 coloum 0

def saveFile():
    global filename
    t = text.get(0.0,END)#store all the text from text box
    f= open(filename,'w')#open the file
    f.write(t)#store 
    f.close()
