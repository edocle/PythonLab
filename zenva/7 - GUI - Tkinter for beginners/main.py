from tkinter import *
from SwapTextApp import SwapTextApp
from SelectItemApp import SelectItemApp
from todolistApp import ToDoListApp



def main():
    root = Tk()
    ToDoListApp(root)
    # SwapTextApp(root)
    # SelectItemApp(root)
    root.mainloop()

main()