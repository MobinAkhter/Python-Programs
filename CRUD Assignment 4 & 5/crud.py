import json 
from library import library

class CRUD:
    def __init__(self):
        self.book_name = None

    def create(self, book_name):
        if book_name not in lib:
            # Exception handling below
            try:
                author_name= input("Author name: ")
                if len(author_name) ==0 or author_name.strip() == "":
                    # Line of code above basically checks if the user did not enter anything
                    raise ValueError
                price = input("Book price: ")
                if len(price) ==0 or price.strip == "":
                    raise ValueError
            except:
                print("ValueError : You did not enter anything ")
                return False
            
            lib[book_name] = {"name": book_name, "author": author_name, "price": "$ " + price}
            j = json.dumps(lib)
            f= open("data.json", "w") # w => writes to file
            f.write(j)
            print("Your", book_name, "has been added to the list in the library")
            f.close()
            return True
        else:
            print(book_name, " : already exists in the library.")
            opt = input("Do you want to add books again? Enter y/Y or n/N")
            if opt.lower() == "y" or opt.lower() == "yes":
                book_name = input("Name of the book you want to add: ")
                CRUD.create(self, book_name)
            elif opt.lower() == "n" or opt.lower() == "no":
                return False
            else:
                print("Not a valid entry")
                raise ValueError
    # The method below lists out all the books that exist in the libraray. 
    def search(self, book_name):
        if book_name in lib:
            print("search details", "\n", "book name\t:\t", lib[book_name]["name"]
            , "\n", "author\t\t:\t", lib[book_name]["author"]
            , "\n", "price\t\t:\t", lib[book_name]["price"])
            return True
        else:
            print("Sorry!", book_name, "does not exist in your library ")
            return False
    def delete(self, book_name):
        if book_name in lib:
            print(lib.pop(book_name), "has been deleted from the library")

            j = json.dumps(lib)
            f = open("data.json", "w")
            f.write(j)
            print("Your book has been removed from the library")
            f.close()
            return True
        else:
            print(book_name, "does not exists in the library")
            return False

lib = Library().dict
crud = CRUD()
