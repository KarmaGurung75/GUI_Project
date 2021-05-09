from tkinter import*


# creating the application main window
root = Tk()

redbutton = Button(root, text="left", fg="green")
redbutton.pack(side=LEFT)
name=Label(root,text="Name").grid(row=0,column=0)

# Entering the event main loop
root.mainloop()