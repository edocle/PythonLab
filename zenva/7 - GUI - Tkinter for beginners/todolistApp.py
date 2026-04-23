from tkinter import *
import tkinter as tk

class ToDoItem:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

class ToDoListApp:
    def __init__(self, root):
        root.title("To-Do List")

        frame = Frame(root, borderwidth=2, relief= "raised")
        frame.grid(column=1, row=1, sticky=(N,E,S,W))

        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)

        # Tasks list
        list_label = Label(frame, text="To Do Items")
        list_label.grid(column=1, row=1, sticky=(S,W))

        self.task_items = [
            ToDoItem("Workout", "Go to the gym and do a workout session."),
            ToDoItem("Grocery Shopping", "Buy groceries for the week."),
        ]

        self.task_description = StringVar()
        self.task_names = StringVar(value=list(map(lambda item: item.name, self.task_items)))

        items_list = Listbox(frame, listvariable = self.task_names)
        items_list.bind("<<ListboxSelect>>", lambda s: self.select_item_with_index(items_list.curselection()))
        items_list.grid(column=1, row=2, sticky=(E,W), rowspan=5)

        selected_description_label = Label(frame, textvariable=self.task_description)
        selected_description_label.grid(column=1, row=7, sticky=(E,W), columnspan=2)

        # New task
        new_item_label = Label(frame, text="New Item")
        new_item_label.grid(column=2, row=1, sticky=(S,W))
        
        name_label = Label(frame, text="Item name")
        name_label.grid(column=2, row=2, sticky=(S,W))

        self.new_task_name = StringVar()
        name_entry = Entry(frame, textvariable=self.new_task_name)
        name_entry.grid(column=2, row=3, sticky=(N,E,W))

        description_label = Label(frame, text="Description")
        description_label.grid(column=2, row=4, sticky=(S,W))

        self.new_task_description = StringVar()
        description_entry = Entry(frame, textvariable=self.new_task_description)
        description_entry.grid(column=2, row=5, sticky=(N,E,W))

        add_task_button = Button(frame, text="Save", command=self.add_task)
        add_task_button.grid(column=2, row=6, sticky=(E))

        for child in frame.winfo_children():
            child.grid_configure(padx=10, pady=5)
        
    def select_item_with_index(self, index): # give directly the index
        selected_item = self.task_items[index[0]]
        self.task_description.set(selected_item.description)

    def add_task(self):
        task_name = self.new_task_name.get()
        task_description = self.new_task_description.get()
        if task_name and task_description:
            task = ToDoItem(task_name, task_description)
            self.task_items.append(task)
            self.task_names.set(list(map(lambda item: item.name, self.task_items)))

            self.new_task_name.set("")
            self.new_task_description.set("")

    def delete_task(self, index):
        del self.task_items[index]
        self.task_names.set(list(map(lambda item: item.name, self.task_items)))