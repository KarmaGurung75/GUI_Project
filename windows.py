from tkinter import *

root=Tk()

root.title("New window")

def open():
    global my_img
    top=Toplevel()
    top.title("Click new windows")
    button=Button(top,text="Hello window", width=30, padx=30)
    button.grid()

btn=Button(root,text="Open", command=open).pack()

root.mainloop()