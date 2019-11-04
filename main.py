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
def saveAs():
    f = asksaveasfile(mode='w',defaultextension='.txt')
    t = text.get(0.0,END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!", message="Unable to save file..")

def openFile():
    f = askopenfile(mode='r')
    t=f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

root = Tk()
root.title("My python text editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As..", command=saveAs)
filemenu.add_command()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
