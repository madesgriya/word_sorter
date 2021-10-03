#importing library for GUI
import tkinter as tk
import subprocess as sub
from processor import stringSeparator

root = tk.Tk()
root.title("Matt's Word Sorter")

#creating canvas
canvas1 = tk.Canvas(root, width = 400, height = 250)
canvas1.pack()

#command label
label1 = tk.Label(root, text="Enter Your Sentence!")
label1.config(font=("helvetica", 14))
canvas1.create_window(200,100, window=label1)

#adding entry box
entry1 = tk.Entry(root)
canvas1.create_window(200,140, window=entry1)

#recalling the processor
#some dummy function --> to be replaced with the processor

def myFunction():  
    x1 = entry1.get()
    #label1 = tk.Label(root, text= float(x1)**0.5)
    label2 = tk.Label(root, text= stringSeparator(x1))
    canvas1.create_window(200, 210, window=label2)

#adding button
button1 = tk.Button(text="Sort Your Sentence", 
                    command= myFunction,
                    fg = "blue",
                    font = ("helvetica",12,"bold")
                    )
canvas1.create_window(200,180, window=button1)

root.mainloop()