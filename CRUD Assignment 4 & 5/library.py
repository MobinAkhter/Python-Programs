import json 
class Library:
    def __init__(self):
        self.dict= None 
        open("data.json") # Opens the "data.json" file\
        self.dict = json.load(f)
        f.close() # I think close takes out information from the "buffer" where if
        # you do not close a file it stores what you have done but does not perform tasks
        # like you want to.