from tkinter import *
root= Tk()
root.title("frame")

Frame= LabelFrame(root, text="My Frame", padx=5, pady=5)
Frame.pack(padx=10, pady=10)

frame=LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10,pady=10)
button1=Button(frame, text="click this")
button1.grid()

root.mainloop()