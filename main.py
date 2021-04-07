class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
        if self.books == None:
            print("No books available")
    def studetails(self):
        try:
            nameenrollno = input(
                "\nplease Enter your Full Name follwing Your College Enroll No..\n")
            gender = input("Please Enter your Gender : ")
            if(gender == 'Male' or gender == 'male' or gender == 'MALE'):
                print(
                    f"\nWelcome, Mr.{nameenrollno} in your College Library..!!!\n")
            elif(gender == 'Female' or gender == 'female' or gender == 'FEMALE'):
                print(
                    f"\nWelcome, Miss.{nameenrollno} in your College Library..!!!\n")
            else:
                print("please enter Valid Gender")
        except ValueError:
            print("enter correct value")
    def displayAvailableBooks(self):
        i = 1
        print("The Books present in Your College Library are : \n")
        for book in self.books:
            print(f"\t{i}. {book}")
            i = i+1

        
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued {bookName}. Please keep it safe, and return it within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, this book is either not available or has been issued to someone else Please wait until the book is available.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print(
            f"Thanks for returning {bookName} | Hope you enjoyed it. |  Have a great day ahead !")


class Student:
    def requestBook(self):
        
        print("\n")
        self.book = input("Enter the Name of the book you want to Borrow : ")
        

        return self.book

    def returnBook(self):
        self.book = input("Enter the Name of the book you want to Return : ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Ktinker", "Python", "achine Learning using Python","Java Servlet", "Data Structure", "DBMS", "Data Communication"])
    student = Student()
    centralLibrary.studetails()
    while(True):

        welcomeMsg = '''\n===========Welcome to Central library==========
        Please Choose an option:
        1. Listing all the Books
        2. Request a Book
        3. Donate/Retuen a Book
        4. Exit the Library\n'''
        print(welcomeMsg)
        try:
            a = int(input("Enter a Choice : "))
        except Exception as e:
            print("please enter the correct neumeric value choice from the given list..")
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for Choosing central Library. Have a great day Ahead!")
            exit()
        else:
            print("Invalid choice")
