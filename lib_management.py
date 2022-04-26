class library:
    def __init__(self,lob):
        self.books=lob
    def booksavail(self):
        print("\tbooks available are: ")
        for book in self.books:
            print(book)
    def borw(self,bname):
        if bname in self.books:
            print(f"\tBook of {bname} have been issued.\n\tTo be returned within a month")
            self.books.remove(bname)
            return True
        else:
            print("\tSorry,book not available...\nMay be it is borrowed by someone else")
            return False
    def retbook(self,bname):
        self.books.append(bname)
        print(" \tBook have been returned...")
class student:
    def __init__(self):
        self.blist=[]
    def reqbk(self):
        self.book=input("\tEnter the book you want to borrow: ")
        return self.book
    def retbook(self):
        self.book=input("\tEnter the name of the book you want to return: ")
        return self.book
if __name__ == '__main__':
    cenlib=library(["C","PYTHON","JAVA","HTML/CSS","C#","PHP"])
    #cenlib.booksavail()
    stud=student()
    while(True):
        msg='''\t****WELCOME TO CENTRAL LIBRARY AKGEC****\n\tPlease Choose the option:\n\t1:To see the booklist\n\t2:Request for a book\n\t3:Return a Book\n\t4:Exit the Library'''
        print(msg)
        a=int(input("\tEnter a choice: "))
        
        if a==1:
            cenlib.booksavail()
        elif a==2:
            cenlib.borw(stud.reqbk())
        elif a==3:
            cenlib.retbook(stud.retbook())
        elif a==4:
            print("\t \U0001F600  THANK YOU for your visit!!!!")
            exit()
        else:
            print("\tPlease Enter the correct choice!!!")
      

