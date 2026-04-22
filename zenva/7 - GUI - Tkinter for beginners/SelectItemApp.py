from tkinter import *
# import tkinter as tk

class SelectItemApp:
    def __init__(self, root):
        # root.title("app title")
        # root.geometry("500x400")
        # root.maxsize(1000,800)

        self.list_item_strings = ["item 1", "item 2", "item 3", "item 4", "item 5"]
        list_items = StringVar(value=self.list_item_strings)
        listBox = Listbox(root, listvariable=list_items)

        listBox.pack()
        listBox.place(x=100, y=200)
        # listBox.grid(column = 0, row = 2)

        listBox.configure(font=("Arial", 8), fg="black", bg="lightgray")
        listBox.configure(width = 30, height = self.list_item_strings.__len__())
        # listBox.bind("<<ListboxSelect>>", self.select_item)
        listBox.bind("<<ListboxSelect>>", lambda s: self.select_item_with_index(listBox.curselection()))
        # listBox.pack(side = tk.BOTTOM)
        

    def select_item(self, event): # give the event as parameter
        selected_index = event.widget.curselection()
        if selected_index:
            selected_item = event.widget.get(selected_index)
            print("Selected item:", selected_item)

    def select_item_with_index(self, index): # give directly the index
        selected_item = self.list_item_strings[index[0]]
        print("Selected item:", selected_item)