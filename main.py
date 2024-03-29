import graphviz
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
win=tk.Tk()
win.title("Binary Tree Visualization")
win.minsize(800,400)
win.resizable(0,0)
win.configure(bg='#1f2937')

numbers=''
informationLabel=tk.LabelFrame(win,text="Create Tree",width=400,height=200,padx=30,pady=30,bg='#1f2937',fg="White")
welcomeMsg=messagebox.showinfo("welcome","please let your entry be only Numbers, each number separated by a space")
informationLabel.pack()
L1 = tk.Label(informationLabel, text="Enter Numbers in order",bg='#1f2937',fg="White")
L1.pack()
entry = tk.Entry(informationLabel, bd =5,bg='#1f2937',fg="White")
entry.pack()
label=tk.Label(win,text='',font='Helvetica 13',bg='#1f2937')
label.pack()






class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def visualizeInOrder(root):
    dot = graphviz.Digraph()
    dot.node(str(root.key))

    def add_nodes_edges(node):
        if node.left:
            dot.node(str(node.left.key))
            dot.edge(str(node.key), str(node.left.key))
            add_nodes_edges(node.left)
        if node.right:
            dot.node(str(node.right.key))
            dot.edge(str(node.key), str(node.right.key))
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    dot.render('binary_tree', view=True, format='png')
#delete
def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = get_min_value(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def get_min_value(root):
    while root.left is not None:
        root = root.left
    return root
#end of delete

# Example usage:
root = None
# keys = [5, 3, 7, 2, 4, 6, 8,1,9]
# for key in keys:
#     root = insert(root, key)
# visualizeInOrder(root)

def use(numbersList):
    root= None
    keys = numbersList
    for key in keys:
        root = insert(root, key)
    visualizeInOrder(root)
    
def get_data():
    numbers=entry.get()
    try:
        numbers = numbers.split()
        numbersList = [int(i) for i in numbers]
        use(numbersList)
        label.config(text="Check your files...Thank you :)",font= ('Helvetica 13'))
    except:
        label.config(text="please enter only numbers separated by one space")
    
ttk.Button(win,text="Insert",command=get_data).pack()

win.mainloop()