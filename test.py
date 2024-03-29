import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
win=tk.Tk()
win.title("Binary Tree Visualization")
win.minsize(800,400)
win.resizable(0,0)

informationLabel=tk.LabelFrame(win,text="Create Tree",width=400,height=200,padx=5,pady=5)
welcomeMsg=messagebox.showinfo("welcome","please let your entry be only Numbers, each number separated by a space")

informationLabel.pack()
L1 = tk.Label(informationLabel, text="Enter Numbers in order")
L1.pack()
entry = tk.Entry(informationLabel, bd =5)
entry.pack()

def get_data():
    label.config(text=entry.get(),font= ('Helvetica 13'))

label=tk.Label(win,text='hallo?',font='Helvetica 13')
label.pack()

ttk.Button(win,text="Insert",command=get_data).pack()

win.mainloop()
