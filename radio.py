from tkinter import *
root=Tk()
root.title=("Radio")

MODES=[
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("onion","Onion")
]

pizza=StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel=Label(root, text=value)
    myLabel.pack()
myButton=Button(root, text="click", command=lambda :clicked(pizza.get())).pack()

root.mainloop()