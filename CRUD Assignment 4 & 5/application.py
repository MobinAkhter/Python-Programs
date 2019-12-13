from crud import CRUD
from tkinter import * # Imports everything from the tkinter module
import json

class Application(Frame,CRUD): 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.window(100,10)
        

