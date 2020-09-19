                        # LIBRARY MANAGMENT SYSTEM
import time
import random

class library:
    secret_key = random.randint(1000, 9999)              # to get admin access
    delkey = random.randint(100, 999)                    # to get permission for deletion

    def __init__(self, libraryName, allBooks, listOfBooks):
        self.lendbooklis = {}
        self.allBooks = allBooks
        self.list_of_books = listOfBooks
        self.libraryName = libraryName

    def displayAllBooks(self):
        print(self.allBooks)

    def displayBooks(self):                         # to display all available books
        return print(self.list_of_books)

    def lendBook(self):                             # to lend books 
        lenderName = input("Enter your name : ")
        lendBook = input("Enter book you want to lend : ")
        if lendBook in self.list_of_books:
            print("You can take the book and donn't forgot to return on time.")
            self.lendbooklis[lenderName] = lendBook
            self.list_of_books.remove(lendBook)
        else:
            print(f"Book '{lendBook}' is currently not available")

    def displaylendedbook(self):                           # lend books info
        return print(self.lendbooklis)

    def addBook(self):                                     # to add new boos to library
        addbok = input("Enter the book you want to add : ")
        self.list_of_books.append(addbok)
        self.allBooks.append(addbok)

    def returnBook(self):                                   # to return a lend book
        retname = input("Enter your name : ")
        retbok = input("Enter book you want to return : ")
        self.list_of_books.append(retbok)
        self.lendbooklis.pop(retname)

    def removeBook(self):                                   # to delete books from libraby permanently
        count = 2
        while (count > 0):
            rmvkey = input("Enter 'Deletion-key' = ")
            if rmvkey == self.delkey:
                delbook = input("enter book you want to remove from your library : ")
                if delbook in self.list_of_books:
                    self.list_of_books.remove(delbook)
                    self.allBooks.remove(delbook)
                    break
                else: print("No such book in library to remove")
            else:
                    print("Invalid key!")
            count -= 1

    def changeKey(self):
        key = int(input("Enter secret key : "))
        count = 2
        while count>0:
            if key == self.secret_key:
                while True:
                    keyChange = input("\t1 --> Change Secret Key\n\t2 --> Change deletion key")
                    if keyChange == "1":
                        while True:
                            new_secretKey1 = int(input("Enter new Secret key : "))
                            new_secretKey2 = int(input("Re-enter new Secret key : "))
                            if new_secretKey1 == new_secretKey2:
                                self.secret_key = new_secretKey1
                                break
                            else:
                                print("key didn't match..!")
                                continue
                    elif keyChange == "2":
                        while True:
                            new_delKey1 = int(input("Enter new Deletion key : "))
                            new_delKey2 = int(input("Re-enter new Deletion key : "))
                            if new_delKey1 == new_delKey2:
                                self.delkey = new_delKey1
                                break
                            else:
                                print("key didn't match..!")
                                continue
                    elif keyChange == "0":
                        print("exit...")
                        time.sleep(3)
                        break
                    else:
                        print('INVALID OPTION..! Try again')
                        continue
            else:
                print('INVALID KEY..!')
                count -= 1
                continue

# admin() method, for Admin functions (includes all functions)
def admin():
    print("\tDisplay all available books --> 1\tLend book --> 2\n\tDisplay lended books --> 3\t\t\tAdd new book --> 4"
          "\n\tReturn a book --> 5\t\t\t\t\tRemove book --> 6\n\tDisplay All books --> 7"
          "\t\t\t\tChange Keys --> 8\n\tExit --> 0")
    choice = int(input("Enter your choice : "))
    Exit = False
    try:
        while Exit is not True:
            if choice == 0:
                localtime = time.asctime(time.localtime(time.time()))
                Exit = True
                return f"Thank You, hope you like our service!\t\t\t\t{localtime}"
            elif choice == 1:
                xlib.displayBooks()
            elif choice == 2:
                xlib.lendBook()
            elif choice == 3:
                xlib.displaylendedbook()
            elif choice == 4:
                xlib.addBook()
            elif choice == 5:
                xlib.returnBook()
            elif choice == 6:
                xlib.removeBook()
            elif choice == 7:
                xlib.displayAllBooks()
            elif choice == 8:
                xlib.changeKey()
            else:
                print("Invalid choice")
            choice = int(input("Enter your choice : "))
    except Exception as e:
        print(e)

#  userfun() method, for user functions (allows display, lend & return books)
def userfun():
    print("  Display all available books --> 1\t\t\tLend book --> 2\n\t\t    Display all books --> 4\t"
          "\tReturn a book --> 3\nExit --> 0")
    choice = int(input("Enter your choice : "))
    Exit = False
    while Exit is not True:
        if choice == 0:
            localtime = time.asctime(time.localtime(time.time()))
            Exit = True
            return f"Thank You, visit again!!\t\t\t\t{localtime}"
        elif choice == 1:
            xlib.displayBooks()
        elif choice == 2:
            xlib.lendBook()
        elif choice == 3:
            xlib.returnBook()
        elif choice == 4:
            xlib.displayAllBooks()
        else:
            print("Invalid choice")
        choice = int(input("Enter your choice : "))

exit = False
while exit is not True:
    libname = input("Enter your library name : ")
    initai_stock = int(input("Enter number of book you're putting in library : "))
    initial_book_list = []
    print("enter books")
    for item in range(initai_stock):
        bookstock = input()
        initial_book_list.append(bookstock)
    ALLBOOKS = initial_book_list[:]
    # library.secret_key = random.randint(1000, 9999)
    # library.delkey = random.randint(100, 999)
    xlib = library(libname, ALLBOOKS, initial_book_list)

    print(f"\tYour secret key = {library.secret_key}\n\t Your deletion key = {library.delkey}\n")

    all_set = input("We're all set, press any key to start\t\t\tpress 0 to make changes or setup again\n"
                    "\t\t\t\t\t\t\t\t\t\t ")
    if all_set == "0":
        continue
    else:
        break
#  xlib = library(libname, allBooks, initial_book_list)

#  xlib = library("xlibrary12", ["book1", "book2", "book3","book4"], ["book1", "book2", "book3","book4"])

lib2 = library.secret_key                 # secret key object

if __name__ == '__main__':                # main function
    localtime = time.asctime(time.localtime(time.time()))
    print(f"{localtime}\t\t\t\t\t\t\tExit --> 0")
    Exit = False
    while Exit is not True:
        user = input("Are you admin (y/n) : ")
        kc=2
        if user == "y":
            while(kc > 0):
                adkey = int(input("Enter admin key : "))
                if adkey == lib2:
                    print("////////////WELCOME SIR!/////////////")
                    print(admin())
                    break
                else:
                    print("Invalid key!")
                kc -= 1
        elif user == "n":
            print(f"/////////////////////Welcome to {xlib.libraryName}//////////////////////// ")
            print(userfun())
        elif user == "0":
            Exit = True
            continue
        else:
            print("Please answer in y for 'yes' or n for 'no' ")
