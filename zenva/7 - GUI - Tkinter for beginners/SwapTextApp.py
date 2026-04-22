from tkinter import *

class SwapTextApp:
    def __init__(self, root):
        root.title("app title")
        root.geometry("500x400")
        root.maxsize(1000,800)

        frame = Frame(root, width=400, height=400, bg="lightblue", relief = "sunken", borderwidth=2)
        frame.pack()
        frame.place(x=50, y=50)

        self.label_text = StringVar()
        label = Label(frame, textvariable=self.label_text)

        label.pack()
        label.place(x=10, y=10)
        # label.configure(width=30, height=1)
        # label.grid(column = 0, row = 0)

        self.label_text.set("update this text")

        # label["text"] = "Welcome to the app!"
        label["font"] = ("Courier", 16)
        # label.configure(text ="Welcome to the app!", font=("Courier", 16)) #same thing as above
        # label.configure(fg="white", bg="black")

        self.entry_text = StringVar()
        entry = Entry(frame, textvariable=self.entry_text)

        entry.pack()
        entry.place(x=10, y=60)
        # entry.configure(width=30, height=1)
        # entry.grid(column = 0, row = 1)

        entry.configure(font=("Arial", 14), fg="black", bg="lightgray")
        self.entry_text.set("Type something here...")
        # label["textvariable"] = self.entry_text

        button = Button(frame, text="Enter", command=self.on_button_click)

        button.pack()
        button.place(x=10, y=120)
        button.configure(width=30, height=1)
        # button.grid(column = 1, row = 1)
    
    def on_button_click(self):
        text = self.entry_text.get()
        self.label_text.set(text)