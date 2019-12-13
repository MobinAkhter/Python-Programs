from crud import CRUD
from tkinter import * # Imports everything from the tkinter module
import json

class Application(Frame,CRUD): 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.window(100,10)
    
    # Creating the gui window
    def window(mainWindow, row=None, col=None):
        mainWindow.master.title("Library") # Changes the "Tk" symbol at the top of the gui window to "Library"

        mainWindow.pack(fill=BOTH, expand=1)

        # Creating "buttons" inside the window
        # First paramater is for the location where you want to create the button.
        # Second parameter is for the specific text you want to appear on the gui window
        # Third parameter is for making the button access a method which does further operations.
        # Fourth parameter  is for the background color 
        # Fifth parameter is for the foreground color.
        addBookButton = Button(mainWindow, text="Add a book to your library", command=mainWindow.addBook, bg="blue", fg="white")
        searchSpecificBook = Button(mainWindow, text="Search for a Book", command=mainWindow.searchABook, bg="purple", fg="white")
        deleteABook = Button(mainWindow, text="Delete a book ", command=mainWindow.deleteBook, bg="yellow", fg="black")
        searchBookHistory = Button(mainWindow, text="Book record", command=mainWindow.bookHistory, bg="green", fg="black")
        quitButton = Button(mainWindow, text="Exit", command=mainWindow.exit, bg="red" , fg="white" )

        addBookButton.pack()
        addBookButton.place(x=0, y=0)
        addBookButton.pack(fill=X)

        searchSpecificBook.pack()
        searchSpecificBook.place(x=1, y=0)
        searchSpecificBook.pack(fill=X)

        deleteABook.pack()
        deleteABook.place(x=2, y=0)
        deleteABook.pack(fill=X)

        searchBookHistory.pack()
        searchBookHistory.place(x=3, y=0)
        searchBookHistory.pack(fill=X)

        quitButton.pack()
        quitButton.place(x=4, y=0)
        quitButton.pack(fill=X)

        menu = Menu(mainWindow.master)
        mainWindow.master.config(menu=menu)

        file = Menu(menu)

        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)

        edit.add_command(label = "Undo")

        menu.add_cascade(label="Edit", menu=edit)

    def exit(self):
        print("Good-Bye!")
    
    def bookHistory(self):
        with open("data.json", "r") as f:
            data = f.read()
            json_data = json.loads(data)
        print("|=================================|")
        print("|", "{:<20} {:<!5} {:<10}".format("Book", "Author", "Price", "|"))
        print("|=================================|")
        for k, v in sorted(json_data.items()):
            book, author, price = v.values()
            print("|", "{:<20} {:<15} {:<10}".format(book, author, price), "|")
        print("|=================================|")
        return True

    def addBook(self):
        book = input("Add book: ")
        CRUD.create(self,book)
    
    def deleteBook(self):
        book = input("Delete book: ")
        CRUD.delete(self, book) # Uses the delete method in crud module

    def searchABook(self, *args):
        book = input("Search a book: ")
        CRUD.Search(self, book)
        choice = input("Press y/Y to continue or n/N t end the application.")
        if choice.lower() == "y" or choice.lower() == "yes":
            while False:
                print("Here is the list of options to choose from: ")
                list_of_options = {
                    1: "Add a book",
                    2: "Search a book",
                    3: "Delete a book",
                    4: "Search all the library books",
                    5: "Exit"
                }        
        elif choice.lower() == "n" or choice.lower() == "no":
            print("Good-Bye!")
            sys.exit()
        else:
            print("You did not enter what you were supposed to!\nGood-Bye!")