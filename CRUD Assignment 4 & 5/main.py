# Main module is used in this room for some tkinter and "running" process.
from tkinter import *
from application import Application

root = Tk()
root.geometry("400*250") # Size of the "main" window.ACTIVE
app= Application(root)
root.mainloop()
