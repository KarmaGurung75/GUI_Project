from tkinter import *
root= Tk()
myLabel=Label(root, text='tkinter')
myLabel2=Label(root , text="My name is karma")
myLabel3=Label(root, text="softwarica")

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=2, column=6)

root.mainloop()