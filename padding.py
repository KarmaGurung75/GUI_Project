from tkinter import *
root= Tk()
myButton=Button(root, text="Click me")
myButton.pack()

myButton1 = Button(root, text="Click", state=DISABLED)
myButton1.pack()

myButton2= Button(root, text='click', padx=50)
myButton2.pack()
myButton3= Button(root, text='click', padx=50, pady=50)
myButton3.pack()
root.mainloop()
